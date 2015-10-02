import sys
import argparse

p = argparse.ArgumentParser(description="This example script work to generate the list of argument")
p.add_argument("-s", dest="stop script when error show up")
p.add_argument("-r", dest="repeat test")
p.add_argument("-l", dest="export log to /tmp")

args = p.parse_args()

if args.infile == None and args.string == None:
    print "Must be given either a string or a file"
    sys.exit(1)
if args.infile != None and args.string != None:
    print "Must be given either a string or a file, not both"
    sys.exit(1)
if args.infile:
    pass
if args.string:
    pass