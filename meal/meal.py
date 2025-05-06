def main():
    actualTime = input("What time is it? ")
    convert(actualTime)
    

def convert(time):
    hours, minutes = time.split(":")
    minutes = float(minutes/60)
    convertedToFloat = (float(hours+minutes))
    return convertedToFloat


