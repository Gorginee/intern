import time
import random
import requests
from lxml import etree


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Referer': 'http://www.dianping.com/shop/69489452/review_all/',
    'Cookie': 'cy=7; cye=shenzhen; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=16df2278e9ac8-02cbec49fff6f1-6b131a7b-1fa400-16df2278e9ac8; _lxsdk=16df2278e9ac8-02cbec49fff6f1-6b131a7b-1fa400-16df2278e9ac8; _hc.v=07799b7f-0c9b-42d0-3415-7667fafe91d9.1571725742; s_ViewType=10; dper=3c1f829b5f10261ba374887f6e73465e543b2bf11370c0dd93913d7b04724a1b27efe107af27886f2aca414b55311246e93dac52b51f2107ca3dbff458dd41ae43ad7a6c833e41c680ecac41d3de35d9bac4687a216a0636fc3d92645594d559; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_9756187615; ctu=4bb4448d029cdcd890155707d47794e900060f47dd0372933bde6ef7e9dd3f82; uamo=18711867523; _lxsdk_s=16df2278e9b-ce8-231-e52%7C%7C491'
}


def get_comment_by_page(shop_id, page_num):
    url = f'http://www.dianping.com/shop/{shop_id}/review_all/p{page_num}'
    resp = requests.get(url, headers=headers, proxies={'https': 'https://60.190.250.120:8080'})
    print(resp.status_code)
    text = resp.text
    html = etree.HTML(text)
    scores = html.xpath('//span[@class="score"]')
    for score in scores:
        if len(score.xpath('./span')) == 5:
            print(score.xpath('./span[last()]/text()'))


if __name__ == '__main__':
    for x in range(1, 307):
        get_comment_by_page('69489452', x)
        time.sleep(random.random())
