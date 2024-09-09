from paddleocr import PaddleOCR, draw_ocr
from PIL import Image
import time
import json


class OCR:
    text_result = []
    img_path_result = ""
    json_string = ""

    def __init__(self, img_path):
        self.img_path = img_path
        self.ocr()
        self.ocr_results_to_json()

    def ocr(self):
        # Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
        # 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
        ocr = PaddleOCR(use_angle_cls=True, lang="ch", use_gpu=True)
        # need to run only once to download and load model into memory
        self.text_result = ocr.ocr(self.img_path, cls=True)

    def img_ocr(self):
        result = self.text_result[0]
        image = Image.open(self.img_path).convert('RGB')
        boxes = [line[0] for line in result]
        txts = [line[1][0] for line in result]
        scores = [line[1][1] for line in result]
        im_show = draw_ocr(image, boxes, txts, scores, font_path='ttf_store/simhei.ttf')
        im_show = Image.fromarray(im_show)
        im_show.save(f'../image/result/result{time.time()}.jpg')

    def ocr_results_to_json(self):
        # 初始化一个空列表，用于存储所有识别结果
        json_result = []
        # 遍历ocr.text_result中的每个元素
        for res in self.text_result:
            # 遍历每个识别结果中的每一行
            for line in res:
                # 解构元组，获取边界框和识别的文本及置信度
                bounding_box, (text, confidence) = line
                # 创建一个字典来存储当前行的信息
                json_line = {
                    "bounding_box": bounding_box,
                    "text": text,
                    "confidence": confidence
                }
                # 将字典添加到列表中
                json_result.append(json_line)

        # 将列表转换为JSON格式的字符串
        json_string = json.dumps(json_result, indent=2)
        self.json_string = json_string


if __name__ == '__main__':
    ocr = OCR("H:\Project_Warehouse\\NLAutoGUI\image\screen_catch\\full-screen_1725770084.png")
    print(ocr.json_string)
