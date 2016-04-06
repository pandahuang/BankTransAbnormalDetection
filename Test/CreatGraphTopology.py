__author__ = 'panda_huang'

DataPath = "G:\\projects\\FraudDetection\\Data\\1pretest.txt"
GraphFilePath = "G:\\projects\\FraudDetection\\Data\\GraphFile.txt"
BankTransData = []

def ReadData(path = DataPath):
    with open(path) as fopen:
        for line in fopen.readlines():
            dataline = line.strip().split('\t')
            BankTransData.append(dataline)
    pass

def CreatGraph(path = GraphFilePath):
    GraphLines = {}
    for data in BankTransData:
        edge = data[1] + "\t" + data[2]
        if GraphLines.has_key(data[0]):
            edge = GraphLines[data[0]] + "," + data[1] + "\t" + data[2]
            GraphLines[data[0]] = edge
        else:
            edge = data[1] + " " + data[2]
            GraphLines[data[0]] = edge

    CentreNodeNum = len(GraphLines)
    with open(path, 'w') as fopen:
        for k, v in GraphLines.iteritems():
            fopen.write(k + '\n')
            edges = v.strip().split(',')
            for edge in edges:
                fopen.write(edge + '\n')

    print(GraphLines, CentreNodeNum)
    pass

if __name__=="__main__":
    ReadData()
    CreatGraph()
    pass