import ctypes
import time


class Analogue_IO:
    VK_LWIN = 0x5B  # 左Win键
    VK_D = 0x44  # D键
    keybd_event = ctypes.windll.user32.keybd_event

    def win_D(self):
        # 模拟按下左Win键
        self.keybd_event(self.VK_LWIN, 0, 0, 0)
        # 模拟按下D键
        self.keybd_event(self.VK_D, 0, 0, 0)
        # 释放D键
        self.keybd_event(self.VK_D, 0, 2, 0)
        # 释放左Win键
        self.keybd_event(self.VK_LWIN, 0, 2, 0)
