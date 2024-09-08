
import cv2
import numpy as np

# 读取输入图像和模板图像
input_image = cv2.imread('../image/screen_catch/full-screen_1725770084.jpg', 0)
template_image = cv2.imread('../image/template/newqq_exit_but.png', 0)

# 获取模板的宽高
w, h = template_image.shape[::-1]

# 执行模板匹配
result = cv2.matchTemplate(input_image, template_image, cv2.TM_CCOEFF_NORMED)

# 设定一个阈值，匹配得分高于该值的区域被认为是匹配到目标
threshold = 0.8
loc = np.where(result >= threshold)

# 绘制匹配到的矩形框
for pt in zip(*loc[::-1]):
    cv2.rectangle(input_image, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)

# 显示结果
cv2.imshow('Detected', input_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
