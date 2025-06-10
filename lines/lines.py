import sys


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

line_count = 0

with open(sys.argv[1], "r") as file:
    for line in file:
        if line.strip():
            line_count +=1






