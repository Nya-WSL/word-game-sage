from slowprint import slowprint_1, slowprint_text, slowprint_title
from end_page import EndPage
from page1 import Page1
from page2 import Page2
from page3 import Page3
import time
import os

#开始游戏
print('''
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                     小生物旅行记                    ┃
┃                                            v1.0.5  ┃
┠────────────────────────────────────────────────────┨
┃               Screenwriter：桑吉Sage               ┃
┃                                                    ┃
┃   Copyright © Nya-WSL 2022. All rights reserved.   ┃
┃   https://nya-wsl.com/6723413/game/Sage_Travels    ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
''')
print("按回车开始游戏")
input()
os.system("cls")

slowprint_title("""  
 __                _     _    
|_  o  __ _ _|_   |_) _ (_| _ 
|   |  | _>  |_   |  (_|__|(/_""")
time.sleep(5)
os.system("cls")
print("按回车开始游戏")
input()
os.system("cls")

slowprint_text("""很久很久以前，有一只谜之小生物。
为了躲避调查员的追杀，小生物使用了由好心的外星猫猫提供的修女身体。
可是，此时的小生物并不理解人类这一物种。
为了更好藏匿在人类社会之中，小生物开始了对人类的调查。""")

os.system("cls")
time.sleep(1.5)
slowprint_1("......")
time.sleep(1.5)
os.system("cls")

def choose_main():
    global choose1
    print("去哪里调查人类？")
    print()
    time.sleep(0.5)
    print("1. 机场[")
    print("2. 公司")
    print("3. 菜市场")
    print()
    time.sleep(1)
    global choose1
    choose1 = int(input("你的选择是："))

choose_main()

if choose1 == 1:
    Page1()
    choose_main()
    if choose1 == 2:
        Page2()
        choose_main()
        if choose1 == 3:
            Page3()
    elif choose1 == 3:
        Page3()
        choose_main()
        if choose1 == 2:
            Page2()
elif choose1 == 2:
    Page2()
    choose_main()
    if choose1 == 1:
        Page1()
        choose_main()
        if choose1 == 3:
            Page3()
    elif choose1 == 3:
        Page3()
        choose_main()
        if choose1 == 1:
            Page1()
elif choose1 == 3:
    Page3()
    choose_main()
    if choose1 == 1:
        Page1()
        choose_main()
        if choose1 == 2:
            Page2()
    elif choose1 == 2:
        Page2()
        choose_main()
        if choose1 == 1:
            Page1()
else:
    print("参数错误，请按下回车键后重新选择")
    os.system("cls")
    choose_main()

EndPage()