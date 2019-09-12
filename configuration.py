#!/usr/bin/env python

"""Contains extractor configuration information
"""

# Setup the name of our extractor.
EXTRACTOR_NAME = "droner"

# Name of scientific method for this extractor. Leave commented out if it's unknown
#METHOD_NAME = ""

# The version number of the extractor
VERSION = "1.0"

# The extractor description
DESCRIPTION = "Extracts greenness or other RGB indices from digital images"

# The name of the author of the extractor
AUTHOR_NAME = "Clairessa Brown"

# The email of the author of the extractor
AUTHOR_EMAIL = "clairessabrown@email.arizona.edu"

# Reposity URI
REPOSITORY = "github.com/cmbrown89/drone-extractor2"

# Output variable identifiers. Use a comma separated list if more than one value is returned.
# For example, "variable 1,variable 2" identifies the two variables returned by the extractor.
# If only one name is specified, no comma's are used.
# Note that variable names cannot have comma's in them: use a different separator instead. Also,
# all white space is kept intact; don't add any extra whitespace since it may cause name comparisons
# to fail
VARIABLE_NAMES = "veg_ind,exg,per_green"
