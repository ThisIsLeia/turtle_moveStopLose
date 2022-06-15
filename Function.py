# 載入套件
import time,OrderCMD

# 下單指令執行檔路徑
execpath = 'C:/OrderCmd/'

# 市價單
def MKT(Prod,BS,Qty):
    OrderNo = OrderCMD.OrderMKT(Prod,BS,Qty)
    time.sleep(1)
    OrderInfo = OrderCMD.GetAccount(OrderNo)
    return OrderInfo
    
# 範圍市價單
def RangeMKT(Prod,BS,Price,Qty,n):
    # 設定下單的價格
    if BS=='B':
        OrderPrice=str(int(Price)+n)
    elif BS=='S':
        OrderPrice=str(int(Price)-n)   
    OrderNo = OrderCMD.OrderLMT(Prod,BS,OrderPrice,Qty)
    
    while True:
        time.sleep(1)
        OrderInfo = OrderCMD.GetAccount(OrderNo)
        # 已成交
        if OrderInfo[-1] == '1':
            return OrderInfo           
    
# 浮動範圍市價單
def MoveRangeMKT(Prod,BS,Price,Qty,n,Sec):
    # 設定下單的價格
    if BS=='B':
        OrderPrice=str(int(Price)+n)
    elif BS=='S':
        OrderPrice=str(int(Price)-n)
    OrderNo = OrderCMD.OrderLMT(Prod,BS,OrderPrice,Qty)
    StartTime=time.time()

    while True:
        time.sleep(1)
        OrderInfo = OrderCMD.GetAccount(OrderNo)
        # 尚未成交
        if OrderInfo[-1] == '0':
            # 還在時間內
            if time.time()-StartTime<Sec:
                print('尚未成交')
            # 超過時間
            else:
                # 刪除舊的委託單
                status = OrderCMD.OrderCancel(OrderNo)
                # 刪單成功，重新下單
                if status == 'CancelSuccess':
                    # 重新設定下單的價格
                    if BS=='B':
                        OrderPrice=str(int(OrderPrice)+n)
                    elif BS=='S':
                        OrderPrice=str(int(OrderPrice)-n)
                    OrderNo = OrderCMD.OrderLMT(Prod,BS,OrderPrice,Qty)
                    StartTime = time.time()
                    print('重新下單',OrderNo,OrderPrice)
                # 刪單過程中已成交
                else:
                    return OrderInfo
        # 已成交
        else:
            return OrderInfo

# 限價單到期刪單
def LMT2DEL(Prod,BS,Price,Qty,Sec):
    OrderNo = OrderCMD.OrderLMT(Prod,BS,Price,Qty)
    StartTime=time.time()
    # 還在時間內
    while time.time()-StartTime<Sec:
        time.sleep(1)
        OrderInfo = OrderCMD.GetAccount(OrderNo)
        # 尚未成交
        if OrderInfo[-1] == '0':
            print('尚未成交')
        # 已成交
        else:
            return OrderInfo
    # 超過時間，刪除委託單
    status = OrderCMD.OrderCancel(OrderNo)
    # 刪單成功，回傳False代表沒有成交
    if status == 'CancelSuccess':
        print('已刪單')
        return False   
    # 刪單過程中已成交    
    else:
        return OrderInfo
    
# 限價單轉市價單
def LMT2MKT(Prod,BS,Price,Qty,Sec):
    OrderNo = OrderCMD.OrderLMT(Prod,BS,Price,Qty)
    StartTime=time.time()
    # 還在時間內
    while time.time()-StartTime<Sec:
        time.sleep(1)
        OrderInfo = OrderCMD.GetAccount(OrderNo)
        # 尚未成交
        if OrderInfo[-1] == '0':
            print('尚未成交')
        # 已成交
        else:
            return OrderInfo
    # 超過時間，刪除委託單
    status = OrderCMD.OrderCancel(OrderNo)
    # 刪單成功，改下市價單
    if status == 'CancelSuccess':
        OrderNo = OrderCMD.OrderMKT(Prod,BS,Qty)
        time.sleep(1)
        OrderInfo = OrderCMD.GetAccount(OrderNo)
        print('已刪單並轉市價單')
        return OrderInfo
    # 刪單過程中已成交    
    else:
        return OrderInfo
