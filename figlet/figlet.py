import sys, random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) < 2:
    f = random.choice(figlet.getFonts())
    figlet.setFont(font=f)

elif len(sys.argv) < 4 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    f = sys.argv[2]
    figlet.setFont(font=f)

else:
    sys.exit("Invalid Usage")

if f in figlet.getFonts():
    input = input("Input:" )
    print(f"Output:  {figlet.renderText(s)}")
else:
    sys.exit("Invalid Usage")






