import re
from pyecharts import Pie
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt


class FocusRatioChart:
    def __init__(self, category=None):
        self.pat = None
        self.category = category
        self.file_path = './lg_gov_title_1.txt'
        if self.category == 'dev':
            self.pat = r'更新|整治|利益统筹|拆除重建|治理|战略|先行|整备|建设|教育|医疗|文化|体育|文体|儿童|养老|老年|高等教育|创新|科技|产业|人口|制造业|服务业'
        else:
            self.pat = r'平湖|横岗|龙岗街道|龙城|坪地|布吉|南湾|坂田|吉华|圆山|宝龙|龙岗河|大运|龙园|龙西|五联|云创|甘坑|坂雪岗|华为|比亚迪|低碳城'

    def gene_pie_chart(self, width='1000', height='600', title="", output=None, **kwargs):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            res = re.findall(self.pat, f.read())
            count_dict = Counter(res)
        if not title:
            title = '发展关注占比' if self.category == 'dev' else '地区关注占比'
        attr, value = count_dict.keys(), count_dict.values()
        pie = Pie(title=title,
                  width=width,
                  height=height,
                  subtitle='',
                  title_pos="center",
                  title_top="95%",
                  title_color="#000",
                  subtitle_color="#aaa",
                  title_text_size=18,
                  subtitle_text_size=12,
                  background_color="#fff",
                  is_grid=False
                  )

        pie.add("", attr, value, is_label_show=True, center=['50%', '55%'])
        # pie.show_config()
        pie.render(path=output or (title + '.html'))

    def gene_word_cloud(self, **kwargs):
        f = open(self.file_path, 'r', encoding='UTF-8').read()
        kws = re.findall(self.pat, f)
        counter = Counter(kws)

        word_cloud = WordCloud(
            font_path="C:/Windows/Fonts/simsun.ttc",
            **kwargs
            # background_color="white",
            # min_font_size=6,
            # width=1000,
            # height=880,
            # max_words=max_words
        )
        word_cloud.generate_from_frequencies(counter)
        plt.imshow(word_cloud, interpolation="bilinear")
        plt.axis("off")
        word_cloud.to_file('res_title_1.png')
        plt.show()


if __name__ == '__main__':
    frc = FocusRatioChart()
    # frc.gene_pie_chart()
    frc.gene_word_cloud(background_color="white")