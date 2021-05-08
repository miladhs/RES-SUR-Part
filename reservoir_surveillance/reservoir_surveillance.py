from math import ceil
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
#import matplotlib.font_manager as fm
#plt.rcParams['axes.linewidth'] = 2
#mpl.rcParams['font.family'] = 'Times New Roman'
#plt.rcParams['font.size'] = 10
#mpl.rcParams["figure.dpi"] = 1200
#mpl.rcParams["savefig.dpi"] = 1200


class Reservoir_Surveillance:
    
    def __init__(self):
        pass
    
    def draw_flux_pattern_map_injection_waf(self, wells_data):
        fig, ax = plt.subplots()
        wellhead_xs = []
        wellhead_ys = []
        injection_wells = wells_data.get_injection_wells()
        for injection_well in injection_wells:
            ax.scatter(injection_well.wellhead.x, injection_well.wellhead.y, marker = "s", color = "black", zorder = 1)
            wellhead_xs.append(injection_well.wellhead.x)
            wellhead_ys.append(injection_well.wellhead.y)
            for connected_well in injection_well.connected_wells:
                ax.scatter(connected_well.wellhead.x, connected_well.wellhead.y, marker = "o", color = "black", zorder = 1)
                x_points = np.linspace(injection_well.wellhead.x, connected_well.wellhead.x, num = 1000)
                y_points = np.linspace(injection_well.wellhead.y, connected_well.wellhead.y, num = 1000)
                ax.plot(x_points, y_points, linewidth = 5*connected_well.waf, zorder = 0, label = "{} - {}".format(injection_well.name, connected_well.name))
                ax.text(x_points.mean(), y_points.mean(), s = "{0:.2f}%".format(100*connected_well.waf), fontsize=8, bbox=dict(boxstyle="round", fc="white", ec="black"))
                wellhead_xs.append(connected_well.wellhead.x)
                wellhead_ys.append(connected_well.wellhead.y)
        x_ticks_major = round(abs(max(wellhead_xs)-min(wellhead_xs))/15)
        x_ticks_major += (x_ticks_major==0)
        x_ticks_minor = x_ticks_major / 2
        y_ticks_major = round(abs(max(wellhead_ys)-min(wellhead_ys))/10)
        y_ticks_major += (y_ticks_major==0)
        y_ticks_minor = y_ticks_major / 2
        ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(x_ticks_major))
        ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(x_ticks_minor))
        ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(y_ticks_major))
        ax.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(y_ticks_minor))
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.legend(frameon=False, fontsize=7)
    
    def draw_flux_pattern_map_production_waf(self, wells_data):
        fig, ax = plt.subplots()
        wellhead_xs = []
        wellhead_ys = []
        production_wells = wells_data.get_production_wells()
        for production_well in production_wells:
            ax.scatter(production_well.wellhead.x, production_well.wellhead.y, marker = "o", color = "black", zorder = 1)
            wellhead_xs.append(production_well.wellhead.x)
            wellhead_ys.append(production_well.wellhead.y)
            for connected_well in production_well.connected_wells:
                ax.scatter(connected_well.wellhead.x, connected_well.wellhead.y, marker = "s", color = "black", zorder = 1)
                x_points = np.linspace(production_well.wellhead.x, connected_well.wellhead.x, num = 1000)
                y_points = np.linspace(production_well.wellhead.y, connected_well.wellhead.y, num = 1000)
                ax.plot(x_points, y_points, linewidth = 5*connected_well.waf, zorder = 0, label = "{} - {}".format(production_well.name, connected_well.name))
                ax.text(x_points.mean(), y_points.mean(), s = "{0:.2f}%".format(100*connected_well.waf), fontsize=8, bbox=dict(boxstyle="round", fc="white", ec="black"))
                wellhead_xs.append(connected_well.wellhead.x)
                wellhead_ys.append(connected_well.wellhead.y)
        x_ticks_major = round(abs(max(wellhead_xs)-min(wellhead_xs))/15)
        x_ticks_major += (x_ticks_major==0)
        x_ticks_minor = x_ticks_major / 2
        y_ticks_major = round(abs(max(wellhead_ys)-min(wellhead_ys))/10)
        y_ticks_major += (y_ticks_major==0)
        y_ticks_minor = y_ticks_major / 2
        ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(x_ticks_major))
        ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(x_ticks_minor))
        ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(y_ticks_major))
        ax.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(y_ticks_minor))
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.legend(frameon=False, fontsize=7)