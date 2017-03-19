# this is a good module to use when working with directories
import os

# just an example of creating directories
if not "sampleDirectory" in os.listdir("."):
    os.mkdir("sampleDirectory")