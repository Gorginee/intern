import jieba  # 分词函数
from scipy.misc import imread  # 这是一个处理图像的函数
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt  # 分析数据的函数

file_apath = open('tlbb.txt', 'r', encoding='gbk', errors='ignore').read()  # 打开文件
# bg_pic = imread('map.jpg')  # 图片路径

# 王语嫣, 慕容复, 木婉清, 游坦之, 鸠摩智, 段延庆,包不同, 丁春秋, 阿紫, 阿朱, 段正淳, 钟万洪, 风波恶, 天山童姥, 耶律洪基...........

jieba.add_word('乔峰')  # 添加关键词
jieba.add_word('段誉')
jieba.add_word('虚竹')
jieba.add_word('王语嫣')
jieba.add_word('慕容复')
jieba.add_word('木婉清')
jieba.add_word('段正淳')
jieba.add_word('鸠摩智')
jieba.add_word('游坦之')
jieba.add_word('包不同')
jieba.add_word('钟万洪')
jieba.add_word('耶律洪基')
jieba.add_word('萧峰')
jieba.add_word('南海恶神')
jieba.add_word('阿朱')
jieba.add_word('钟灵')
jieba.add_word('阿碧')
jieba.add_word('阿紫')
jieba.add_word('玄慈')

wordlist_jieba = jieba.cut(file_apath, cut_all=True)  # 使用jieba分词

world_split = " ".join(wordlist_jieba)  # 分词后的数据

my_wordcloud = WordCloud(background_color='white',  # 设置背景色
                          margin=2,  # 图片的宽,高,和边距
                         # mask=bg_pic,  # 设置背景图片
                         font_path="C:/Windows/Fonts/simsun.ttc",  # 设置字体路径
                         # random_state=42,
                         )
# 屏蔽关键词
STOPWORDS.add('自己')
STOPWORDS.add('说道')
STOPWORDS.add('什么')
STOPWORDS.add('他们')
STOPWORDS.add('一个')
STOPWORDS.add('不是')
STOPWORDS.add('便是')
STOPWORDS.add('甚么')
STOPWORDS.add('不知')
STOPWORDS.add('咱们')
STOPWORDS.add('我们')
STOPWORDS.add('可是')
STOPWORDS.add('只是')
STOPWORDS.add('如此')
STOPWORDS.add('这些')
STOPWORDS.add('倘若')
STOPWORDS.add('怎么')
STOPWORDS.add('这么')

my_wordcloud.generate(world_split)  # 生成词云
# image_colors = ImageColorGenerator(bg_pic)  # 转换字体主题色与图片一致
# 绘制词云
plt.figure()
plt.imshow(my_wordcloud.recolor())
plt.title('Word Cloud')  # 词云标题
plt.axis("off")  # 关闭词云
plt.show()  # 显示生成的词云图片
my_wordcloud.to_file('ciyun.png')  # 保存图片
