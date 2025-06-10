import sys


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

line_count = 0
try:
    with open(sys.argv[1], "r") as file:
        for line in file:
            if line.strip() and not line.startswith("#"):
                line_count +=1
except FileNotFoundError:
    sys.exit("File does not exist")

print(line_count)








