# 游戏的脚本可置于此文件中。
# 简化版本
# 定义数字对应的颜色映射
define number_colors = {
    2: "#eee4da",
    4: "#ede0c8", 
    8: "#f2b179",
    16: "#f59563",
    32: "#f67c5f",
    64: "#f65e3b",
    128: "#edcf72",
    256: "#edcc61",
    512: "#edc850",
    1024: "#edc53f",
    2048: "#edc22e"
}

# 默认颜色，用于未在映射中定义的数字
define default_color = "#cdc1b4"

# 显示数字矩阵的屏幕
screen board2(matrix, cell_size=100, spacing=10):
    # 计算矩阵的尺寸
    $ rows = len(matrix)
    $ cols = len(matrix[0]) if rows > 0 else 0
    
    # 计算总宽度和高度
    $ total_width = cols * cell_size + (cols - 1) * spacing
    $ total_height = rows * cell_size + (rows - 1) * spacing
    
    # 主容器
    frame:
        xalign 0.5
        yalign 0.5
        xsize total_width
        ysize total_height
        background None
        
        # 使用网格布局放置数字方块
        grid cols rows:
            xalign 0.5
            yalign 0.5
            spacing spacing
            
            # 遍历矩阵中的每个元素
            for i in range(rows):
                for j in range(cols):
                    $ number = matrix[i][j]
                    $ color = number_colors.get(number, default_color)
                    
                    # 数字方块
                    frame:
                        xsize cell_size
                        ysize cell_size
                        background color
                        
                        # 显示数字
                        if number > 0:
                            text str(number):
                                size int(cell_size * 0.4)
                                if number < 8:
                                    color "#776e65"
                                else:
                                    color "#f9f6f2"
                                align (0.5, 0.5)
                                text_align 0.5
# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define e = Character("xxc")
init python:
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
        
# 老的游戏界面
# screen board:
    # frame:
        # xalign 0.5 
        # yalign 0.5
        # grid 4 4:
            # spacing 30
            # for line in a.matrix:
                # for num in line:
                    # text"[num]"

# 游戏在此开始。

label start:
    "欢迎玩2048！！！"
    
    menu:
        "你想要的大小？"
        "4X4":
            $ a=matrix(4,4)
            $ a.random_num()
            $ a.random_num()
    show screen board2(a.matrix)
    show screen direction_control
    window hide
    pause
    jump loop

label loop:
    show screen board2(a.matrix)
    pause
    jump loop

label gg:
    "说白了你就是菜"
    return


screen direction_control():
    zorder 100
    modal False
    
    # 方向键按钮布局
    fixed:
        pos (100, 100)  # 调整这个位置来移动整个控制面板
        xysize (300, 300)
        
        # 上键
        button:
            pos (100, 0)
            xysize (100, 100)
            action Function(good,"w"),Jump("loop")
            keysym "K_UP"
            background Solid("#888888")
            text "↑" size 40 align (0.5, 0.5)

        
        # 下键
        button:
            pos (100, 200)
            xysize (100, 100)
            action Function(good,"s"),Jump("loop")
            keysym "K_DOWN"
            background Solid("#888888")
            text "↓" size 40 align (0.5, 0.5)
        
        # 左键
        button:
            pos (0, 100)
            xysize (100, 100)
            action Function(good,"a"),Jump("loop")
            keysym "K_LEFT"
            background Solid("#888888")
            text "←" size 40 align (0.5, 0.5)
        
        # 右键
        button:
            pos (200, 100)
            xysize (100, 100)
            action Function(good,"d"),Jump("loop")
            keysym "K_RIGHT"
            background Solid("#888888")
            text "→" size 40 align (0.5, 0.5)



