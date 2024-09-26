from CV import CV
from NLP import NLP
from OCR import OCR
from Tool_Mediator import Tool_Mediator
from maxize_program_window import maximize_and_center
from screenshot import screenshot

if __name__ == '__main__':
    out_path = "../image/result"
    template_dir = "../image/template"
    # while True:
    tool = Tool_Mediator(out_path, template_dir)
    mission = "清理QQ缓存"  # (str(input("\n请输入任务命令:")))
    nlp = NLP(mission, tool)
    mission_hwnd = nlp.NLP_find_mission()
    """if mission_hwnd == -1:
        print("无法定位任务实体，请修改措辞再试一遍")
        continue"""
    """anaIO = analogue_IO()
    anaIO.win_D()"""
    maximize_and_center(mission_hwnd)
    pic_file = screenshot(mission_hwnd)
    ocr = OCR(pic_file, out_path)
    cv = CV(pic_file, template_dir)
    matched_dic = cv.matched_positions

    nlp.NLP_do_mission()
