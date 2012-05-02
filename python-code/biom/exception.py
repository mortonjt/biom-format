#!/usr/bin/env python

"""Define BIOM exceptions"""

__author__ = "Daniel McDonald"
__copyright__ = "Copyright 2012, BIOM-Format Project"
__credits__ = ["Daniel McDonald", "Jai Rideout", "Greg Caporaso", 
                       "Jose Clemente", "Justin Kuczynski"]
__license__ = "GPL"
__url__ = "http://biom-format.org"
__version__ = "0.9.3-dev"
__maintainer__ = "Daniel McDonald"
__email__ = "daniel.mcdonald@colorado.edu"
__status__ = "Release"

class BiomException(Exception):
    pass

class BiomParseException(BiomException):
    pass

class TableException(BiomException):
    pass

class UnknownID(BiomException):
    pass