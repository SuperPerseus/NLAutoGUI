import win32gui
import win32con
import ctypes


def maximize_and_center(hwnd):
    # 将窗口最大化
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
    user32 = ctypes.windll.user32
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)


if __name__ == '__main__':
    maximize_and_center(68366)