import datetime
import sys
import re
import inflect


def main():

    date = input("Date of Birth: ")
    print(transform(date))



def transform(date):

    #Regex pattern to check for valid input having a convenction of "YYYY-MM-DD"
    date_pattern = r'\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])'
    matches = re.findall(date_pattern, date)


    if matches:
        p = inflect.engine()
        date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        time_since = datetime.date.today() - date
        time_since = int(time_since.total_seconds() / 60)
        #Making sure they didn't place the date of birth in the future from today
        if time_since < 0:
            sys.exit("Invalid date")
        else:
            word = p.number_to_words(time_since)
            word = word.replace("and", "")
            word = word.replace("  ", " ")
            word = word.replace("thous", "thousand")
            word = word.capitalize()
            return word + " minutes"
    else:
        sys.exit("Invalid date")



if __name__ == "__main__":
    main()
