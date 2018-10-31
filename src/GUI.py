"""包的导入"""
import tkinter
import View
import Timer


class Gui(object):
    """生命游戏的界面设计及初始化"""



    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.alive = 0
        self.view = View.View()
        self.root = tkinter.Tk()
        self.root.title('Game of Life')
        self.root.geometry('600x640')
        # self.round_label = tkinter.Label(self.root, text='round:0')

        self.canvas = tkinter.Canvas(self.root, bg='white', width=560, height=560)
        self.canvas.place(x=20, y=20)
        # self.update()

        self.p_btn = tkinter.Button(self.root, width=8, text='pause', command=self.pause)
        self.p_btn.place(x=100, y=596)
        self.round_label = tkinter.Label(self.root, text='round:0')
        self.round_label.place(x=220, y=596)
        self.alive_label = tkinter.Label(self.root, text='Alive Cell:0')
        self.alive_label.place(x=300, y=596)
        self.start_button = tkinter.Button(self.root, text='start', width=8, command=self.start)
        self.start_button.place(x=20, y=596)

        tkinter.mainloop()

    def judge(self):
        """判断细胞并进行填充"""
        width = float(self.canvas['width'])
        height = float(self.canvas['height'])
        p_width = width/self.cols
        p_height = height/self.rows
        self.alive = 0
        self.canvas.create_rectangle(0, 0, width, height, fill="#fff", outline="#fff")
        for row in range(self.rows):
            for col in range(self.cols):
                if self.view.map[row][col] == 1:      # 活细胞进行黑色填充
                    self.alive += 1
                    self.canvas.create_rectangle(p_width*col, p_height*row,\
                                                 p_width*(1+col), p_height*(1+row), \
                                                 fill='#000', outline='#fff')

    def g_update(self):
        """界面更新"""
        self.round_label.config(text='round:'+str(self.view.round))
        self.view.update()
        self.judge()
        self.alive_label.config(text='Alive Cell:'+str(self.alive))

    def start(self):
        """游戏开始运行"""
        self.timer = Timer.Timer(2, self.g_update)
        self.timer.start()

    def hold(self):
        """游戏界面保持不变"""
        self.judge()

    def pause(self):
        """游戏暂停"""
        self.timer.pause()
        self.hold()


def main():
    """主函数，程序入口"""
    Gui(25, 25)


if __name__ == "__main__":
    main()
