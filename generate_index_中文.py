import os
import urllib.parse


# ================= 配置区 =================
# 1. 你本地存放图片的文件夹名字
image_folder = 'image'

# 2. 你的 GitHub Raw 链接的前缀（注意最后要保留斜杠 /）
github_base_url = 'https://raw.githubusercontent.com/1mmagg1e/IB-Math-calculator-Assistant/refs/heads/main/image/'

# 3. 最后生成的文本文件名
output_file = 'Image_Index.md'
# =========================================

# 检查图片文件夹是否存在
if not os.path.exists(image_folder):
    print(f"❌ 找不到文件夹：{image_folder}，请检查路径！")
else:
    # 打开（或创建）输出文件，准备写入
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# TI-84 视觉检索字典\n\n")  # 写入大标题

        count = 0
        # 遍历图片文件夹里的所有文件
        for filename in os.listdir(image_folder):
            # 只处理图片文件
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                count += 1

                # 提取按键名字
                button_name = os.path.splitext(filename)[0]

                # 安全处理文件名
                safe_filename = urllib.parse.quote(filename)
                full_url = f"{github_base_url}{safe_filename}"

                # 拼装出完美的 Markdown 代码行
                markdown_line = f"* **{button_name}**：![{button_name}]({full_url})\n\n"

                # 写进文件里
                f.write(markdown_line)

    print(f"✅ 大功告成！成功处理了 {count} 张图片。")
    print(f"📄 请在左侧项目面板查看生成的 {output_file} 文件。")
