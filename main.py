from ConfigBundle import *
from Config import *
from FileManager import FileManager
import sys
import getopt

###
# BEOLD THE WORLD'S MOST AWFUL, INEFFICIENT AND PAINFUL PYTHON CODE \0/
# MAY THE LORD FORGIVE US FOR OUR SINS
# 
# "I did what I had to do to just get to sleep" - Amy
###


if __name__ == '__main__':

    arg_help = "config combiner thingi: -i filename.ini -o newfilename.ini"
    inputfile = ""
    outputfile = ""
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:u:o:", ["help", "input=", 
        "user=", "output="])
    except:
        print("(invalid input)" + arg_help)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(arg_help)  # print the help message
            sys.exit(2)
        elif opt in ("-i", "--input"):
            inputfile = arg
            print(arg)
        elif opt in ("-o", "--output"):
            outputfile = arg

    if outputfile == "": 
        outputfile = "new " + inputfile

    if(inputfile == ""):
        print("Error, no inputfile provided.")
        print(arg_help)
        sys.exit(2)

    bundle = ConfigBundle(inputfile)

    for category in bundle.configs:
        bundle = bundle.merge(category)

    bundle.write(outputfile)
    print("Finished!")