import random
import sys
import time
import os

def slowprint_title(s):
    for c in s + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(random.random() * 0.003)

def slowprint_choose(s):
    for c in s + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(0.8)

def slowprint_text(s):
    for c in s + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(0.2)

def slowprint_1(s):
    for c in s + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(random.random() * 0.8)
#slowprint('スターリン主義は馬鹿だけだ、早くそんな塵芥を倒せ！') 

os.system('')

print("""
""")

slowprint_title("""  
.-..--. .-. .-..-.   .-..-. .-..-..-.     .-..--.   .-..-..-. .-..--.  .-..--. 
| | ~~  | | | | ~.-. | | ~   ~ | | ~      | | ~~.-. | | ~ | | | | ~~   | | ~~  
| | _   | | | |.-.~   \|       | |        | |.--.~  | |.-.| | | |  __  | | _   
| |`-'  | | | | ~.-.    |\     | |        | | ~~    | | ~ | | | | `. | | |`-'  
| |     | | | |  | |  _ | |    | |        | |       | |   | | | | _| | | | __  
`-'     `-' `-'  `-' `-'`-'    `-'        `-'       `-'   `-' `-'`---' `-'`--' """)
time.sleep(0.7)
input("回车开始游戏")

slowprint_text("""
很久很久以前，有一只谜之小生物。
为了躲避调查员的追杀，小生物使用了由好心的外星猫猫提供的修女身体。
可是，此时的小生物并不理解人类这一物种。
为了更好藏匿在人类社会之中，小生物开始了对人类的调查。
""")

slowprint_1("......")

print("""去哪里调查人类？""")
time.sleep(0.5)
slowprint_choose("""
1. 机场
2. 公司
3. 菜市场""")
input("你的选择是：")
