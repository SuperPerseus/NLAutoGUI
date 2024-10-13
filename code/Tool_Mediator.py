import OCR
from CV import CV
from OCR import OCR
import analogue_IO
import time
import ast
import re
from screenshot import *

class Tool_Mediator:
    pic_file=""
    mission_hwnd=""
    def __init__(self, out_path, template_dir, ):
        self.tools_map = {
            """"mouse_action": MouseTool().mouse_action,
            "keyboard_action": KeyboardTool().keyboard_action,
            "OCR_action": OCR().OCR_action,
            "CV_action": CVTool().CV_action,"""
        }
        self.ocr = OCR(out_path)
        self.cv = CV(template_dir)
        self.mission_hwnd = 134390#暂时的测试用进程号

    def analy(self, order: str):
        split_pattern = r'[,()\s]+'
        order = re.split(split_pattern, order)
        action = order[0]
        if action == "mouse_action":
            print("yes")

        elif action == "keyboard_action":
            time.sleep(60)

        elif action == "OCR_action":
            img_path = self.screenshot_action()
            self.ocr.img_path = img_path
            self.ocr.do_ocr()

        elif action == "CV_action":
            img_path=self.screenshot_action()
            self.cv.img_path=img_path
            self.cv.do_cv()
    def screenshot_action(self):
        maximize_and_center(self.mission_hwnd)
        pic_file = screenshot(self.mission_hwnd)
        return pic_file


if __name__ == '__main__':
    out_path = "../image/result"
    template_dir = "../image/template"
    # while True:
    tool = Tool_Mediator(out_path, template_dir)
    tool.analy("OCR_action,NA,NA,NA")
