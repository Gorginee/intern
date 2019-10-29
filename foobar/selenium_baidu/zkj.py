import time
import requests
from lxml import etree
from selenium import webdriver


def simulate():
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    driver.find_element_by_id('kw').send_keys('UiBot')
    driver.find_element_by_id('su').click()
    time.sleep(0.5)
    page_source = driver.page_source
    write(page_source)
    driver.quit()


def write(page_source):
    html = etree.HTML(page_source)
    div = list(filter(lambda x: x.xpath('./child::h3'), html.xpath('.//div[@id="content_left"]/div')))[3]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'
    }
    href = div.xpath('./h3/a/@href')[0]
    with open('res.txt', 'w', encoding='utf-8') as f:
        f.write(requests.get(href, headers=headers).text)


if __name__ == '__main__':
    simulate()