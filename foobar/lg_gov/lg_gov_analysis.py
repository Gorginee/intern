import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt  # 绘制图像的模块

path_txt = './lg_gov.txt'
f = open(path_txt, 'r', encoding='UTF-8').read()

# 24
dev_kw_pat = r'更新|整治|利益统筹|拆除重建|治理|战略|先行|整备|建设|教育|医疗|文化|体育|文体|儿童|养老|老年|高等教育|创新|科技|产业|人口|制造业|服务业'
# 22
place_kw_pat = r'平湖街道|横岗街道|龙岗街道|龙城街道|坪地街道|布吉街道|南湾街道|坂田街道|吉华街道|圆山街道|宝龙街道|龙岗河|大运|龙园|龙西|五联|云创|甘坑|坂雪岗|华为|比亚迪|低碳城'

dev_kws = re.findall(dev_kw_pat, f)
# dev_kws = re.findall(place_kw_pat, f)


cut_text = " ".join(dev_kws)

word_cloud = WordCloud(
    font_path="C:/Windows/Fonts/simfang.ttf",
    background_color="white", width=1000, height=880,
    max_words=20,
    collocations=False
).generate(cut_text)

plt.imshow(word_cloud, interpolation="bilinear")
plt.axis("off")
plt.show()
