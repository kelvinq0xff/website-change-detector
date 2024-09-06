from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time as t
import os
import re
from redlines import Redlines
import datetime as dt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file", default='urls.txt', help="The urls file name")
parser.add_argument("--wait", default=10, type=int, help="Time to wait for loading the website content")
args = parser.parse_args()

assert args.file in os.listdir('.')
assert args.wait >= 0

def check_website(driver, url, wait):
    driver.get(url)
    t.sleep(wait)
    text = driver.find_element(By.TAG_NAME, 'body').text
    return str(re.sub(r'\s+', ' ', text))


def load_website(url):
    fpath = os.path.join('website_log', re.sub(r'[:*?"<>|/\\]', '', url) + '.txt')
    try:
        with open(fpath, encoding='utf-8') as f:
            fr = f.read()
    except:
        return ''
    return fr


def compare_website(c1, c2):
    return re.sub(r'\s+', '', c1) != re.sub(r'\s+', '', c2)


def save_website(url, content):
    fpath = os.path.join('website_log', re.sub(r'[:*?"<>|/\\]', '', url) + '.txt')
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

with open(args.file, encoding='utf-8') as f:
    URLS = f.read().split('\n')
WAIT = args.wait

if not os.path.exists(f'result-{dt.date.today()}.html'):
	result = open(f'result-{dt.date.today()}.html', 'w', encoding='utf-8')
	result.write('<div style="font-family: Consolas; font-size:xx-large;">')
	result.close()

result = open(f'result-{dt.date.today()}.html', 'a', encoding='utf-8')

for i, url in enumerate(URLS):
    if not os.path.exists('website_log'):
        os.mkdir('website_log')
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    c1 = check_website(driver, url, wait=WAIT)
    c2 = load_website(url)
    if compare_website(c1, c2):
        diff_html = Redlines(c2, c1).output_markdown
        diff_html = diff_html.replace('color:green;font-weight:700;', 'background-color:yellow;')
        result.write(f'''<a href="{url}"><h2 style="background-color: yellow; white-space:nowrap;">{i+1}. {url}</h2></a>{diff_html}''')
        save_website(url, c1)

result.write('</div>')
result.close()
driver.quit()
