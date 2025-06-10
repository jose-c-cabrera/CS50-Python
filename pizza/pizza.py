import sys
import csv
import tabulate

if len(sys.argv) > 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a csv file")

try:
    with open (sys.argv[1], "r") as csvfile:
        for line in csvfile:
            print(tabulate(table, headers="firstrow"))


