import os
import urllib.parse


# ==========================================
# 1. 你的本地图片文件夹名称
image_folder = 'image'

# 2. GitHub Raw 链接前缀 (严格保留最后的斜杠)
github_base_url = 'https://raw.githubusercontent.com/1mmagg1e/ti84_calc_image/refs/heads/main/images/'

# 3. 生成的文本文件名
output_file = 'Image_Dictionary_For_Dify.txt'
# ==========================================

if not os.path.exists(image_folder):
    print(f"❌ 找不到文件夹：{image_folder}，请检查路径！")
else:
    count = 0
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("<Image_Dictionary>\n")
        f.write(
            "(AI, strictly use these exact markdown links when referring to these buttons/menus)\n")

        # 使用 os.walk 遍历主文件夹及其所有子文件夹
        for root, dirs, files in os.walk(image_folder):
            # 过滤出当前层级的图片文件
            images = [img for img in files if img.lower().endswith(('.png', '.jpg', '.jpeg'))]

            # 如果当前文件夹里有图片，才生成一个分类标题
            if images:
                # 提取当前文件夹的名字
                category_name = os.path.basename(root)

                # 如果是在 image 根目录的图片，给个默认名字
                if category_name == image_folder:
                    category_name = "General"

                # 写入分类大标题
                f.write(f"\n# {category_name}\n")
                print(f"\n# {category_name}")

                for filename in sorted(images):
                    count += 1
                    button_name = os.path.splitext(filename)[0]

                    # 核心逻辑：获取图片的相对路径
                    # 比如文件在 image/Main Buttons/MATH.png，相对路径就是 Main Buttons/MATH.png
                    rel_path = os.path.relpath(os.path.join(root, filename), image_folder)

                    # 将 Windows 的反斜杠 \ 替换为 URL 的正斜杠 /
                    rel_path = rel_path.replace('\\', '/')

                    # 安全编码（比如把文件夹或文件名的空格变成 %20）
                    safe_rel_path = urllib.parse.quote(rel_path)
                    full_url = f"{github_base_url}{safe_rel_path}"

                    markdown_line = f"* {button_name}: ![{button_name}]({full_url})\n"
                    f.write(markdown_line)
                    print(markdown_line.strip())

        f.write("\n</Image_Dictionary>")

    print(f"\n✅ 成功！已在 {output_file} 中按文件夹生成了 {count} 条分类链接。")
