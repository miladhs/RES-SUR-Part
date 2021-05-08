import matplotlib as mpl
from matplotlib import pyplot as plt
import matplotlib.font_manager as fm
#plt.rcParams['axes.linewidth'] = 2
#mpl.rcParams['font.family'] = 'Times New Roman'
#plt.rcParams['font.size'] = 10
#mpl.rcParams["figure.dpi"] = 1200
#mpl.rcParams["savefig.dpi"] = 1200

import data_structures.streamline_data_structures as sds
import data_structures.well_data_structures as wds
import reservoir_surveillance.reservoir_surveillance as rs

wells_data_guide = {"NAME": 0, "TYPE": 1, "DIRECTION": 2, "LOCS": 3, "DIAMETER": 7, "SKIN": 9}
streamlines_data_guide = {"SlNumber": 0, "TOF": 1, "StartWellName": 2, "StartBlockNumber": 3, "EndWellName":7, "EndBlockNumber": 8, "Flux": 12}
wells_data = wds.Wells_Data()
wells_data.load_wells_data("Wells-Data.dat", wells_data_guide)

streamlines_data = sds.Streamlines_Data()
streamlines_data.load_streamlines_data("Streamlines-Data.dat", wells_data, streamlines_data_guide)

print(wells_data.wells)

print(wells_data.wells[0].connected_wells)

reservoir_surveillance = rs.Reservoir_Surveillance()

#plt.tight_layout()

reservoir_surveillance.draw_flux_pattern_map_injection_waf(wells_data)
plt.show()

reservoir_surveillance.draw_flux_pattern_map_production_waf(wells_data)
plt.show()