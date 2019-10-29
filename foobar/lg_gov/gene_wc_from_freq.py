from collections import Counter
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt  # 绘制图像的模块

pat = r'更新|整治|利益统筹|拆除重建|治理|战略|先行|整备|建设|教育|医疗|文化|体育|文体|儿童|养老|老年|高等教育|创新|科技|产业|人口|制造业|服务业'

with open('lg_gov.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    match_res = re.findall(pat, text)
    counter = Counter(match_res)

wc = WordCloud(font_path="C:/Windows/Fonts/simsun.ttc")

wc.generate_from_frequencies(counter)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()