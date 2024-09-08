import os
import time
from PIL import ImageGrab
import win32gui
import win32con

"""def screencut(hwnd):
    if hwnd == 0:
        # 如果句柄为0，表示没有找到对应的窗口
        return None

    directory = "../image/screen_catch"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # 确保窗口句柄有效
    if not win32gui.IsWindow(hwnd):
        print("无效的窗口句柄")
        return None

    # 最小化窗口
    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

    # 等待一段时间，确保窗口已经最小化
    time.sleep(1)

    # File path with timestamp
    file_path = os.path.join(directory, f"full-screen_{int(time.time())}.png")

    try:
        # Take a screenshot and save it to the specified directory
        screenshot = ImageGrab.grab()
        screenshot.save(file_path)
        # 如果没有发生异常，则返回文件名
        return file_path
    except Exception as e:
        # 如果发生异常，打印错误信息
        print(f"发生错误：{e}")
        return None
    finally:
        # 还原窗口
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)"""


def screenshot(hwnd):
    directory = "../image/screen_catch"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # 确保窗口句柄有效
    if not win32gui.IsWindow(hwnd):
        print("无效的窗口句柄")
        return None

    # 最小化窗口
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

    # 等待一段时间，确保窗口已经最小化
    time.sleep(1)

    # File path with timestamp
    file_path = os.path.join(directory, f"full-screen_{int(time.time())}.png")

    try:
        # Take a screenshot and save it to the specified directory
        screenshot = ImageGrab.grab()
        screenshot.save(file_path)
        # 如果没有发生异常，则返回文件名
        return file_path
    except Exception as e:
        # 如果发生异常，打印错误信息
        print(f"发生错误：{e}")
        return None


if __name__ == '__main__':
    screenshot()
