import dataStructures.streamLineDataStruc as SLClass
import dataStructures.wellData as wellClass
import reservoirSurveillance.resSur as resClass
# from dataStructures.streamLineDataStruc import *
# from dataStructures.wellData import *
# from reservoirSurveillance.resSur import *

SLS= SLClass.StreamLinesData()
SLS.readAllSL()
print(SLS.allSLData[0].number)

WD= wellClass.WellsData()
WD.readWells()
print(WD.wells[0].name)
print(WD.getWell("INJ1").type)

print("ALL WELLS ========================================================")
for onewd in WD.wells:
    print(onewd.name)

print("connections ======================================================")
WD.checkAllConnections(SLS)
WD.setTotalRate()
# print(WD.getWell("INJ1").name)
# print(WD.getWell("PROD4").name)
WAF1=WD.wells[0].connectionsAndRateW2W["PROD1"]/WD.wells[0].totalRate
WAF2=WD.wells[0].connectionsAndRateW2W["PROD2"]/WD.wells[0].totalRate
WAF3=WD.wells[0].connectionsAndRateW2W["PROD3"]/WD.wells[0].totalRate
WAF4=WD.wells[0].connectionsAndRateW2W["PROD4"]/WD.wells[0].totalRate



print(WAF1)
print(WAF2)
print(WAF3)
print(WAF4)
print(WAF1+WAF2+WAF3+WAF4)


## X=geo[0]  and Y=geo[1]
print(WD.wells[0].geo)
print(WD.wells[0].diameterW)

# res= resClass.ResSur(wells)



