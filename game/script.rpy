define e = Character("kuro")
default persistent.maxnum=0
init python:
    #游戏主逻辑
    def good(direct):
        if direct == 'a':
            a.move()
        elif direct == "d":
            a.move(True)
        elif direct == "w":
            a.change()
            a.move()
            a.change()
        else:
            a.change()
            a.move(True)
            a.change()  
        a.random_num()
        if a.damn()==True:
            renpy.jump("gg")

label start:
    e "欢迎玩2048！！！"
    menu:
        e "你想要的大小？"
        "4X4":
            $ a=matrix(4,4)
            $ a.random_num()
            $ a.random_num()
    show screen board2(a.matrix)
    show screen direction_control
    show screen inform
    window hide
    pause
    jump loop


label loop:
    show screen board2(a.matrix)
    show screen inform
    pause
    jump loop


label gg:
    e "才合出[a.maxnum]，"
    e "说白了你就是菜。"
    $ persistent.maxnum=a.maxnum
    return

