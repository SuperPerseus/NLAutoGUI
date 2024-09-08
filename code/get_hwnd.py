import win32gui
import win32con


class WindowEnumerator:
    def __init__(self):
        self.windows = {}
        self.enumerate_windows()

    def enum_windows_callback(self, hwnd, _):
        title = win32gui.GetWindowText(hwnd)
        if win32gui.IsWindowVisible(hwnd) and len(title) > 0:
            self.windows[hwnd] = title

    def enumerate_windows(self):
        win32gui.EnumWindows(self.enum_windows_callback, None)


if __name__ == '__main__':
    we=WindowEnumerator()
    print(we.windows)