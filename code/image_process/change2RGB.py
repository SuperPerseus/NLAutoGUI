from PIL import Image
import os

# 设置输入和输出目录
input_dir = r'H:\Project_Warehouse\NLAutoGUI\image\screen_catch'
output_dir = r'H:\Project_Warehouse\NLAutoGUI\image\screen_catch'

# 确保输出目录存在
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 遍历目录中的所有图片
for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        # 打开图片
        img_path = os.path.join(input_dir, filename)
        img = Image.open(img_path)

        # 检查图片模式并转换为 RGB
        if img.mode == 'RGBA':
            img = img.convert('RGB')

        # 保存转换后的图片
        new_filename = os.path.splitext(filename)[0] + '.jpg'
        img.save(os.path.join(output_dir, new_filename))

print("图片转换完成，已保存到指定目录。")
