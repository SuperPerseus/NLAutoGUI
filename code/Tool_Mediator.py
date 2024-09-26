import OCR
import CV
import analogue_IO


class Tool_Mediator:
    out_path = ""
    template_dir = ""

    def __init__(self, out_path, template_dir, ):
        self.out_path = out_path
        self.template_dir = template_dir
        self.tools_map = {


            """"mouse_action": MouseTool().mouse_action,
            "keyboard_action": KeyboardTool().keyboard_action,
            "OCR_action": OCR().OCR_action,
            "CV_action": CVTool().CV_action,"""
        }

    def analy(self, order: str):
        if order == "mouse_action":
            pass
        elif order == "keyboard_action":
            pass
        elif order == "OCR_action":
            pass
        elif order == "CV_action":
            pass
