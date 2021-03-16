import dataStructures.streamLineDataStruc as SLlass
import dataStructures.wellData as wellClass
import reservoirSurveillance.resSur as resClass

SLS= SLlass.StreamLinesData()
SLS.readAllSL()
print(SLS.allSLData[0].number)

WD= wellClass.WellsData()
WD.readWells()
print(WD.wells[0].name)
print(WD.getWell("INJ1").type)

# WD.checkAllConnections(SLS)

# res= resClass.ResSur(wells)



