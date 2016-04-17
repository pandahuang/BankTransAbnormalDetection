__author__ = 'panda_huang'

INFREQUENCYPATH = "G:\\projects\\FraudDetection\\Data\\TimeSeries\\inFrequency.csv"
OUTFREQUENCYPATH = "G:\\projects\\FraudDetection\\Data\\TimeSeries\\outFrequency.csv"
INCOMEPATH = "G:\\projects\\FraudDetection\\Data\\TimeSeries\\income.csv"

UserOne = {}
UserTwo = {}
UserThree = {}
UserFour = {}
UserFive = {}
UserSix = {}

def ReadData():
    inFreq = []
    outFreq = []
    inCome = []
    with open(INFREQUENCYPATH) as fopen1:
        inFreq = fopen1.readlines()
    with open(OUTFREQUENCYPATH) as fopen2:
        outFreq = fopen2.readlines()
    with open(INCOMEPATH) as fopen3:
        inCome = fopen3.readlines()

    pass

def GetUserData(inList, outList, inComeList):
    for line in inList:
        inDatas = line
    pass