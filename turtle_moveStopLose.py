import GetData,OrderCMD

Prod = 'TXFH7'
Date = '20170803'

BS = None
MaxPrice = 0
MinPrice = 999999

T1 = '08:45:00.00'
T2 = '09:00:00.00'
T3 = '12:00:00.00'
StopLoss = 30

# 區間高低點判斷
for i in GetData.GetMatch(Prod,Date):
    T = i[0][-11:]  # 時間
    P = float(i[2]) # 價格
    if T >= T1 and T < T2:
        MaxPrice = max(MaxPrice,P)
        MinPrice = min(MinPrice,P)
    elif T >= T2:
        break
    
print('MaxPrice:',MaxPrice,'MinPrice:',MinPrice)

# 進場
for i in GetData.GetMatch(Prod,Date):
    T = i[0][-11:]  # 時間
    P = float(i[2]) # 價格
    if T >= T2 and T < T3:
        # 多單進場
        if BS == None and P > MaxPrice:
            BS = 'B'
            # 下市價單(商品名稱,下單方向,下單口數)
            OrderNo = OrderCMD.OrderMKT(Prod,'B','1')
            OrderInfo = OrderCMD.GetAccount(OrderNo)
            # 下單時間及價格
            OrderTime = OrderInfo[7]
            OrderPrice = float(OrderInfo[4])
            print(BS,'OrderTime:',OrderTime,'OrderPrice:',OrderPrice)
            break
        # 空單進場
        elif BS == None and P < MinPrice:
            BS = 'S'
            # 下市價單(商品名稱,下單方向,下單口數)
            OrderNo = OrderCMD.OrderMKT(Prod,'S','1')
            OrderInfo = OrderCMD.GetAccount(OrderNo)
            # 下單時間及價格
            OrderTime = OrderInfo[7]
            OrderPrice = float(OrderInfo[4])
            print(BS,'OrderTime:',OrderTime,'OrderPrice:',OrderPrice)
            break
    else:
        break
        
# 出場    
for i in GetData.GetMatch(Prod,Date):
    T = i[0][-11:]  # 時間
    P = float(i[2]) # 價格

    # 持有多單
    if BS == 'B':
        MaxPrice = max(MaxPrice,P)
        Condition1 = T >= T3                  # 超過出場時間
        Condition2 = P <= MaxPrice - StopLoss # 移動式停損
        if Condition1 or Condition2:
            # 下市價單(商品名稱,下單方向,下單口數)
            CoverNo = OrderCMD.OrderMKT(Prod,'S','1')
            CoverInfo = OrderCMD.GetAccount(OrderNo)
            # 下單時間及價格
            CoverTime = CoverInfo[7]
            CoverPrice = float(CoverInfo[4])
            print('S','CoverTime:',CoverTime,'CoverPrice:',CoverPrice)
            break 
    # 持有空單
    elif BS == 'S':
        MinPrice = min(MinPrice,P)
        Condition1 = T >= T3                  # 超過出場時間
        Condition2 = P >= MinPrice + StopLoss # 移動式停損
        if Condition1 or Condition2:
            # 下市價單(商品名稱,下單方向,下單口數)
            CoverNo = OrderCMD.OrderMKT(Prod,'B','1')
            CoverInfo = OrderCMD.GetAccount(OrderNo)
            # 下單時間及價格
            CoverTime = CoverInfo[7]
            CoverPrice = float(CoverInfo[4])
            print('B','CoverTime:',CoverTime,'CoverPrice:',CoverPrice)
            break 