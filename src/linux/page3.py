from .slowprint import slowprint_text, slowprint_1
from rich.console import Console
import time
import os

title_console = Console(color_system="windows")
start_console = Console(color_system="windows")
text_console = Console(color_system="windows")
choose_console = Console(color_system="windows")

def Page3():
    os.system("clear")
    text_console.print("菜市场", justify="center")
    time.sleep(3)
    os.system("clear")
    slowprint_text("""
小生物来到了一座菜市场。
正所谓人生在世，吃喝二字，要了解人类，就应该从人类的吃喝学起。
菜市场就自然是一个非常值得调查的地方。
小贩的吆喝声、顾客的讨价还价声、哐哐的剁肉声交织在一起，奏成了一首满是人间烟火气息的交响曲。
小生物正跟随着人流缓慢前行着，她的目光突然被一处摊贩吸引。
这个小摊处于菜市场的边缘位置，地上铺着一张红白蓝的塑料布，左半边不太齐整地排着几条不同种类的死鱼，而右半边则搁着一只水盆。水盆的旁边立着足有半人高的硬纸板，拿红漆刷着几个大字。
“王靳鱼专卖”
老板是皮肤发绿的健壮男人，光头在正午的太阳下折射出一片明亮的光辉，此时正忙着招揽面前的客人。
""")
    text_console.print("[yellow]027[/]：", end="")
    time.sleep(1)
    slowprint_text("哟靓仔，买点什么不？看看新到的蛇和鱼和王靳鱼吗？")
    text_console.print("[red]红白[/]：", end="")
    time.sleep(1)
    slowprint_text("？王靳鱼是什么东西")
    slowprint_text("""老板露出一个营业笑容，伸手示意周围的客人都靠近一些。
小生物也向前走了几步，这时它才清楚地看见，水盆里摆放着一条非常特别的鱼。
它的形状有些许像缩小版的鲸鱼，但这条鱼的前脊处长着一排形状奇怪的鳍，从远处看仿佛头上顶着王冠。""")
    text_console.print("[yellow]027[/]：", end="")
    time.sleep(1)
    slowprint_text("来，看看这条鱼二位。这可是稀有的好东西。")
    text_console.print("[yellow]027[/]：", end="")
    time.sleep(1)
    slowprint_text("据说这鱼产自极东之地的桑尾草园，非常受当地人的喜爱。")
    text_console.print("[yellow]027[/]：", end="")
    time.sleep(1)
    slowprint_text("它不仅外表美丽，具有极高的使用价值；而且营养丰富，味道也极其鲜美。")
    text_console.print("[yellow]027[/]：", end="")
    time.sleep(1)
    slowprint_text("是居家旅行必备之良品啊！")
    text_console.print("[red]红白[/]：", end="")
    time.sleep(1)
    slowprint_text("哦哦，听老板这么说我有点心动了啊。既然是出了名的好吃的鱼，过几天家里人生日的主菜就用这个吧。")
    text_console.print("[red]红白[/]：", end="")
    time.sleep(1)
    slowprint_text("正好拿王靳鱼做一道酸菜鱼。")
    slowprint_text("""他已经掏出钱包，准备付钱。
这时，一位青年挡在了他的面前。""")
    text_console.print("[yellow]袭秋[/]：", end="")
    time.sleep(1)
    slowprint_text("等等——")
    text_console.print("[yellow]袭秋[/]：", end="")
    time.sleep(1)
    slowprint_text("能把这条鱼让给我吗？")
    text_console.print("[yellow]袭秋[/]：", end="")
    time.sleep(1)
    slowprint_text("我，我爱上她了。")
    text_console.print("[yellow]袭秋[/]：", end="")
    time.sleep(1)
    slowprint_text("我要让她成为我的一生挚爱。")
    text_console.print("[yellow]027[/]：", end="")
    time.sleep(1)
    slowprint_text("？")
    text_console.print("[red]红白[/]：", end="")
    time.sleep(1)
    slowprint_text("？")
    slowprint_text("青年十分腼腆地抿抿嘴唇，继续说到。")
    text_console.print("[yellow]袭秋[/]：", end="")
    time.sleep(1)
    slowprint_text("不知为什么，冥冥之中，我竟觉得她跟我有一丝非常微妙的联系。")
    text_console.print("[yellow]袭秋[/]：", end="")
    time.sleep(1)
    slowprint_text("我不知道怎么想的，就觉得她会是我命运中的另一半。在你看来我应该是个很幼稚很蠢的人吧。")
    text_console.print("[yellow]袭秋[/]：", end="")
    time.sleep(1)
    slowprint_text("但是我相信我心中的感情！")
    text_console.print("[yellow]袭秋[/]：", end="")
    time.sleep(1)
    slowprint_text("爱情就是这样的不讲道理，我看到她的第一眼，我就知道了。")
    slowprint_text("""他的双颊通红，但是眼神却非常坚定。
红白和鱼摊老板似乎都被这位青年的告白感动了。沉默了一会，老板开口了。""")
    text_console.print("[yellow]027[/]：", end="")
    time.sleep(1)
    slowprint_text("啊这，两位都想买啊。")
    text_console.print("[yellow]027[/]：", end="")
    time.sleep(1)
    slowprint_text("凡事都讲先来后到，但是这位的理由确实又感人。可惜我这只有一条鱼呢...")
    text_console.print("[yellow]027[/]：", end="")
    time.sleep(1)
    slowprint_text("要卖给谁好呢？")
    slowprint_text("老板似乎陷入了犹豫之中。")
    time.sleep(3)
    slowprint_1("......")
    time.sleep(1.5)
    print("""
    
""")
    text_console.print("此时小生物应该劝说老板...？", justify="center")
    print()
    time.sleep(0.5)
    choose_console.print("1. [cyan]把王靳鱼卖给红白[/cyan]", justify="center")
    choose_console.print("2. [green]把王靳鱼卖给袭秋[/green]", justify="center")
    print()
    time.sleep(1)
    global choose4
    choose4 = int(choose_console.input("[yellow]你的选择是：[/]"))
    if choose4 == 1:
        os.system("clear")
        slowprint_text("""
先来后到，遵守规则。
把这条鱼让给先来的人吧，况且他家人生日这样的时机，要是有了这样的好食材，可谓锦上添花。
老板听了小生物的劝说，也认可地摸摸下巴。
哐哐几刀下去，老板就熟练地宰杀了王靳鱼。他把鱼肉和内脏分开塞进了不同的塑料袋，然后递给红白。
红白则非常高兴地向小生物点点头。
""")
        text_console.print("[red]红白[/]：", end="")
        time.sleep(1)
        slowprint_text("哎呀，你真是个好人。")
        time.sleep(3)
        print()
        slowprint_text("【获得道具：红白的好人卡*1】")
        time.sleep(1.5)
        print()
        slowprint_text("""想必之后，他们会有一场非常愉快的家庭聚会吧。
小生物想着这一点，露出了笑容。
离开菜市场时，小生物暗暗发誓。
它一定要成为一个守护规则的人""")
    elif choose4 == 2:
        os.system("clear")
        slowprint_text("""
即使是人和鱼的感情也是伟大的。
这份爱情虽然不为世人所容，但是它的真挚却无可否认。
""")
        text_console.print("[yellow]袭秋[/]：", end="")
        time.sleep(1)
        slowprint_text("！")
        text_console.print("[yellow]袭秋[/]：", end="")
        time.sleep(1)
        slowprint_text("你，你能理解我吗？")
        text_console.print("[yellow]袭秋[/]：", end="")
        time.sleep(1)
        slowprint_text("我，我其实已经做好了被骂恶心，被骂变态，被骂滚出去的心理准备了。")
        text_console.print("[yellow]袭秋[/]：", end="")
        time.sleep(1)
        slowprint_text("但是...谢谢你——谢谢——")
        slowprint_text("青年握着小生物的手，一时泪如雨下。")
        time.sleep(3)
        print()
        slowprint_text("【获得道具：变tai..大爱无疆者的认可*1】")
        time.sleep(1.5)
        print()
        slowprint_text("看到这样的场面，一开始有些犹豫的老板和红白也有些感动。")
        text_console.print("[red]红白[/]：", end="")
        time.sleep(1)
        slowprint_text("...算了，让给他吧。")
        text_console.print("[red]红白[/]：", end="")
        time.sleep(1)
        slowprint_text("比起被我吃掉，或许这才是更好的结局。")
        text_console.print("[yellow]027[/]：", end="")
        time.sleep(1)
        slowprint_text("是啊，让他们获得幸福吧。")
        slowprint_text("""
青年捧着王靳鱼，开心地离开了。
小生物大受感动。
离开菜市场时，它暗自发誓，要成为一个能够守护超越人类之恋的人。""")