import random
from pyfiglet import Figlet


figlet = Figlet()

figlet.getFonts()

figlet.setFont(font = font.random)

input = input("Input:" )
print(f"Output:  {figlet.renderText(input)}")


