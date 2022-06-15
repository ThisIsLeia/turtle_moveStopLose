# 匯入模組
import subprocess

# 下單指令執行檔路徑
execpath = 'C:/OrderCmd/'

# 下市價單(商品名稱,下單方向,下單口數)
def OrderMKT(prod,bs,qty):
	OrderNo = subprocess.check_output([execpath+'Test_Order.exe',prod,bs,'0',qty,'MKT','IOC','0']).decode('big5').strip('\r\n')
	return OrderNo

# 下限價單(商品名稱,下單方向,下單價格,下單口數)
def OrderLMT(prod,bs,price,qty):
	OrderNo = subprocess.check_output([execpath+'Test_Order.exe',prod,bs,price,qty,'LMT','ROD','0']).decode('big5').strip('\r\n')
	return OrderNo

# 取消委託單(委託單編號)
def OrderCancel(SNVS):
	return subprocess.check_output([execpath+'Test_Order.exe','Delete',SNVS]).decode('big5').strip('\r\n')
	
# 緊急平倉(商品名稱)
def MayDay(prod):
	return subprocess.check_output([execpath+'Test_MayDay.exe',prod]).decode('big5').strip('\r\n')
	
# 取目前帳戶餘額
def FutureRights():
	return subprocess.check_output([execpath+'Test_FutureRights.exe']).decode('big5').strip('\r\n')
	
# 取帳戶下單資訊(委託單編號)
def GetAccount(SNVS):
	OrderAcc =  subprocess.check_output([execpath+'Test_GetAccount.exe',SNVS]).decode('big5').strip('\r\n').split('\n')
	OrderAcc = [i.split(',') for i in OrderAcc][0]
	return OrderAcc
	
# 取目前委託單(商品名稱)
def GetUnfinished(prod):
	OrderAcc = subprocess.check_output([execpath+'Test_GetUnfinished.exe',prod]).decode('big5').strip('\r\n').split('\n')
	OrderAcc = [i.split(',') for i in OrderAcc]
	return OrderAcc

# 取目前未平倉單(商品名稱)
def OnOpenInterest(prod):
	OrderAcc = subprocess.check_output([execpath+'Test_OnOpenInterest.exe',prod]).decode('big5').strip('\r\n').split('\n')
	OrderAcc = [i.split(',') for i in OrderAcc]
	return OrderAcc

