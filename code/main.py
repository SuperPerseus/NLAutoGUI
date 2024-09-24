from NLP import NLP
from CV import CV
from maxize_program_window import maximize_and_center
from screenshot import screenshot
from OCR import OCR

if __name__ == '__main__':
    while True:
        mission = "清理QQ缓存"#(str(input("\n请输入任务命令:")))
        nlp = NLP(mission)
        mission_hwnd = nlp.NLP_find_mission()
        if mission_hwnd == -1:
            print("无法定位任务实体，请修改措辞再试一遍")
            continue
        """anaIO = analogue_IO()
        anaIO.win_D()"""
        maximize_and_center(mission_hwnd)
        pic_file = screenshot(mission_hwnd)
        ocr = OCR(pic_file,"../image/result")
        cv = CV(pic_file, "../image/template")
        matched_dic = cv.matched_positions

