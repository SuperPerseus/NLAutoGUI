import json

import OCR
from CV import CV
from OCR import OCR
from analogue_IO import Analogue_IO
import time
import ast
import re
from screenshot import *
import json

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
        self.io= Analogue_IO()

    def analy(self, order:str):
        order=json.loads(order)
        action = order["action"]
        if action == "mouse_action":
            str_list = order["mouse_list"].replace('(', '[').replace(')', ']')
            str_list = json.loads(str_list)
            self.io.mouse(str_list,bool(order["mouse_slide_mode"]))

        elif action == "keyboard_action":
            str_list=order["keyboard_list"][1:-1]
            str_list = str_list.split(",")
            self.io.keyboard(str_list)

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
    """testjson={
        "action":"mouse_action",
        "mouse_list":"[(2560, 10)]",
        "mouse_slide_mode":"False",
        "keyboard_list":"NA"
    }"""
    testjson = {
        "action": "keyboard_action",
        "mouse_list": "NA",
        "mouse_slide_mode": "NA",
        "keyboard_list": "[press-CTRL,press-A,release-CTRL,release-A]"
    }
    json_string=json.dumps(testjson)
    tool.analy(json_string)
