import os
import urllib.parse


# ==========================================
# folder name for all the image on computer
image_folder = 'image'

# github image url base
github_base_url = 'https://raw.githubusercontent.com/1mmagg1e/ti84_calc_image/refs/heads/main/images/'

# name for output file
output_file = 'Image_Dictionary_For_Dify.txt'
# ==========================================

if not os.path.exists(image_folder):
    print(f" Can't find the folder：{image_folder}，please check route")
else:
    count = 0
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("<Image_Dictionary>\n")
        f.write(
            "(AI, strictly use these exact markdown links when referring to these buttons/menus)\n")

        # use os.walk go through all the files and sub files
        for root, dirs, files in os.walk(image_folder):
            # filter out all the image files
            images = [img for img in files if img.lower().endswith(('.png', '.jpg', '.jpeg'))]

            # create sub title if there is image in the folder
            if images:
                # filter folder name out
                category_name = os.path.basename(root)

                #
                if category_name == image_folder:
                    category_name = "General"

                # write in the title
                f.write(f"\n# {category_name}\n")
                print(f"\n# {category_name}")

                for filename in sorted(images):
                    count += 1
                    button_name = os.path.splitext(filename)[0]

                    # main idea：get the route for the image
                    # for example if file is in image/Main Buttons/MATH.png，
                    # then the route is Main Buttons/MATH.png
                    rel_path = os.path.relpath(os.path.join(root, filename), image_folder)

                    # replace the \ in windows to / in url
                    rel_path = rel_path.replace('\\', '/')

                    # correct coding (for example change space to "%20")
                    safe_rel_path = urllib.parse.quote(rel_path)
                    full_url = f"{github_base_url}{safe_rel_path}"

                    markdown_line = f"* {button_name}: ![{button_name}]({full_url})\n"
                    f.write(markdown_line)
                    print(markdown_line.strip())

        f.write("\n</Image_Dictionary>")

    print(f"\n Success！Have created {count} links in {output_file}.")
