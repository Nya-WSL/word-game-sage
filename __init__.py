from rich.console import Console
from rich import print
import random
import sys
import time
import os

title_console = Console(color_system="windows")
start_console = Console(color_system="windows")
text_console = Console(color_system="windows")
choose_console = Console(color_system="windows")

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

def slowprint_a(s):
    for c in s + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(random.random() * 1)

os.system('')
title_console.print('''
[cyan]┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓[/]
[cyan]┃[/]                     [r]小生物旅行记[/r]                   [cyan]┃[/]
[cyan]┃                                            [cyan]v1.0.0[/cyan]  [cyan]┃[/]
[cyan]┠────────────────────────────────────────────────────┨[/cyan]
[cyan]┃[/]               [white]Screenwriter：[/][yellow]桑吉Sage[/yellow]               [cyan]┃[/]
[cyan]┃[/]                                                    [cyan]┃[/]
[cyan]┃[/]   Copyright [green]©[/green] [red]Nya-WSL[/red] 2022. [green]All rights reserved.[/green]   [cyan]┃[/]
[cyan]┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛[/]
''', justify="center")
start_console.print("[cyan]按[bold red]回车[/bold red]开始游戏[/cyan]", style="blink", justify="center")
input()
os.system("cls")

slowprint_title("""  
.-..--. .-. .-..-.   .-..-. .-..-..-.     .-..--.   .-..-..-. .-..--.  .-..--. 
| | ~~  | | | | ~.-. | | ~   ~ | | ~      | | ~~.-. | | ~ | | | | ~~   | | ~~  
| | _   | | | |.-.~   \|       | |        | |.--.~  | |.-.| | | |  __  | | _   
| |`-'  | | | | ~.-.    |\     | |        | | ~~    | | ~ | | | | `. | | |`-'  
| |     | | | |  | |  _ | |    | |        | |       | |   | | | | _| | | | __  
`-'     `-' `-'  `-' `-'`-'    `-'        `-'       `-'   `-' `-'`---' `-'`--' """)
time.sleep(3)
os.system("cls")
start_console.print("[blue]按[bold red]回车[/bold red]开始游戏[/blue]", style="blink", justify="center")
input()
os.system("cls")

slowprint_text("""
很久很久以前，有一只谜之小生物。
为了躲避调查员的追杀，小生物使用了由好心的外星猫猫提供的修女身体。
可是，此时的小生物并不理解人类这一物种。
为了更好藏匿在人类社会之中，小生物开始了对人类的调查。
""")

os.system("cls")
time.sleep(1.5)
slowprint_1("......")
time.sleep(1.5)
os.system("cls")

text_console.print("去哪里调查人类？", justify="center")
print()
time.sleep(0.5)
choose_console.print("1. [blue]机场[/blue]", justify="center")
choose_console.print("2. [green]公司[/green]", justify="center")
choose_console.print("3. [red]菜市场[/red]", justify="center")
print()
time.sleep(1)
choose1 = int(choose_console.input("[yellow]你的选择是：[/]"))
if choose1 == 1:
    os.system("cls")
    text_console.print("机场", justify="center")
    time.sleep(3)
    os.system("cls")
    slowprint_text("""
小生物来到了一处机场。
据猫猫说，这样的交通要道是人类聚集之地。
想必在这样的地方，一定能看到不少有趣的人类故事。
可能是由于疫情缘由，机场的人并不算多。而这稀疏人群中，大厅正中央中伫立着的三位男性格外醒目。""")
    slowprint_text("""
三人均是面色凝重，即便不熟悉人类文化的小生物也能感觉到空气中的沉重气氛。""")
    slowprint_text("""
僵持许久，年纪最轻的男孩开口打破了沉默。
""")
    text_console.print("[blue]晨宝[/]：", end="")
    time.sleep(1)
    slowprint_text("毕方...别走。")
    slowprint_text("""
他的语气非常轻，仿佛是害怕吓到对方似的。
但仅仅短短四个字，宛如压垮骆驼的最后一根稻草，让对面的金发红瞳资本家泪如雨下。""")
    text_console.print("[blue]毕方[/]：", end="")
    time.sleep(1)
    slowprint_text("混蛋，你为什么来...!")
    text_console.print("[blue]毕方[/]：", end="")
    time.sleep(1)
    slowprint_text("...混蛋，为什么你会找到啊！")
    slowprint_text("""
情感宛如涌出的泪水，无法压抑无法控制地随着重力坠落。
“啪嗒”
翻涌的内心，促使晨宝向对面奔去。""")
    text_console.print("[blue]毕方[/]：", end="")
    time.sleep(1)
    slowprint_text("！停下，晨宝，六翼在看着...")
    slowprint_text("""
这样是不行的。
这样是不能被允许的。
晨宝不应该背叛六翼。
那个每天在群里笑笑闹闹，给自己发红豆流汗脸的六翼。
那个打出“狠狠地撅晨宝”之后，又会附上傲娇表情的六翼。
那个在DD歌会用歌声唱出“gamer和晨宝相比，那我还是觉得晨宝刺激”的六翼。
那个一直守望着自己，说着“晨宝，就算你被撅了，我还是爱你的”的六翼。
大脑在大声尖叫停止，心脏中负罪感多到快要爆炸了。""")
    slowprint_a("可是，可是——")
    slowprint_text("""
即便如此，晨宝飞奔的脚步也没有停止。
即便如此，晨宝身体中的每一个细胞都在尖叫，都在呐喊：
""")
    print("晨宝", end="")
    slowprint_a("好喜欢毕方。")
    print()
    text_console.print("[blue]晨宝[/]：", end="")
    time.sleep(1)
    slowprint_text("对不起，对不起，六翼...")
    slowprint_text("""
晨宝抱住了毕方。
他们接吻了。""")
    input("cg1")
    slowprint_text("""
晨宝和毕方深深吻住了对方。
用仿佛明天世界就会毁灭一般的，仿佛这就是二人仅剩最后一秒般的热情亲吻对方。""")