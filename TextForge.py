import sys
from pyfiglet import Figlet
import random

def RandText(s):
    figlet = Figlet()
    lst1=figlet.getFonts()
    rndFont=random.choice(lst1)
    figlet.setFont(font=rndFont)
    return figlet.renderText(s)
        
if len(sys.argv)==1:
    str1=input("Input: ")
    str1=RandText(str1)
    print(f"{str1}")

elif len(sys.argv)==3 and (sys.argv[1]=="-f" or sys.argv[1]=="--font"):
    str1=input("Input: ")
    figlet = Figlet()
    font1=sys.argv[2]
    figlet.setFont(font=font1)
    print(figlet.renderText(str1))

else:
    sys.exit("Invalid usage")




    


