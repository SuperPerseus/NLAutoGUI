import os
import numpy as np
from PIL import Image, ImageFilter
import shutil

# 设置输入和输出目录
input_dir = r'C:\Users\ASUS\Desktop\project\pic'
output_dir = r'C:\Users\ASUS\Desktop\project\salted'
label_dir = r'C:\Users\ASUS\Desktop\project\labels'  # 假设标注文件存放在这个目录
salted_label_dir = r'C:\Users\ASUS\Desktop\project\salted_labels'  # 保存加盐后的标注文件

# 确保输出目录存在
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
if not os.path.exists(salted_label_dir):
    os.makedirs(salted_label_dir)


# 椒盐噪声函数
def salt_and_pepper_noise(image, prob):
    output = np.copy(image)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = np.random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
    return output


# 中度椒盐噪声函数
def moderate_salt_and_pepper_noise(image, prob):
    output = np.copy(image)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = np.random.random()
            if rdn < prob:
                output[i][j] = np.random.choice([0, 255])  # 随机选择黑点或白点
    return output


# 彩色椒盐噪声函数
def color_salt_and_pepper_noise(image, prob):
    output = np.copy(image)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = np.random.random()
            if rdn < prob:
                output[i][j] = [np.random.choice([0, 255]),
                                np.random.choice([0, 255]),
                                np.random.choice([0, 255])]
    return output


# 遍历目录中的所有图片并进行处理
for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        # 使用PIL读取图片
        img_path = os.path.join(input_dir, filename)
        try:
            img = Image.open(img_path)
            # 确保图片是RGB模式
            if img.mode != 'RGB':
                img = img.convert('RGB')
        except IOError:
            print(f"Failed to load image: {img_path}")
            continue

        # 将图片转换为 numpy 数组
        img_np = np.array(img)

        # 添加椒盐噪声
        noisy_salt_pepper = salt_and_pepper_noise(img_np, prob=0.05)
        salted_img_path = os.path.join(output_dir, f'sp_{filename}')
        Image.fromarray(noisy_salt_pepper).save(salted_img_path)

        # 添加中度椒盐噪声
        noisy_moderate_sp = moderate_salt_and_pepper_noise(img_np, prob=0.05)
        moderate_salted_img_path = os.path.join(output_dir, f'moderate_sp_{filename}')
        Image.fromarray(noisy_moderate_sp).save(moderate_salted_img_path)

        # 添加彩色椒盐噪声
        noisy_color_sp = color_salt_and_pepper_noise(img_np, prob=0.05)
        color_salted_img_path = os.path.join(output_dir, f'color_sp_{filename}')
        Image.fromarray(noisy_color_sp).save(color_salted_img_path)

        # 如果原始图片有对应的标注文件，则复制并重命名标注文件
        label_file = os.path.join(label_dir, filename.replace('.jpg', '.txt'))
        if os.path.exists(label_file):
            salted_label_file = os.path.join(salted_label_dir, f'sp_{filename.replace(".jpg", ".txt")}')
            shutil.copy(label_file, salted_label_file)

            moderate_salted_label_file = os.path.join(salted_label_dir,
                                                      f'moderate_sp_{filename.replace(".jpg", ".txt")}')
            shutil.copy(label_file, moderate_salted_label_file)

            color_salted_label_file = os.path.join(salted_label_dir, f'color_sp_{filename.replace(".jpg", ".txt")}')
            shutil.copy(label_file, color_salted_label_file)

print("图片和标注文件处理完成，已保存到指定目录。")
