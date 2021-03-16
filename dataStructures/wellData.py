

wellProp= {"Name" : 0, "type": 1, "Direction": 2, "Geo": 3, "WellDiameter":7,
                "WF": 8, "Skin": 9}

def typeChange(x):
    try:
        if(x.isdigit()):
            return int(x)
        else:
            return float(x)
    except:
        return x

class WellData:
    def __init__(self):
      self.name =""
      self.connections= []
      self.rateW2W= []
    def setWell(self,wellI):
        self.name= wellI[wellProp["Name"]]                   # INJ1  or PROD1
        self.type= wellI[wellProp["type"]]                   # I: injector P: (producer)
        self.Direction= wellI[wellProp["Direction"]]         # X or Y or Z
        self.geo= wellI[wellProp["Geo"]:wellProp["Geo"]+3]   # array 4. start End of well 
        self.diameterW= wellI[wellProp["WellDiameter"]]      # WELLBORE DIAMETER IN METERS  WD
        self.WF= wellI[wellProp["WF"]]                       # WELL ANGLE OPEN TO FLOW (fraction between 0 and 1)
        self.skin= wellI[wellProp["Skin"]]                   # WELLBORE SKIN
        #read from history
        # self.rate
    
    def setConnection(self,con,rate):
        self.connections= con
        self.rateW2W= rate
        # self.ratewell= sum(rate)
    #find well2 in well connections and return rate between them
    def getOneRateW2W(self,well2):
        pass
    

class WellsData:
    def __init__(self):
        self.numOfWells= -1
        self.wells=[]

    def readWells(self,input=""):
        data=self.openWellFile()

        def buildWell(lineI):
            well= WellData()
            well.setWell(lineI)
            return well
        # if(input=="readFromGRDECLFIle"):
        #     data=1
        # else:
        data=self.openWellFile()
        # print(data)
        self.wells= list(map(buildWell,data))
  
    def checkAllConnections(self,SLData):
        for well in self.wells:
            if((well.type=="I") | (well.type=="i")):
                checkConnections(well,self.wells,SLData)  

    def openWellFile(self):
        with open("well.dat", "r") as data_file:
            data=data_file.readlines()
            self.numOfWells=int(data[1])
            dataW=data[15:15+self.numOfWells]
            dataW=list(map(lambda x: x.replace("\n", ""),dataW))
            dataW=list(map(lambda x: x.split(), dataW))
            dataW=list(map(lambda x: list(map(typeChange,x)),dataW ))
            return dataW

    def getWell(self,wellName):
        # find WellName in wells
        for well in self.wells:
            if(well.name==wellName):
                return well
                break
            else:
                return "Error"

# check connection of one well with other well. if two well was connected then
# compute flux between two well
def checkConnections(well,wells,SLData):
    
    print(SLData.NumAllSL)
    well.connections.append()
    # wellp.connections.append()

    