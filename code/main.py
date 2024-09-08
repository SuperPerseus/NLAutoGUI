from NLP import NLP_find_mission
from analogue_IO import analogue_IO
from maxize_program_window import maximize_and_center
from screenshot import screenshot
from OCR import OCR

if __name__ == '__main__':
    while True:
        mission = str(input("请输入任务命令"))
        mission_hwnd = NLP_find_mission(mission)
        if mission_hwnd == -1:
            print("无法定位任务实体，请修改措辞再试一遍")
            continue
        """anaIO = analogue_IO()
        anaIO.win_D()"""
        maximize_and_center(mission_hwnd)
        pic_file=screenshot(mission_hwnd)
        ocr=OCR(pic_file)


