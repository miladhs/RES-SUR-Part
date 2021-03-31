

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
      self.connections= {}
      self.rateW2W= []
      self.connectionsAndRateW2W={}
      self.totalRate=0
    def setWell(self,wellI):
        self.name= wellI[wellProp["Name"]]                   # INJ1  or PROD1
        self.type= wellI[wellProp["type"]]                   # I: injector P: (producer)
        self.Direction= wellI[wellProp["Direction"]]         # X or Y or Z
        self.geo= wellI[wellProp["Geo"]:wellProp["Geo"]+4]   # array 4. start End of well 
        self.diameterW= wellI[wellProp["WellDiameter"]]      # WELLBORE DIAMETER IN METERS  WD
        self.WF= wellI[wellProp["WF"]]                       # WELL ANGLE OPEN TO FLOW (fraction between 0 and 1)
        self.skin= wellI[wellProp["Skin"]]                   # WELLBORE SKIN
        #read from history
    
    def setConnection(self,con,rate):
        self.connections= con
        self.rateW2W= rate
        # self.connectionsAndRatW2W={}
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
  
    # def checkAllConnections(self,SLData):
    #     for well in self.wells:
    #         if((well.type=="I") | (well.type=="i")):
    #             checkConnections(well,self.wells,SLData)

    def checkAllConnections(self,SLData):
        for sl in SLData.allSLData:
            # if self.getWell(sl.startWellName).connections.has_key(sl.endWellName):
            stratWell=self.getWell(sl.startWellName)
            endWell=self.getWell(sl.endWellName)
            # if stratWell.connectionsAndRateW2W.has_key(sl.endWellName):
            if sl.endWellName in stratWell.connectionsAndRateW2W:
                stratWell.connectionsAndRateW2W[sl.endWellName]+=sl.rate
                endWell.connectionsAndRateW2W[sl.startWellName]+=sl.rate
            else:
                stratWell.connectionsAndRateW2W[sl.endWellName]=sl.rate
                endWell.connectionsAndRateW2W[sl.startWellName]=sl.rate
    def setTotalRate(self):
        if not bool(self.wells[0].connectionsAndRateW2W):
            print("error: well connection not checked. first most be check wellConnection")
        else:
            for well in self.wells:
                rateValues=well.connectionsAndRateW2W.values()
                well.totalRate= sum(rateValues)


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
        return "Error"


    