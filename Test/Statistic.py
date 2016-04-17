__author__ = 'panda_huang'

DataPath = "G:\\projects\\FraudDetection\\Data\\1bankdataTest.txt"
BankTransData = []
TransCardID = {}

def ReadData(path = DataPath):
    with open(path) as fopen:
        for line in fopen.readlines():
            dataline = line.strip().split('\t')

            BankTransData.append(dataline)
    pass

def ShowDataStructure():
    print(BankTransData)

def CoutNum():
    for line in BankTransData:
        if TransCardID.has_key(line[0]):
            TransCardID[line[0]] = TransCardID[line[0]] + 1
        else:
            TransCardID[line[0]] = 1
    TransCardIDNum = TransCardID.__len__()
    print("TransCardIDNum:", TransCardIDNum, TransCardID)

if __name__ == "__main__":
    ReadData()
    ShowDataStructure()
    CoutNum()
    pass