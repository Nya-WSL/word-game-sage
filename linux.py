from src.linux.slowprint import slowprint_1, slowprint_text, slowprint_title
from rich.console import Console
#from update import check_update
from src.linux.end_page import EndPage
from src.linux.page1 import Page1
from src.linux.page2 import Page2
from src.linux.page3 import Page3
#from flask import Flask
from rich import print
import time
import os

#check_update()

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0', port=80)

title_console = Console(color_system="auto")
start_console = Console(color_system="auto")
text_console = Console(color_system="auto")
choose_console = Console(color_system="auto")

#开始游戏
title_console.print('''
[cyan]┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓[/]
[cyan]┃[/]                     [r]小生物旅行记[/r]                   [cyan]┃[/]
[cyan]┃                                            [cyan]v1.0.5[/cyan]  [cyan]┃[/]
[cyan]┠────────────────────────────────────────────────────┨[/cyan]
[cyan]┃[/]               [white]Screenwriter：[/][yellow]桑吉Sage[/yellow]               [cyan]┃[/]
[cyan]┃[/]                                                    [cyan]┃[/]
[cyan]┃[/]   Copyright [green]©[/green] [red]Nya-WSL[/red] 2022. [green]All rights reserved.[/green]   [cyan]┃[/]
[cyan]┃[/]   https://nya-wsl.com/6723413/game/Sage_Travels    [cyan]┃[/]
[cyan]┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛[/]
''', justify="center")
start_console.print("[cyan]按[bold red]回车[/bold red]开始游戏[/cyan]", style="blink", justify="center")
input()
os.system("clear")

slowprint_title("""  
 __                _     _    
|_  o  __ _ _|_   |_) _ (_| _ 
|   |  | _>  |_   |  (_|__|(/_""")
time.sleep(5)
os.system("clear")
start_console.print("[cyan]按[bold red]回车[/bold red]开始游戏[/cyan]", style="blink", justify="center")
input()
os.system("clear")

slowprint_text("""很久很久以前，有一只谜之小生物。
为了躲避调查员的追杀，小生物使用了由好心的外星猫猫提供的修女身体。
可是，此时的小生物并不理解人类这一物种。
为了更好藏匿在人类社会之中，小生物开始了对人类的调查。""")

os.system("clear")
time.sleep(1.5)
slowprint_1("......")
time.sleep(1.5)
os.system("clear")

def choose_main():
    global choose1
    text_console.print("去哪里调查人类？", justify="center")
    print()
    time.sleep(0.5)
    choose_console.print("1. [cyan]机场[/cyan]", justify="center")
    choose_console.print("2. [green]公司[/green]", justify="center")
    choose_console.print("3. [red]菜市场[/red]", justify="center")
    print()
    time.sleep(1)
    global choose1
    choose1 = int(choose_console.input("[yellow]你的选择是：[/]"))

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
    text_console.print("[blod red]参数错误，请按下回车键后重新选择", justify="center")
    os.system("clear")
    choose_main()

EndPage()