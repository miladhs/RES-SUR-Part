from .common_data_structures import _Data


# Well connection class: To define and use well connection to a well (Private)
class _Well_Connection:

    # Constructor method: To build and define well connection objects
    def __init__(self, well, rate):
        self.name = well.name    # Name of the connected well
        self.wellhead = well.wellhead
        self.rate = rate    # rate of the connected well
        self.waf = 0.0      # Well allocation factor of the connected well
    
    def __stringformatter(self):
        return "{0}: ({1:.4f}, {2:.2f}%)".format(self.name, self.rate, 100*self.waf) 

    # String and Representation dunder methods: To make a better text based representations of a well connection object
    def __str__(self):
        return self.__stringformatter()    # String method to be used in printing well objects
    def __repr__(self):
        return self.__stringformatter()    # Representation method to be used in showing well objects in console


# Streamline class: To define and use streamlines (Public)
class Streamline:
    
    # Constructor method: To build and define streamline objects
    def __init__(self, number, time_of_flight, start_block, end_block, flux):
        self.number = number                    # Number of the streamline
        self.time_of_flight = time_of_flight    # Time of flight of the streamline
        self.start_block = start_block          # Start block number of the streamline
        self.end_block = end_block              # End block number of the streamline
        self.flux = flux                        # Flux of the streamline (!!! This should be changed to support multiphase flow)


# Streamlines data class: To define and use a dataset for streamlines (Public)
class Streamlines_Data:
    
    # Constructor method: To build and define streamlines data object
    def __init__(self):
        self.num_streamlines = 0    # Number of streamlines in the streamlines data
        self.streamlines = []       # List of the wells which are in the wells data
    
    # Interpret streamlines data line method: To interpret each line in the streamlines data file
    def __interpret_streamlines_data_line(self, line):
        return list(map(_Data.datatype_corrector, line.replace("\n", "").split()))
    
    # time dependency
    def load_streamlines_data(self, file, wells_data, guide):
        with open(file, "r") as data_file:                                                      # Reading streamlines data file
            data = data_file.readlines()[3:]
        self.num_streamlines = len(data)                                                        # Obtaining number of streamlines from the length of the 
        for line in data:
            data_line = self.__interpret_streamlines_data_line(line)
            number = data_line[guide["SlNumber"]]                                               # Number of the streamline
            time_of_flight = data_line[guide["TOF"]]                                            # Time of flight of the streamline
            injector_well = wells_data.get_well(data_line[guide["StartWellName"]])              # Injection well of the streamline
            start_block = data_line[guide["StartBlockNumber"]]                                  # Starting block of the streamline
            producer_well = wells_data.get_well(data_line[guide["EndWellName"]])                # Producer well of the streamline
            end_block = data_line[guide["EndBlockNumber"]]                                      # Ending block of the streamline
            flux = data_line[guide["Flux"]]                                                     # Flux of the streamline
            streamline = Streamline(number, time_of_flight, start_block, end_block, flux)       # Creating the streamline object from its attributes
            self.streamlines.append(streamline)                                                 # Adding well to the streamlines list of the streamlines data
            if (injector_well.get_connected_well(producer_well.name) == None):                  # Creating/Updating well to well connection rates for the injection and production wells
                injector_well.add_connected_well(_Well_Connection(producer_well, flux))
                producer_well.add_connected_well(_Well_Connection(injector_well, flux))
            else:
                injector_well.get_connected_well(producer_well.name).rate += flux
                producer_well.get_connected_well(injector_well.name).rate += flux
        wells_data.compute_wells_rates()                                                        # Computing well rates based on the connectivity data
        wells_data.compute_wells_wafs()                                                         # Computing well allocation factors based on the connectivity data and well rate