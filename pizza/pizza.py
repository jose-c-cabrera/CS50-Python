import sys

if len(sys.argv) > 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a csv file")

try:
    
