### -------------------------------------------------------------------------------------------------------------------
### helps you mass purchase wingulls on pokecord which does not violate the pokecord anti botting rules whatsoever
### -------------------------------------------------------------------------------------------------------------------

import time, sys, re
from pyautogui import press, typewrite, hotkey

#p!market search --name wingull --order price a
#$p add 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25

"""
Example input arguement
PokécordBOTToday at 10:55 PM
Pokécord Market:
Level 16 Wingull | ID: 362585589 | Price: 1 Credits
Level 16 Wingull | ID: 367224111 | Price: 1 Credits
Level 40 Wingull | ID: 367833153 | Price: 1 Credits
Level 9 Wingull | ID: 353484162 | Price: 3 Credits
Level 22 Wingull | ID: 193645436 | Price: 4 Credits
Level 4 Wingull | ID: 206872445 | Price: 5 Credits
Level 23 Wingull | ID: 208117809 | Price: 5 Credits
...
"""

arg = sys.argv[1]

m = re.findall('ID: (\d{5,10})', arg)


time.sleep(3)

for i in m:
    typewrite('p!market buy ' + i)
    press('enter')
    time.sleep(.7)
    typewrite('p!confirmbuy')
    press('enter')
    time.sleep(.7)



