"""有关线程的包的导入"""
import threading

class Timer(object):
    """游戏时间以及线程的更新"""
    def __init__(self, time, function):
        self.time = time
        self.function = function
        self.__flag = threading.Event()     # 用于暂停线程的标识
        self.__flag.set()       # 设置为True

    def start(self):
        """游戏开始计时"""
        print('start')
        self._timer = threading.Timer(self.time, self.run)
        self._timer.setDaemon(True)
        self._timer.start()

    def run(self):
        """线程开始运行"""
        if self.__flag.isSet():
            print('run')
            try:
                self.function()
            except:
                pass
            self.start()

    def pause(self):
        """线程及时间暂停"""
        print('pause')
        self.__flag.clear()
