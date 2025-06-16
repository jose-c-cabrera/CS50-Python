import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a csv file")
try:

    with open (sys.argv[1], "r") as view, open(sys.argv[2], "w") as modify:
        reader = csv.DictReader(view)
        writer = csv.DictWriter(modify, fieldnames = ["first", "last", "house"])
        writer.writeheader()

        for row in reader:
            name = row["name"].strip()
            if ',' in name:
                last, first = name.split(',',1)
                first = first.strip()
                last = last.strip()
            else:
                first = name
                last = ""

            writer.writerow({
                "first":first,
                "last":last,
                "house":row["house"].strip()
        })
except(FileNotFoundError):
    sys.exit(f"Could not read {sys.argv[1]}")

