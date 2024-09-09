import cv2
import numpy as np
from PIL import Image
import json


class CV:
    # 类变量，存储模板匹配到的元素的坐标
    matched_positions = {}

    def __init__(self, img_path, template_path):
        self.img_path = img_path
        self.template_path = template_path
        self.img = None
        self.templ = None
        self.load_images()

    def load_images(self):
        # 移除PNG图像中的iCCP块
        self.fix_image_srgb_profile(self.img_path)
        self.fix_image_srgb_profile(self.template_path)

        # 读取待识别图片和模板
        self.img = cv2.imread(self.img_path)
        self.templ = cv2.imread(self.template_path)

    @staticmethod
    def fix_image_srgb_profile(file_path):
        img = Image.open(file_path)
        img.save(file_path, icc_profile=None)

    def match_template(self, threshold=0.99):
        # 获取模板图像的尺寸
        height, width, _ = self.templ.shape

        # 进行模板匹配
        results = cv2.matchTemplate(self.img, self.templ, cv2.TM_CCOEFF_NORMED)

        # 存储模板匹配到的元素的坐标
        CV.matched_positions[self.template_path] = []

        # 找到匹配度较高的区域
        locations = np.where(results >= threshold)
        for pt in zip(*locations[::-1]):
            x, y = map(int, pt)  # 转换为标准 Python int
            # 计算矩形的四个顶点坐标并转换为 Python 的 int 类型
            rect = {
                "top_left": (int(x), int(y)),
                "top_right": (int(x + width), int(y)),
                "bottom_left": (int(x), int(y + height)),
                "bottom_right": (int(x + width), int(y + height))
            }
            CV.matched_positions[self.template_path].append(rect)
            # 在原图上绘制矩形框
            cv2.rectangle(self.img, (x, y), (x + width, y + height), (0, 0, 255), 2)

        return self.img

    def display_result(self):
        cv2.imshow("Matched Result", self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def save_result(self, output_path):
        cv2.imwrite(output_path, self.img)

    @staticmethod
    def save_positions_to_json(output_path):
        # 将匹配到的坐标字典保存为 JSON 文件
        with open(output_path, 'w') as f:
            json.dump(CV.matched_positions, f, indent=4)


# 使用示例
img_path = "../image/screen_catch/full-screen_1725770084.jpg"
template_path = "../image/template/newqq_mainsetting_but.png"

matcher = CV(img_path, template_path)
matched_img = matcher.match_template()
matcher.save_result("../image/matched_result.jpg")

# 保存匹配到的坐标为 JSON 文件
CV.save_positions_to_json("../image/matched_positions.json")

# 打印匹配到的坐标
print(CV.matched_positions)