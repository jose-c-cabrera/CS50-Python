
dates = [
    "January",
    "February",
    "March",
    "April",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

date = input("Date: ").strip()
day,month,year = date.rsplit(sep= " ")

match month:
    case "January":
        print("01")
    case "February":
        print("02")
    case "March":
        print("03")
    case "April":
        print("04")
    case "May":
        print("05")
    case "June":
        print("06")
    case "July":
        print("07")
    case "August":
        print("08")
    case "September":
        print("09")
    case "October":
        print("10")
    case "November":
        print("11")
    case "December":
        print("12")














