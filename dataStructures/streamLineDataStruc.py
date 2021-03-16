
FloodDataProp= {"Number" : 0, "TOf": 1, "StartWellName": 2, "StartBlockNumber": 3, "G0":4,
                "EndWellName": 7, "EndBlockNumber": 8, "G1": 9 , "Flux":12}

def typeChange(x):
    try:
        if(x.isdigit()):
            return int(x)
        else:
            return float(x)
    except:
        return x

class StreamLineData:
   def __init__(self):
       self.number=-1
   def setSL(self,lineI):
       self.startWellName= lineI[FloodDataProp["StartWellName"]]    #or head
    #    self.startWellNum
    #    self.startPos= lineI[FloodDataProp["G0"]:FloodDataProp["G0"]+2]
    #    self.startBlock= lineI[FloodDataProp["StartBlockNumber"]]
    #    self.startLayer= lineI[FloodDataProp["startLayer"]]

       self.endWellName= lineI[FloodDataProp["EndWellName"]]          #or tail
    #    self.endWellNum
    #    self.endPos= lineI[FloodDataProp["G1"]:FloodDataProp["G1"]+2]
    #    self.endBlock= lineI[FloodDataProp["EndBlockNumber"]]
    #    self.endLayer= lineI[FloodDataProp["endLayer"]]

       self.number= lineI[FloodDataProp["Number"]]
       self.rate= lineI[FloodDataProp["Flux"]]
    #    self.TOF= lineI[FloodDataProp["Number"]]

   def setSLNodesPos(self,poss):
       self.numeNodeInSL
       self.slNodePos = []


class StreamLinesData:
    def __init__(self):
        self.NumAllSL=0
        self.allSLData= []
        # self.oneSL= StreamLineData()
        
    def readAllSL(self,input=""):
        self.NumAllSL= 346
        data=self.openFloodEffMapData()
        print(data[345])

        def buildSL(lineI):
            oneSL= StreamLineData()
            oneSL.setSL(lineI)
            return oneSL

        self.allSLData = list(map(buildSL,data))
    
    def readAllSLNodesPos(self,input=""):
        self.NumAllSL=1
        self.allSLData= []    #array of streamLineData slnodes part  #elf.allSlNodesPos =[]

    def openFloodEffMapData(self):
        with open("FloodEffMapData.out", "r") as data_file:
            data=data_file.readlines()[3:self.NumAllSL+3]
            data=list(map(lambda x: x.replace("\n", ""),data))
            data=list(map(lambda x: x.split(), data))
            data=list(map(lambda x: list(map(typeChange,x)),data ))
            # print(data[0])
            return data
    
    def openSLPos(self):
        with open("SL 1.plt", "r") as data_file:
            data=data_file.readlines()[3:1000]
        



