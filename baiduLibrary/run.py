import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Mobile Safari/537.36'
}

resp = requests.get('https://wenku.baidu.com/view/27302dea50e79b89680203d8ce2f0066f53364e8.html', headers=headers).content.decode('utf-8')

html = etree.HTML(resp)

paras = html.xpath('//div[@class="rtcspage"]/div/p')

for para in paras:
    spans = para.xpath('./span')
    # print(spans)
    print(''.join([span.text or '' for span in spans]))
    # for span in spans:
    #     span_text = span.text
    #     print(span_text)
