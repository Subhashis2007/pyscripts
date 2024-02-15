# Copyright (c) 2024 Subhashis Barad
# GitHub: https://github.com/Subhashis2007
# Licensed under the GNU General Public License v3.0 (GPLv3)

def get_color_input(color_name):
    color_input = input(f"Enter color for {color_name} (e.g., #123456): ")
    return color_input

color_names = [
    "Color00",
    "Color01",
    "Color02",
    "Color03",
    "Color04",
    "Color05",
    "Color06",
    "Color07",
    "Color08"
]

user_colors = []

for color_name in color_names:
    color = get_color_input(color_name)
    user_colors.append([color, color])

code_block = "[\n"
for color in user_colors:
    code_block += f'    ["{color[0]}", "{color[1]}"], # {color_names[user_colors.index(color)]}\n'
code_block += "]\n"

print("\nThe generated code block is:")
print(code_block)

