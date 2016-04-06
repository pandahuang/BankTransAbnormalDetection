__author__ = 'panda'

DataPath = "G:\\projects\\FraudDetection\\Data\\1pretest.txt"
BankTransData = []

def ReadData(path = DataPath):
    with open(path) as fopen:
        for line in fopen.readlines():
            dataline = line.strip().split('\t')
            BankTransData.append(dataline)
    pass
