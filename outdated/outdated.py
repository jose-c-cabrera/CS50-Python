
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").strip()

    try:
        if "/" in date:
            m, d, y = date.split("/")
            m, d = int(m), int(d)

        else:
            if "," not in date:
                raise ValueError("Missing comma")

            month_name, d, y = date.replace(",", "").split()
            m = months.index(month_name) + 1
            d = int(d)

        if 1 <= m <= 12 and 1 <= d <= 31:
            print(f"{int(y):04}-{m:02}-{d:02}")
            break

    except (ValueError, IndexError):
        continue














