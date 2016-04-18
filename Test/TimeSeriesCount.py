__author__ = 'panda_huang'

INFREQUENCYPATH = "G:\\projects\\FraudDetection\\Data\\TimeSeries\\inFrequency.csv"
OUTFREQUENCYPATH = "G:\\projects\\FraudDetection\\Data\\TimeSeries\\outFrequency.csv"
INCOMEPATH = "G:\\projects\\FraudDetection\\Data\\TimeSeries\\income.csv"

UserOne = []
UserTwo = []
UserThree = []
UserFour = []
UserFive = []
UserSix = []

def ReadData(user):
    inFreq = []
    outFreq = []
    inCome = []
    with open(INFREQUENCYPATH) as fopen1:
        inFreq = fopen1.readlines()
    with open(OUTFREQUENCYPATH) as fopen2:
        outFreq = fopen2.readlines()
    with open(INCOMEPATH) as fopen3:
        inCome = fopen3.readlines()

    UserData = GetUserData(user, inFreq, outFreq, inCome)
    return UserData
    pass

# print(len(UserOne), len(UserOne[0]), len(UserOne[1]), len(UserOne[2]))

def GetUserData(user, inList, outList, inComeList):
    allData = []
    inDatas = []
    outDatas = []
    inComes = []
    for lineIn in inList:
        inDatas.append(lineIn.strip().split(',')[user-1])
    for lineOut in outList:
        outDatas.append(lineOut.strip().split(',')[user-1])
    for lineIncome in inComeList:
        inComes.append(lineIncome.strip().split(',')[user-1])
    if len(inDatas) == len(outDatas) and len(inDatas) == len(inComes):
        print("UserID:", user)
        allData.append(inDatas)
        print("len(inDatas):", len(inDatas))
        allData.append(outDatas)
        print("len(outDatas):", len(outDatas))
        allData.append(inComes)
        print("len(inComes):", len(inComes))
    else:
        print("Error:length of datalist is not same! UserID is :", user)
        print("len(inDatas):", len(inDatas))
        print("len(outDatas):", len(outDatas))
        print("len(inComes):", len(inComes))
    return allData
    pass

UserOnePeaks = [(90, 120), (210, 240), (325, 355)]
UserTwoPeaks = [(30, 42), (135, 150)]
UserThreePeaks = [(115, 140), (235, 260), (349, 372)]
UserFourPeaks = [(362, 374)]
UserFivePeaks = [(362, 374)]
UserSixPeaks = [(160, 190), (273, 303)]

def FindPeaks(user):
    pass

def CountPeakProperties(user, UserData, UserPeaks):
    print("UserID:", user, "PeakAmount:", len(UserPeaks))
    for peak in UserPeaks:
        PeakInFreq = []
        PeakOutFreq = []
        PeakFreqDifs = []
        PeakInComes = []
        startPeak, endPeak = peak
        for pos in range(startPeak-1, endPeak):
            PeakInFreq.append(int(UserData[0][pos]))
            PeakOutFreq.append(int(UserData[1][pos]))
            PeakFreqDifs.append(int(UserData[1][pos]) - int(UserData[0][pos]))
            PeakInComes.append(float(UserData[2][pos]))
        print(("-------------------------------------------------------"))
        print(startPeak, endPeak)
        print("MaxPeakInFreq:", max(PeakInFreq))
        print("MaxPeakOutFreq:", max(PeakOutFreq))
        print("PeakFreqDifs:", PeakFreqDifs)
        print("PeakInComes:", PeakInComes)
        print("MaxPeakFreqDifs:", max(PeakFreqDifs))
        print("MinPeakFreqDifs:", min(PeakFreqDifs))
        print("AvgPeakFreqDifs:", sum(PeakFreqDifs)/len(PeakFreqDifs))
        print("TotalPeakInComes:", sum(PeakInComes))
        print("MaxPeakInComes:", max(PeakInComes))
        print("MinPeakInComes:", min(PeakInComes))
        print("AvgPeakInComes:", sum(PeakInComes)/len(PeakInComes))
    print("=====================================================================")
    pass

if __name__=="__main__":
    UserOne = ReadData(1)
    UserTwo = ReadData(2)
    UserThree = ReadData(3)
    UserFour = ReadData(4)
    UserFive = ReadData(5)
    UserSix = ReadData(6)
    CountPeakProperties(1, UserOne, UserOnePeaks)
    CountPeakProperties(2, UserTwo, UserTwoPeaks)
    CountPeakProperties(3, UserThree, UserThreePeaks)
    CountPeakProperties(4, UserFour, UserFourPeaks)
    CountPeakProperties(5, UserFive, UserFivePeaks)
    CountPeakProperties(6, UserSix, UserSixPeaks)
    pass