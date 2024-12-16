import os
import shutil
from PIL import Image


def convert_and_resize_images(target_width=800, quality=85, temp_dir='F:\\临时图片'):
    # 检查临时目录是否存在，不存在则创建
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    # 获取当前文件夹下所有的文件
    for filename in os.listdir('.'):
        # 支持转换webp等非jpg格式图片
        if filename.lower().endswith(('png', 'jpeg', 'bmp', 'gif', 'webp')) and not filename.lower().endswith('jpg'):
            try:
                img = Image.open(filename)
                rgb_img = img.convert('RGB')  # 将图片转换为RGB格式以保存为JPG
                new_filename = os.path.splitext(filename)[0] + '.jpg'
                rgb_img.save(new_filename, 'JPEG', quality=quality)
                print(f"{filename} 已转换为 {new_filename}")
                # 移动原始非jpg文件到临时目录
                shutil.move(filename, os.path.join(temp_dir, filename))
                print(f"原文件 {filename} 已移动到 {temp_dir}")
            except Exception as e:
                print(f"转换 {filename} 失败: {e}")

    # 处理所有jpg格式的图片，调整大小并压缩
    for filename in os.listdir('.'):
        if filename.lower().endswith('jpg'):
            try:
                img = Image.open(filename)
                width, height = img.size
                # 计算新的高度以保持纵横比
                aspect_ratio = height / width
                new_height = int(target_width * aspect_ratio)
                # 调整图片尺寸
                resized_img = img.resize((target_width, new_height), Image.Resampling.LANCZOS)
                # 保存图片，尽量压缩图片体积但保持质量
                resized_img.save(filename, 'JPEG', quality=quality, optimize=True)
                print(f"{filename} 已调整宽度为 {target_width} 且压缩完成")
            except Exception as e:
                print(f"调整 {filename} 尺寸失败: {e}")


if __name__ == "__main__":
    convert_and_resize_images()
