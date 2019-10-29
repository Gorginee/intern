import re
from pyecharts import Pie
from collections import Counter

# 24 发展
kw_pat = r'更新|整治|利益统筹|拆除重建|治理|战略|先行|整备|建设|教育|医疗|文化|体育|文体|儿童|养老|老年|高等教育|创新|科技|产业|人口|制造业|服务业'
# 22 地点
# kw_pat = r'平湖街道|横岗街道|龙岗街道|龙城街道|坪地街道|布吉街道|南湾街道|坂田街道|吉华街道|圆山街道|宝龙街道|龙岗河|大运|龙园|龙西|五联|云创|甘坑|坂雪岗|华为|比亚迪|低碳城'

title = '龙岗区地点关注占比' if kw_pat.startswith('平湖街道') else '龙岗区发展关注占比'

with open('lg_gov.txt', 'r', encoding='utf-8') as f:
    res = re.findall(kw_pat, f.read())
    count_dict = Counter(res)


attr, value = count_dict.keys(), count_dict.values()
pie = Pie(title=title,
          width='1000',
          height='600',
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
pie.show_config()
pie.render(path=title + '.html')
