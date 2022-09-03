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
     time.sleep(random.random() * 0.06)

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
     time.sleep(1)

os.system('')
title_console.print('''
[cyan]┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓[/]
[cyan]┃[/]                     [r]小生物旅行记[/r]                   [cyan]┃[/]
[cyan]┃                                            [cyan]v1.0.0[/cyan]  [cyan]┃[/]
[cyan]┠────────────────────────────────────────────────────┨[/cyan]
[cyan]┃[/]               [white]Screenwriter：[/][yellow]桑吉Sage[/yellow]               [cyan]┃[/]
[cyan]┃[/]                                                    [cyan]┃[/]
[cyan]┃[/]   Copyright [green]©[/green] [red]Nya-WSL[/red] 2022. [green]All rights reserved.[/green]   [cyan]┃[/]
[cyan]┃[/]     https://github.com/Nya-WSL/word-game-sage      [cyan]┃[/]
[cyan]┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛[/]
''', justify="center")
start_console.print("[cyan]按[bold red]回车[/bold red]开始游戏[/cyan]", style="blink", justify="center")
input()
os.system("cls")

slowprint_title("""  
 __                _     _    
|_  o  __ _ _|_   |_) _ (_| _ 
|   |  | _>  |_   |  (_|__|(/_""")
time.sleep(5)
os.system("cls")
start_console.print("[cyan]按[bold red]回车[/bold red]开始游戏[/cyan]", style="blink", justify="center")
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
choose_console.print("1. [cyan]机场[/cyan]", justify="center")
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
    text_console.print("[cyan]晨宝[/]：", end="")
    time.sleep(1)
    slowprint_text("毕方...别走。")
    slowprint_text("""
他的语气非常轻，仿佛是害怕吓到对方似的。
但仅仅短短四个字，宛如压垮骆驼的最后一根稻草，让对面的金发红瞳资本家泪如雨下。
""")
    text_console.print("[cyan]毕方[/]：", end="")
    time.sleep(1)
    slowprint_text("混蛋，你为什么来...!")
    text_console.print("[cyan]毕方[/]：", end="")
    time.sleep(1)
    slowprint_text("...混蛋，为什么你会找到啊！")
    slowprint_text("""
情感宛如涌出的泪水，无法压抑无法控制地随着重力坠落。""")
    slowprint_a("""“啪嗒”""")
    slowprint_text("""
翻涌的内心，促使晨宝向对面奔去。
""")
    text_console.print("[cyan]毕方[/]：", end="")
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
大脑在大声尖叫停止，心脏中负罪感多到快要爆炸了。
""")
    slowprint_a("可是，可是")
    slowprint_text("""
即便如此，晨宝飞奔的脚步也没有停止。
即便如此，晨宝身体中的每一个细胞都在尖叫，都在呐喊：
""")
    print("晨宝", end="")
    slowprint_a("好喜欢毕方。")
    print()
    text_console.print("[cyan]晨宝[/]：", end="")
    time.sleep(1)
    slowprint_text("对不起，对不起，六翼...")
    slowprint_text("""
晨宝抱住了毕方。
他们接吻了。""")
    input("cg1")
    slowprint_text("""
晨宝和毕方深深吻住了对方。
用仿佛明天世界就会毁灭一般的，仿佛这就是二人仅剩最后一秒般的热情亲吻对方。""")
    text_console.print("[cyan]毕方[/]：", end="")
    time.sleep(1)
    slowprint_text("唔...晨宝...啾...")
    text_console.print("[cyan]晨宝[/]：", end="")
    time.sleep(1)
    slowprint_text("啾...")
    slowprint_text("""一旁六翼注视着二人。""")
    slowprint_text("""
用酸楚的，痛苦的，又温柔的希冀着二人获得幸福的目光默默地注视着他们。
公主找到了王子，晨宝找到了毕方。
从此他们就幸福地生活在了一起。
对于传统意义上的故事而言，这应当就是Happy Ending了。
和主角无关的配角就应当在这里退场，让主角满意，让作者满意，让观众满意。""")
    slowprint_a("""
——可是，好不甘心。
——可是，好痛苦。""")
    text_console.print("[cyan]六翼[/]：", end="")
    time.sleep(1)
    slowprint_text("明明，是我先来的...")
    text_console.print("[cyan]六翼[/]：", end="")
    time.sleep(1)
    slowprint_text("拥抱也好，撅撅也好，明明都是我先来的...")
    text_console.print("[cyan]六翼[/]：", end="")
    time.sleep(1)
    slowprint_text("为什么会这样呢...一边是喜欢的晨宝，一边是水群的朋友，为什么...")
    text_console.print("[cyan]六翼[/]：", end="")
    time.sleep(1)
    slowprint_text("....不甘心，不甘心，不甘心...呜...")
    text_console.print("[cyan]六翼[/]：", end="")
    time.sleep(1)
    slowprint_text("...我...我应该怎么做...")
    time.sleep(3)
    slowprint_1("......")
    time.sleep(1.5)
    print("""
    
""")
    text_console.print("此时小生物应该...？", justify="center")
    print()
    time.sleep(0.5)
    choose_console.print("1. [cyan]劝说六翼放弃晨宝[/cyan]", justify="center")
    choose_console.print("2. [green]劝说六翼继续追求晨宝[/green]", justify="center")
    print()
    time.sleep(1)
    choose2 = int(choose_console.input("[yellow]你的选择是：[/]"))
    if choose2 == 1:
        os.system("cls")
        slowprint_text("""爱情想必是强求不来的东西。
或许放弃对于双方来说才是最好的选择。
""")
        text_console.print("[cyan]六翼[/]：", end="")
        time.sleep(1)
        slowprint_text("你是说，我应该，给他自由吗...")
        text_console.print("[cyan]六翼[/]：", end="")
        time.sleep(1)
        slowprint_text("可是，可是，我放不下晨宝。")
        text_console.print("[cyan]六翼[/]：", end="")
        time.sleep(1)
        slowprint_text("我知道的，其实我一直都知道的。晨宝是个花心的孩子。他一直都那么交际花。")
        text_console.print("[cyan]六翼[/]：", end="")
        time.sleep(1)
        slowprint_text("他每天都在群里发撅撅我，又说要啃狐师傅高师傅头皮，还整天撩铜宝，甚至和秋暝击剑的次数我都数不清了。我知道的，我一直都知道的。")
        text_console.print("[cyan]六翼[/]：", end="")
        time.sleep(1)
        slowprint_text("他一向是一个，会自己寻找幸福的孩子。")
        text_console.print("[cyan]六翼[/]：", end="")
        time.sleep(1)
        slowprint_text("可是，我的幸福，却只有他一个人能给。")
        text_console.print("[cyan]六翼[/]：", end="")
        time.sleep(1)
        slowprint_text("即使！即使是他被别人撅了！")
        text_console.print("[cyan]六翼[/]：", end="")
        time.sleep(1)
        slowprint_text("...看到他被撅开心的脸我也就已经很幸福了。")
        text_console.print("[cyan]六翼[/]：", end="")
        time.sleep(1)
        slowprint_text("我无法放弃晨宝。")
        text_console.print("[cyan]六翼[/]：", end="")
        time.sleep(1)
        slowprint_text("还是谢谢你愿意劝说我。")
        text_console.print("[cyan]六翼[/]：", end="")
        time.sleep(1)
        slowprint_text("你真是个好人。")
        time.sleep(3)
        os.system("cls")
        slowprint_a("【获得道具：六翼的好人卡*1】")
        time.sleep(1.5)
        os.system("cls")
        slowprint_text("""小生物大受感动。
离开机场时，它暗自发誓，要成为一个能够守护男酮之悲恋的人。""")
    if choose2 == 2:
        os.system("cls")
        slowprint_text("""既然不甘心，既然痛苦。
那就应当拿出行动，继续努力。
""")
        text_console.print("[cyan]六翼[/]：", end="")
        time.sleep(1)
        slowprint_text("继续...努力吗？")
        text_console.print("[cyan]六翼[/]：", end="")
        time.sleep(1)
        slowprint_text("结婚之前都是公平竞争？你说的...好像是有些道理。")
        text_console.print("[cyan]六翼[/]：", end="")
        time.sleep(1)
        slowprint_text("的确，这不应该是结局。")
        text_console.print("[cyan]六翼[/]：", end="")
        time.sleep(1)
        slowprint_text("就这样放弃自己心爱的人或许太过轻易了。我的内心在大喊着不应该就这样结束。")
        text_console.print("[cyan]六翼[/]：", end="")
        time.sleep(1)
        slowprint_text("我不甘心，我不甘心。")
        text_console.print("[cyan]六翼[/]：", end="")
        time.sleep(1)
        slowprint_text("——而不甘心就应该去争取。")
        text_console.print("[cyan]六翼[/]：", end="")
        time.sleep(1)
        slowprint_text("的确，晨宝今天抛弃我选择了毕方，那么在将来他也有可能会离开毕方而重新选择其他人。")
        text_console.print("[cyan]六翼[/]：", end="")
        time.sleep(1)
        slowprint_text("这个其他人或许是鸽子王，或许是红月，或许……也可以是我！")
        text_console.print("[cyan]六翼[/]：", end="")
        time.sleep(1)
        slowprint_text("谢谢你，我下定决心了。")
        text_console.print("[cyan]六翼[/]：", end="")
        time.sleep(1)
        slowprint_text("我一定要撅到晨宝！")
        time.sleep(3)
        os.system("cls")
        slowprint_a("【获得道具：南桐六翼的认可*1】")
        time.sleep(1.5)
        os.system("cls")
        slowprint_text("""小生物大受感动。
离开机场时，它暗自发誓，要成为一个能够守护男酮之执恋的人。""")
if choose1 == 2:
    os.system("cls")
    text_console.print("公司", justify="center")
    time.sleep(3)
    os.system("cls")
    slowprint_text("""
小生物来到了一处公司。
据说这里是人类用劳动力换取报酬的地方，这对小生物而言是一个全新的概念。
想要用劳动力换取报酬的前提条件，则是参加一种名为“面试”的东西。
今天，这家名为“男酮工作室”的公司正在展开一场面试。
好奇的小生物溜进去时，正好是面试的中途。""")
    text_console.print("[cyan]冰蓝[/]：", end="")
    time.sleep(1)
    slowprint_text("你以为你接受的是谁的爱？是我的爱！")
    slowprint_text("""
坐在面试官位置的少女似乎正对面试者大发雷霆。
""")
    text_console.print("[cyan]冰蓝[/]：", end="")
    time.sleep(1)
    slowprint_text("我的爱！我的如此珍贵的爱！")
    text_console.print("[cyan]冰蓝[/]：", end="")
    time.sleep(1)
    slowprint_text("你竟敢拒绝我的爱！")
    print()
    slowprint_text("办公室的其他员工窃窃私语。")
    text_console.print("[yellow]（员工）游魂[/]：", end="")
    time.sleep(1)
    slowprint_text("我又漏看了两集？冰蓝这是怎么了？")
    text_console.print("[yellow]（员工）桶鸟[/]：", end="")
    time.sleep(1)
    slowprint_text("我不知道啊，昨天她不是和老G一起约会去了吗？照理说约会之后心情不应该非常好吗？")
    text_console.print("[yellow]（员工）027[/]：", end="")
    time.sleep(1)
    slowprint_text("嘘——你忘啦？上次冰蓝妹妹背着gamer给我偷偷发消息的事情？就是那个“027，gamer不在，人家想你啦><”那个！")
    text_console.print("[yellow]（员工）猫店长[/]：", end="")
    time.sleep(1)
    slowprint_text("这么说是有这么一回事，G先生该不会...")
    text_console.print("[yellow]（员工）雨林：", end="")
    time.sleep(1)
    slowprint_text("唔这么说gamer桑不太好吧...")
    text_console.print("[yellow]（员工）殷红[/]：", end="")
    time.sleep(1)
    slowprint_text("哎呀兄弟们，这个我觉得还是得再看看再看看。总之先吃瓜——")
    slowprint_text("""
这些精确控制音量的八卦猜测并没有传到当事人的耳朵里，冰蓝只是气呼呼地瞪着面前的人。
坐立不安的江江却听到了大家的讨论，有些尴尬地扭了扭脖子。
""")
    text_console.print("[cyan]江江[/]：", end="")
    time.sleep(1)
    slowprint_text("那个...")
    slowprint_text("""江江才张嘴，就换来对方的狠狠一瞪。
他吞吞口水，艰难地说出了下半句话。""")
    text_console.print("[cyan]江江[/]：", end="")
    time.sleep(1)
    slowprint_text("我，那个，对不起，你，你是个好人。")
    slowprint_text("""听了这句话，对面的火气更大了。。""")
    text_console.print("[cyan]冰蓝[/]：", end="")
    time.sleep(1)
    slowprint_text("为什么！！！你为什么要拒绝我的爱！")
    text_console.print("[cyan]冰蓝[/]：", end="")
    time.sleep(1)
    slowprint_text("没有人，没有人可以拒绝我的爱！")
    text_console.print("[cyan]冰蓝[/]：", end="")
    time.sleep(1)
    slowprint_text("只要你点点头接受了我，你现在就可以入职！")
    text_console.print("[cyan]冰蓝[/]：", end="")
    time.sleep(1)
    slowprint_text("不用再去参加任何的面试，不用再担心被开除。")
    text_console.print("[cyan]冰蓝[/]：", end="")
    time.sleep(1)
    slowprint_text("不用再担心像那个新闻里的45岁阿姨一样因为失业只能住桥洞里了。")
    text_console.print("[cyan]冰蓝[/]：", end="")
    time.sleep(1)
    slowprint_text("不用捡瓶盖，不用睡纸板箱，更不用担心半夜涨潮被河水冲走。")
    text_console.print("[cyan]冰蓝[/]：", end="")
    time.sleep(1)
    slowprint_text("你只需要接受我，然后在这份劳动合同上签名。")
    text_console.print("[cyan]冰蓝[/]：", end="")
    time.sleep(1)
    slowprint_text("然后每天工作18小时每周工作7天就可以了！")
    text_console.print("[cyan]冰蓝[/]：", end="")
    time.sleep(1)
    slowprint_text("还有经常的加班能够让你实现个人价值！这不是非常棒的条件吗！")
    text_console.print("[cyan]冰蓝[/]：", end="")
    time.sleep(1)
    slowprint_text("江江！把你余生的剩余价值交给我吧！")
    slowprint_text("说到激动处，冰蓝向对方伸出手，却被对方歪头躲过。")
    text_console.print("[cyan]江江[/]：", end="")
    time.sleep(1)
    slowprint_text("不好意西我想起来还有三十分钟我最爱的节目假面来不打就要播了我先走了——")
    slowprint_text("""江江宛如脱缰的菜狗一般冲出了办公室，只余下一片寂静。
孤独的冰蓝呆呆矗立在办公室的中央，还维持着手臂前伸的姿势。""")
    text_console.print("[cyan]冰蓝[/]：", end="")
    time.sleep(1)
    slowprint_a("...")
    text_console.print("[yellow]（员工）桶鸟[/]：", end="")
    time.sleep(1)
    slowprint_text("冰蓝酱好像有点可怜啊，昨天才被老G那样对待今天又失恋了。")
    text_console.print("[yellow]（员工）露鸢[/]：", end="")
    time.sleep(1)
    slowprint_text("比起可怜她，我想先问一下我们能挂她吗？")
    text_console.print("[yellow]（员工）殷红[/]：", end="")
    time.sleep(1)
    slowprint_text("我也觉得该挂啊兄弟们。")
    text_console.print("[yellow]（员工）猫店长[/]：", end="")
    time.sleep(1)
    slowprint_text("不太好吧，好歹过两天再挂。和G先生挂一起岂不是更好。")
    time.sleep(3)
    slowprint_1("......")
    time.sleep(1.5)
    print("""
    
""")
    text_console.print("此时小生物应该...？", justify="center")
    print()
    time.sleep(0.5)
    choose_console.print("1. [cyan]安慰冰蓝[/cyan]", justify="center")
    choose_console.print("2. [green]和员工一起挂冰蓝[/green]", justify="center")
    print()
    time.sleep(1)
    choose3 = int(choose_console.input("[yellow]你的选择是：[/]"))
    if choose3 == 1:
        os.system("cls")
        slowprint_text("""
即便是邪恶的资本家，也拥有追求爱情的权力。
即使是罪恶的资本家，在感到悲伤时也应被温柔以待
""")
        text_console.print("[cyan]冰蓝[/]：", end="")
        time.sleep(1)
        slowprint_text("谢谢你，你真是个温柔的好人。")
        time.sleep(3)
        print()
        slowprint_a("【获得道具：冰蓝的好人卡*1】")
        time.sleep(1.5)
        print()
        text_console.print("[cyan]冰蓝[/]：", end="")
        time.sleep(1)
        slowprint_text("但总是沉溺于悲伤的情感可不行，得抬头往前走。我现在必须得寻找我的下一个打工人了。")
        text_console.print("[cyan]冰蓝[/]：", end="")
        time.sleep(1)
        slowprint_text("说起来，你现在有工作吗？")
        text_console.print("[cyan]冰蓝[/]：", end="")
        time.sleep(1)
        slowprint_text("要是没有工作，有兴趣来我们这里打工吗？")
        text_console.print("[cyan]冰蓝[/]：", end="")
        time.sleep(1)
        slowprint_text("只要做7休0，每天只用上班18小时就可以了。")
        text_console.print("[cyan]冰蓝[/]：", end="")
        time.sleep(1)
        slowprint_text("是非常有竞争力的工作时间呢，还有经常的加班让你的能力得到更好的锻炼。")
        text_console.print("[cyan]冰蓝[/]：", end="")
        time.sleep(1)
        slowprint_text("如何？很宽厚的条件吧？")
        text_console.print("[cyan]冰蓝[/]：", end="")
        time.sleep(1)
        slowprint_text("今天签合同还送不锈钢大铁盆和牙刷牙杯，以后在公司打地铺加班的时候就更方便了。")
        slowprint_text("""
收到邀请的小生物大受感动。
离开公司时，它暗自发誓，要成为一个能够充满打工之力的人""")
    if choose3 == 2:
        os.system("cls")
    slowprint_text("""
正义理应得到伸张。
被压迫的打工人们渴望自由，渴望处刑为他们带来痛苦的源头。
员工们纷纷向小生物叙述自己曾经遭遇过的被压迫故事，让小生物听得眼泪汪汪。
小生物决心加入他们。
""")
    time.sleep(3)
    print()
    slowprint_a("【获得道具：打工群友的认可*1】")
    time.sleep(1.5)
    print()
    text_console.print("[cyan]冰蓝[/]：", end="")
    time.sleep(1)
    slowprint_text("你们，你们这是要做什么？！")
    text_console.print("[cyan]冰蓝[/]：", end="")
    time.sleep(1)
    slowprint_text("我给了你们工作，你们难道不应该感恩吗？")
    text_console.print("[cyan]冰蓝[/]：", end="")
    time.sleep(1)
    slowprint_text("觉得工资不够花，你们不会一天干25小时，一周干8天吗？")
    text_console.print("[cyan]冰蓝[/]：", end="")
    time.sleep(1)
    slowprint_text("快停下，没了我，你们连工作都没有——")
    slowprint_text("""
收到邀请的小生物大受感动。
离开公司时，它暗自发誓，要成为一个能够守护打工人的人""")