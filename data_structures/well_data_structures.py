from .common_data_structures import _Data


# Wellhead class: To define and use well head for wells (Private)
class _Wellhead:

    # Constructor method: To build and define wellhead objects
    def __init__(self, x, y, z):
        self.x = x    # Location of the wellhead in the x direction
        self.y = y    # Location of the wellhead in the y direction
        self.z = z    # Location of the wellhead in the z direction


# Well class: To define and use wells (Public)
class Well:
    
    # Constructor method: To build and define well objects
    def __init__(self, name, kind, direction, iloc, jloc, kloc, diameter, skin):
        self.name = name                                        # Name of the well
        self.kind = kind                                        # Kind of the well (I/P) I: Injection, P: Production 
        self.direction = direction                              # Direction of the well (X/Y/Z) X: X-direction, Y: Y-direction, Z: Z-direction
        self.blocks_x = iloc                                    # Number of grid block in x-direction for well
        self.blocks_y = jloc                                    # Number of grid block in y-direction for well
        self.blocks_z = kloc                                    # Number of grid block in z-direction for well
        self.wellhead = _Wellhead(iloc[0], jloc[0], kloc[0])    # Wellhead of the well 
        self.diameter = diameter                                # Diameter of the well
        self.skin = skin                                        # Skin factor of the well
        self.rate = 0.0                                         # Total flow rate of the well
        self.connected_wells = []                               # Name of the wells which connect the current well and their coresponding flow rates
    
    # Get connected well method: To get a connected well by name
    def get_connected_well(self, name, indexer = False):
        if (indexer):                                                        # Checking if the index of the well is wanted alongside with the well
            for index, connected_well in enumerate(self.connected_wells):
                if (connected_well.name == name):
                    return (index, connected_well)
            return None, None
        else:
            for connected_well in self.connected_wells:
                if (connected_well.name == name):
                    return connected_well
            return None
    
    # Add connected well method: To add a connected well to the connected wells of the well
    def add_connected_well(self, connected_well):
        index, _ = self.get_connected_well(connected_well.name, indexer = True)
        if (index == None):                                                        # Checking if the well is not repetative
            self.connected_wells.append(connected_well)
    
    # Compute well rate method: To compute well rate based on the connected wells
    def compute_well_rate(self):
        self.rate = 0.0
        for connected_well in self.connected_wells:
            self.rate += connected_well.rate
    
    # Compute well waf method: To compute well waf for the connected wells
    def compute_well_wafs(self):
        for connected_well in self.connected_wells:
            connected_well.waf = connected_well.rate/self.rate
    
    def __stringformatter(self):
        return "{}: ({})".format(self.name, self.kind)
    
    # String and Representation dunder methods: To make a better text based representations of a well object
    def __str__(self):
        return self.__stringformatter()    # String method to be used in printing well objects
    def __repr__(self):
        return self.__stringformatter()    # Representation method to be used in showing well objects in console


# Wells data class: To define and use a dataset for wells (Public)
class Wells_Data:
    
    # Constructor method: To build and define wells data object
    def __init__(self):
        self.num_wells = 0    # Number of the wells in the wells data
        self.wells = []       # List of the wells which are in the wells data
    
    # Interpret wells data line method: To interpret each line in the wells data file
    def __interpret_wells_data_line(self, line):
        return list(map(_Data.datatype_corrector, line.replace("\n", "").split()))
    
    # Load wells data method: To load well dataset using a guide dictionary
    def load_wells_data(self, file, guide):
        with open(file, "r") as data_file:                                             # Reading wells data file and removing comment lines (start with * character)
            data = list(filter(lambda line: line[0] != "*", data_file.readlines()))
        self.num_wells = int(data[0])                                                  # Obtaining number of wells from the first line of the wells data file
        for line in data[1:]:
            data_line = self.__interpret_wells_data_line(line)                         # Converting datas in each of the lines in the data file
            name = data_line[guide["NAME"]]                                            # Name of the well
            kind = data_line[guide["TYPE"]]                                            # Kind of the well
            direction = data_line[guide["DIRECTION"]]                                  # Direction of the well
            locs = data_line[guide["LOCS"]: guide["LOCS"]+4]                           # i_min, i_max, j_min, j_max, k_min, k_max values for the well
            if (direction == "X"):                                                     # Checking if the well is in the X-direction
                iloc = locs[0], locs[1]
                jloc = locs[2], locs[2]
                kloc = locs[3], locs[3]
            elif (direction == "Y"):                                                   # Checking if the well is in the Y-direction
                iloc = locs[0], locs[0]
                jloc = locs[1], locs[2]
                kloc = locs[3], locs[3]
            elif (direction == "Z"):                                                   # Checking if the well is in the Z-direction
                iloc = locs[0], locs[0]
                jloc = locs[1], locs[1]
                kloc = locs[2], locs[3]
            diameter = data_line[guide["DIAMETER"]]                                    # Diameter of the well
            skin = data_line[guide["SKIN"]]                                            # Skin factor of the well
            well = Well(name, kind, direction, iloc, jloc, kloc, diameter, skin)       # Creating the well object from its attributes
            self.wells.append(well)                                                    # Adding well to the wells list of the wells data
    
    # Get well method: To obtain a well with a specific name from wells data
    def get_well(self, name, indexer = False):
        if (indexer):
            for index, well in enumerate(self.wells):
                if (well.name == name):
                    return (index, well)
            return None, None
        else:
            for well in self.wells:
                if (well.name == name):
                    return well
            return None
    
    # Get injection wells method: To obtain a list of injection wells from wells data
    def get_injection_wells(self):
        searched_list =  list(filter(lambda well: well.kind == "I", self.wells))
        if (len(searched_list) > 0):
            return searched_list
        else:
            return None
    
    # Get production wells method: To obtain a list of production wells from wells data
    def get_production_wells(self):
        searched_list = list(filter(lambda well: well.kind == "P", self.wells))
        if (len(searched_list) > 0):
            return searched_list
        else:
            return None
    
    # Add well method: To add a well to the wells data
    def add_well(self, well):
        if (self.get_well(well.name) == None):    # Checking if the well is not in the wells data
            self.wells.append(well)
    
    # Remove well method: To remove a well from the wells data
    def remove_well(self, name):
        index, well = self.get_well(name, indexer = True)
        if (index != None):              # Checking if the well is in the wells data
            _ = self.wells.pop(index)
    
    # Update well method: To update a well in the wells data
    def update_well(self, well):
        if (self.get_well(well.name) != None):    # Checking if the well is in the wells data
            self.wells[index] = well
    
    # Compute wells rates method: To compute all wells rates
    def compute_wells_rates(self):
        for well in self.wells:
            well.compute_well_rate()
    
    # Compute well wafs method: To compute all wells well allocation factors
    def compute_wells_wafs(self):
        for well in self.wells:
            well.compute_well_wafs()