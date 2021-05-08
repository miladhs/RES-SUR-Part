import re


# Data class: To be used as a data modifier tool
class _Data:

    # Datatype corrector method: To correct datas which are in string format into numerial format if needed (Static)
    @staticmethod
    def datatype_corrector(value):
        pattern_float = r"\d+\.\d+"                 # Regular expression pattern for floating point numbers
        pattern_integer = r"\d+"                    # Regular expression pattern for integer numbers
        if (re.match(pattern_float, value)):        # Checking if the data is a floating point number
            return float(value)
        elif (re.match(pattern_integer, value)):    # Checking if the data is not a floating point and is an integer number
            return int(value)
        else:                                       # Checking if the data is not a number and yet a string
            return value