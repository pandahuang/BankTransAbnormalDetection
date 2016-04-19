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
UserSeven = []
UserEight = []
UserNine = []
UserTen = []
UserEleven = []
UserTwelve = []
UserThirteen = []
UserFourteen = []
UserFifteen = []
UserSixteen = []
UserSeventeen = []
UserEighteen = []
UserNineteen = []
UserTwenty = []
UserTwentyOne = []
UserTwentyTwo = []
UserTwentyThree = []

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
        # print("UserID:", user)
        allData.append(inDatas)
        # print("len(inDatas):", len(inDatas))
        allData.append(outDatas)
        # print("len(outDatas):", len(outDatas))
        allData.append(inComes)
        # print("len(inComes):", len(inComes))
    else:
        print("Error:length of datalist is not same! UserID is :", user)
        # print("len(inDatas):", len(inDatas))
        # print("len(outDatas):", len(outDatas))
        # print("len(inComes):", len(inComes))
    return allData
    pass


UserOnePeaks = [(94, 114), (209, 235), (324, 349)]
UserTwoPeaks = [(31, 40), (139, 149)]
UserThreePeaks = [(113, 139), (235, 260), (350, 372)]
UserFourPeaks = [(366, 372)]
UserFivePeaks = [(366, 372)]
UserSixPeaks = [(163, 190), (278, 299)]
UserSevenPeaks = [(40, 63), (163, 209), (278, 307)]
UserEightPeaks = [(65, 92), (188, 210)]
UserNinePeaks = [(40, 64), (163, 190), (278, 300)]
UserTenPeaks = [(234, 259)]
UserElevenPeaks = [(63, 92), (188, 209), (299, 324)]
UserTwelvePeaks = [(366, 372)]
UserThirteenPeaks = [(92, 113), (209, 235), (324, 349)]
UserFourteenPeaks = [(63, 92), (177, 211), (291, 324)]
UserFifteenPeaks = [(209, 234)]
UserSixteenPeaks = [(136, 163), (253, 278), (363, 389)]
UserSeventeenPeaks = [(163, 189), (273, 300)]
UserEighteenPeaks = [(188, 210), (299, 324)]
UserNineteenPeaks = [(63, 92), (188, 210), (299, 372)]
UserTwentyPeaks = [(209, 234), (324, 349)]
UserTwentyOnePeaks = [(259, 278), (372, 389)]
UserTwentyTwoPeaks = [(372, 389)]
UserTwentyThreePeaks = [(63, 93), (188, 212), (299, 324)]

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
    UserSeven = ReadData(7)
    UserEight = ReadData(8)
    UserNine = ReadData(9)
    UserTen = ReadData(10)
    UserEleven = ReadData(11)
    UserTwelve = ReadData(12)
    UserThirteen = ReadData(13)
    UserFourteen = ReadData(14)
    UserFifteen = ReadData(15)
    UserSixteen = ReadData(16)
    UserSeventeen = ReadData(17)
    UserEighteen = ReadData(18)
    UserNineteen = ReadData(19)
    UserTwenty = ReadData(20)
    UserTwentyOne = ReadData(21)
    UserTwentyTwo = ReadData(22)
    UserTwentyThree = ReadData(23)

    CountPeakProperties(1, UserOne, UserOnePeaks)
    CountPeakProperties(2, UserTwo, UserTwoPeaks)
    CountPeakProperties(3, UserThree, UserThreePeaks)
    CountPeakProperties(4, UserFour, UserFourPeaks)
    CountPeakProperties(5, UserFive, UserFivePeaks)
    CountPeakProperties(6, UserSix, UserSixPeaks)
    CountPeakProperties(7, UserSeven, UserSevenPeaks)
    CountPeakProperties(8, UserEight, UserEightPeaks)
    CountPeakProperties(9, UserNine, UserNinePeaks)
    CountPeakProperties(10, UserTen, UserTenPeaks)
    CountPeakProperties(11, UserEleven, UserElevenPeaks)
    CountPeakProperties(12, UserTwelve, UserTwelvePeaks)
    CountPeakProperties(13, UserThirteen, UserThirteenPeaks)
    CountPeakProperties(14, UserFourteen, UserFourteenPeaks)
    CountPeakProperties(15, UserFifteen, UserFifteenPeaks)
    CountPeakProperties(16, UserSixteen, UserSixteenPeaks)
    CountPeakProperties(17, UserSeventeen, UserSeventeenPeaks)
    CountPeakProperties(18, UserEighteen, UserEighteenPeaks)
    CountPeakProperties(19, UserNineteen, UserNineteenPeaks)
    CountPeakProperties(20, UserTwenty, UserTwentyPeaks)
    CountPeakProperties(21, UserTwentyOne, UserTwentyOnePeaks)
    CountPeakProperties(22, UserTwentyTwo, UserTwentyTwoPeaks)
    CountPeakProperties(23, UserTwentyThree, UserTwentyThreePeaks)
    pass