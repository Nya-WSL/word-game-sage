from .slowprint import slowprint_a, slowprint_title, slowprint_text, slowprint_end
from rich.console import Console
from rich import print
from . import page1
from . import page2
from . import page3
import webbrowser
import time
import sys
import os

title_console = Console(color_system="windows")
start_console = Console(color_system="windows")
text_console = Console(color_system="windows")
choose_console = Console(color_system="windows")

def EndPage():
    os.system("clear")
    slowprint_a("......")
    os.system("clear")
    slowprint_title("""  
 __             _ 
|_ __  _| o __ (_|
|__| |(_| | | |__|""")
    time.sleep(5)
    os.system("clear")
    start_console.print("[cyan]按[bold red]回车[/bold red]进入结局戏[/cyan]", style="blink", justify="center")
    input()
    os.system("clear")
    slowprint_text("""
太阳落山了，小生物的人类调查到此结束。
是时候检查自己在本次调查中的收获了。
它回到了自己的桥洞，开始回想自己今天的经历。
今天是非常漫长的一天，它回想起了自己在旅途之中所下的决心——
""")
    if page1.choose2 == 1 and page2.choose3 == 1 and page3.choose4 == 1:
        slowprint_text("""
——要成为一个能够守护男酮之悲恋的人。
——要成为一个能够充满打工之力的人。
——成为一个能够守护规则的人。
它开始翻看自己的背包。
【六翼的好人卡*1】
【冰蓝的好人卡*1】
【红白的好人卡*1】
小生物虽然没有改变途中遇到伙伴的现状，也没有改变故事结局，但是它获得了他人的称赞。
它做到了成为一个好人。
在今后的道路上，想必小生物也会继续做一个热爱南桐，并且守护规则的南桐爱好者吧。
想到这里，小生物嘴角露出欣慰笑容，进入了快乐的梦乡。
""")
        time.sleep(2)
        print("-")
        time.sleep(2)
        slowprint_text("""
第二天，附近的人们听说，桥下多出来了一座桥洞教堂。
听说在那里，有一位好人修女。
虽然据说修女有爱好南桐的怪癖，但只要是去过桥洞教堂的人们都会这样称赞她：""")
        slowprint_a("“是个好人。”")
        time.sleep(5)
        slowprint_end("""Thank you for playing.
Normal Ending: 好人修女""")

    elif page1.choose2 == 2 and page2.choose3 == 2 and page3.choose4 == 2:
        slowprint_text("""
——要成为一个能够守护男酮之执恋的人。
——要成为一个能够守护打工人的人。
——要成为一个能够守护超越人类之恋的人
在这样的道路上，小生物改变了相遇之人的命运，也获得了悲恋之人的，打工之人和变tai...大爱无疆之人的认可。
它做到了成为一个改变事物的人。
在今后的道路上，想必小生物也会继续做一个守护各种恋情并保护打工人的人吧。
虽然前行的道路是未知的，但是来自友人们的认可会是小生物心中永恒的宝物。
这份宝物会给与她勇气，使她能够继续前进
""")
        time.sleep(2)
        print("-")
        time.sleep(2)
        slowprint_text("""
第二天，附近的人们听说，桥下多出来了一座桥洞教堂。
听说在那里，有一位不可思议的修女。
虽然据说修女有爱好南桐和欣赏超越人类理解范畴的恋爱的怪癖，但只要是去过桥洞教堂的人们都会这样称赞她：""")
        slowprint_a("“是个能带来改变，促使人不断前进的好修女。”")
        time.sleep(5)
        slowprint_end("""Thank you for playing.
Good Ending: 变革的修女""")
    else:
        slowprint_text("""
似乎自己还没有足够的觉悟。
又或许是还没有搜集到足够多的东西。
小生物闭上眼，进入了梦乡。
或许，或许——
在下一次的冒险中，会有不同的结局...？
""")
        time.sleep(5)
        slowprint_end("""Thank you for playing.
Bad Ending: 不知前路为何的修女""")

    slowprint_end("""
小生物旅行记v1.0.2
——————
感谢游玩！
制作组：Nya-WSL
编剧：桑吉Sage
cg：冰蓝
友情出演：
晨宝 冰蓝
毕方 六翼
游魂 桶鸟
027 猫店长
雨林 殷红
江江 露鸢
红白 袭秋
——————
Thank you for playing.
希望各位玩家的每一天都是Happy Ending.
""")

#花絮
    time.sleep(5)
    slowprint_a("......")
    choose_end = choose_console.input("[yellow]是否查看花絮？(y/n)[/]")
    if choose_end == "n" or choose_end == "N":
        input("感谢游玩")
        sys.exit()
    else:
        url = "https://nya-wsl.com/word-game/sage/tidbits"
        webbrowser.open(url, new=0, autoraise=True)