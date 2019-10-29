import requests
from lxml import etree

site_domain = 'http://www.lg.gov.cn/xxgk/xwzx/zwdt/'


def get_all_articles():
    for x in range(1, 37):
        url = 'http://www.lg.gov.cn/xxgk/xwzx/zwdt/index_%s.htm' % x
        resp = requests.get(url)
        text = resp.text
        html = etree.HTML(text)
        if x < 25:
            lis = html.xpath('//ul[@class="common-list"]/li')
            for li in lis:
                href = li.xpath('./a/@href')[0]
                full_href = site_domain + href[2:]
                get_page_content(x, full_href)
                #     break
                # break
        else:
            lis = html.xpath('//div[@class="list-r"]/ul/li')
            for li in lis:
                href = li.xpath('./a/@href')[0]
                full_href = site_domain + href[2:]
                get_page_content_after_24(x, full_href)


def get_page_content(page, url):
    resp = requests.get(url)
    text = resp.content.decode('utf-8')
    # print(text)
    html = etree.HTML(text)
    content = ''.join(map(lambda x: x.rstrip('\u3000\u3000').strip(), html.xpath('//div[@class="TRS_Editor"]/p//text()')))
    print(page, url, content)
    print()
    with open('lg_gov.txt', 'a', encoding='utf-8') as f:
        f.write(content)
        # print(url)


def get_page_content_after_24(page, url):
    resp = requests.get(url)
    text = resp.content.decode('utf-8')
    # print(text)
    html = etree.HTML(text)
    content = ''.join(map(lambda x: x.rstrip('\u3000\u3000').strip(), html.xpath('//div[@class="nr-zw"]/p//text()')))
    print(page, url, content)
    print()
    with open('lg_gov.txt', 'a', encoding='utf-8') as f:
        f.write(content)
        # print(url)


if __name__ == '__main__':
    get_all_articles()
