# 匯入模組
import tailer

# MicroPlay資料存檔路徑
DataPath = 'C:/MicroPlay_SaveFile/'

# 持續取得成交資訊
def GetMatch(prod,date):
    for data in tailer.follow(open(DataPath + prod + '/' + date + '_Match.txt'),0):
        yield data.split(',')

# 持續取得委託資訊
def GetCommission(prod,date):
    for data in tailer.follow(open(DataPath + prod + '/'  + date + '_Commission.txt'),0):
        yield data.split(',')

# 持續取得上下五檔價資訊
def GetUpDn5(prod,date):
    for data in tailer.follow(open(DataPath + prod + '/'  + date + '_UpDn5.txt'),0):
        yield data.split(',')

# 取得最新一筆成交資訊
def GetLastMatch(prod,date):
    return tailer.tail(open(DataPath + prod + '/'  + date + '_Match.txt'),3)[-2].split(",")

# 取得最新一筆委託資訊
def GetLastCommission(prod,date):
    return tailer.tail(open(DataPath + prod + '/'  + date + '_Commission.txt'),3)[-2].split(",")

# 取得最新一筆上下五檔價資訊
def GetLastUpDn5(prod,date):
    return tailer.tail(open(DataPath + prod + '/'  + date + '_UpDn5.txt'),3)[-2].split(",")