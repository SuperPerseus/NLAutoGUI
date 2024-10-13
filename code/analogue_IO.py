import ctypes
import time


class Analogue_IO:
    VK_CODE = {
        'backspace': 0x08, 'tab': 0x09, 'clear': 0x0C, 'enter': 0x0D,
        'shift': 0x10, 'ctrl': 0x11, 'alt': 0x12, 'pause': 0x13, 'caps_lock': 0x14,
        'esc': 0x1B, 'spacebar': 0x20, 'page_up': 0x21, 'page_down': 0x22,
        'end': 0x23, 'home': 0x24, 'left_arrow': 0x25, 'up_arrow': 0x26,
        'right_arrow': 0x27, 'down_arrow': 0x28, 'select': 0x29, 'print': 0x2A,
        'execute': 0x2B, 'print_screen': 0x2C, 'insert': 0x2D, 'delete': 0x2E,
        'help': 0x2F, '0': 0x30, '1': 0x31, '2': 0x32, '3': 0x33,
        '4': 0x34, '5': 0x35, '6': 0x36, '7': 0x37, '8': 0x38,
        '9': 0x39, 'a': 0x41, 'b': 0x42, 'c': 0x43, 'd': 0x44,
        'e': 0x45, 'f': 0x46, 'g': 0x47, 'h': 0x48, 'i': 0x49,
        'j': 0x4A, 'k': 0x4B, 'l': 0x4C, 'm': 0x4D, 'n': 0x4E,
        'o': 0x4F, 'p': 0x50, 'q': 0x51, 'r': 0x52, 's': 0x53,
        't': 0x54, 'u': 0x55, 'v': 0x56, 'w': 0x57, 'x': 0x58,
        'y': 0x59, 'z': 0x5A, 'left_win': 0x5B, 'right_win': 0x5C,
        'applications': 0x5D, 'sleep': 0x5F, 'numpad_0': 0x60, 'numpad_1': 0x61,
        'numpad_2': 0x62, 'numpad_3': 0x63, 'numpad_4': 0x64, 'numpad_5': 0x65,
        'numpad_6': 0x66, 'numpad_7': 0x67, 'numpad_8': 0x68, 'numpad_9': 0x69,
        'multiply': 0x6A, 'add': 0x6B, 'separator': 0x6C, 'subtract': 0x6D,
        'decimal': 0x6E, 'divide': 0x6F, 'f1': 0x70, 'f2': 0x71, 'f3': 0x72,
        'f4': 0x73, 'f5': 0x74, 'f6': 0x75, 'f7': 0x76, 'f8': 0x77,
        'f9': 0x78, 'f10': 0x79, 'f11': 0x7A, 'f12': 0x7B, 'f13': 0x7C,
        'f14': 0x7D, 'f15': 0x7E, 'f16': 0x7F, 'f17': 0x80, 'f18': 0x81,
        'f19': 0x82, 'f20': 0x83, 'f21': 0x84, 'f22': 0x85, 'f23': 0x86,
        'f24': 0x87, 'num_lock': 0x90, 'scroll_lock': 0x91,
        'left_shift': 0xA0, 'right_shift': 0xA1, 'left_control': 0xA2,
        'right_control': 0xA3, 'left_menu': 0xA4, 'right_menu': 0xA5,
        'browser_back': 0xA6, 'browser_forward': 0xA7, 'browser_refresh': 0xA8,
        'browser_stop': 0xA9, 'browser_search': 0xAA, 'browser_favorites': 0xAB,
        'browser_home': 0xAC, 'volume_mute': 0xAD, 'volume_down': 0xAE,
        'volume_up': 0xAF, 'media_next_track': 0xB0, 'media_prev_track': 0xB1,
        'media_stop': 0xB2, 'media_play_pause': 0xB3, 'launch_mail': 0xB4,
        'launch_media_select': 0xB5, 'launch_app1': 0xB6, 'launch_app2': 0xB7
    }

    keybd_event = ctypes.windll.user32.keybd_event

    def keyboard(self, keys):
        for key in keys:
            action, key_name = key.split('_')
            vk = self.VK_CODE[key_name.lower()]
            if action == 'press':
                self.keybd_event(vk, 0, 0, 0)
            elif action == 'release':
                self.keybd_event(vk, 0, 2, 0)


    def mouse(self,location:list):
        pass

    # 示例使用
analogue_io = Analogue_IO()
analogue_io.keyboard(['press_shift', 'release_shift', 'press_d', 'release_d'])