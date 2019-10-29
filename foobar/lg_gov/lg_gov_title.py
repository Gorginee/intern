import requests
from lxml import etree

site_domain = 'http://www.lg.gov.cn/xxgk/xwzx/zwdt/'


def get_all_articles(to_file):
    for x in range(1, 37):
        url = 'http://www.lg.gov.cn/xxgk/xwzx/zwdt/index_%s.htm' % x
        html = etree.HTML(requests.get(url).content.decode('UTF-8'))
        if x < 25:
            lis = html.xpath('//ul[@class="common-list"]/li')
            for li in lis:
                title = li.xpath('./a/text()')[0]
                print(title)
                with open(to_file, 'a', encoding='utf-8') as f:
                    f.write(title)
        else:
            lis = html.xpath('//div[@class="list-r"]/ul/li')
            for li in lis:
                title = li.xpath('./a/h2/text()')[0]
                print(title)
                with open(to_file, 'a', encoding='utf-8') as f:
                    f.write(title)


if __name__ == '__main__':
    get_all_articles('lg_gov_title_2.txt')
