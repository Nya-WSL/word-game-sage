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

os.system('')
title_console.print('''
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                     [r]小生物旅行记[/r]                   ┃
┃                                            [cyan]v1.0.0[/cyan]  ┃
┠────────────────────────────────────────────────────┨
┃               Screenwriter： [yellow]桑吉Sage[/yellow]              ┃
┃                                                    ┃
┃   Copyright [green]©[/green] [red]Nya-WSL[/red] 2022. [green]All rights reserved.[/green]   ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
''', justify="center")
start_console.print("[blue]按[bold red]回车[/bold red]开始游戏[/blue]", style="blink", justify="center")
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
