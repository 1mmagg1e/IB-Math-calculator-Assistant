import os
import urllib.parse


# ==================================

### In terminal window enter "pip install python-docx"
# 1. file store alll the image 你本地存放图片的文件夹名字
image_folder = 'image'

# 2. Git hub Raw link pres, GitHub Raw 链接的前缀（注意最后要保留斜杠 /）
github_base_url = 'https://raw.githubusercontent.com/1mmagg1e/ti84_calc_image/refs/heads/main/images/'

# 3. The final name for the files 最后生成的文本文件名
output_file = 'Image_Index.md'
# =========================================

# Check if the iamge folder exist or not 检查图片文件夹是否存在
if not os.path.exists(image_folder):
    print(f"❌ fail find file：{image_folder}，please check route！")
else:
    # 打开（或创建）输出文件，准备写入
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# TI-84 visual search dictionary\n\n")  # 写入大标题

        count = 0
        # run through all the images in the file 遍历图片文件夹里的所有文件
        for filename in os.listdir(image_folder):
            # only the image file only 只处理图片文件
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                count += 1

                # extract the name 提取按键名字
                button_name = os.path.splitext(filename)[0]

                # 安全处理文件名
                safe_filename = urllib.parse.quote(filename)
                full_url = f"{github_base_url}{safe_filename}"

                # 拼装出完美的 Markdown 代码行
                # 使用 ### 定义 Parent Chunk，下方的图片自动成为 Child Chunk
                markdown_line = f"### {button_name}\n![{button_name}]({full_url})\n\n"

                # 写进文件里
                f.write(markdown_line)

    print(f"✅ Finished! Successfully generate index for {count} of image files.")
    print(f"📄 Please check {output_file} file on the left side in menu bar.")
