# Copyright (c) 2024 Subhashis Barad
# GitHub: https://github.com/Subhashis2007
# Licensed under the GNU General Public License v3.0 (GPLv3)

import re

def generate_urls_with_suffixes(input_url):
    pattern = re.compile(r'https://\w+\.cloudfront\.net/([\w-]+)/')
    
    match = pattern.search(input_url)
    
    if match:
        another_random_number = match.group(1)
        
        suffixes = ['240', '360', '480', '720']
        
        output_urls = [f'https://d26g5bnklkwsh4.cloudfront.net/{another_random_number}/hls/{resolution}/main.m3u8' for resolution in suffixes]
        
        return output_urls
    else:
        return None

user_input_url = input("Enter the complete URL: ")

results = generate_urls_with_suffixes(user_input_url)

if results:
    for resolution, result in zip(['240', '360', '480', '720'], results):
        print(f"URL for {resolution} video: {result}")
else:
    print("Invalid URL format. Please make sure the input URL follows the specified format.")

