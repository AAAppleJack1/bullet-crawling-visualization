import re  # 实现正则表达式的操作
import jieba  # 中文分词库
import wordcloud  # 词云展示库
import numpy as np  # 科学计算基础库，整理数据
import matplotlib.pyplot as plt  # 绘图库 绘制2D图表
from PIL import Image  # 基础图像处理库  导入展示图片

jieba.load_userdict('cast1.txt')  # 保留嘉宾名字
jieba.load_userdict('cast2.txt')

# 读取文件并生成列表
def get_words():
    f = open('danmu.txt', 'r', encoding="utf-8")
    file = f.read()
    f.close()

    # 文本预处理
    pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"')  # 定义正则表达式匹配模式
    file = re.sub(pattern, '', file)  # 将符合模式的字符去除

    # 对文本进行分词
    string = jieba.lcut(file)  # jieba精确模式分词

    # 去除emoji和无意义词汇
    string = [word for word in string if len(word) > 1]  # 去除单个字符，包括emoji
    # 设置停用词
    with open('stopword.txt', 'r', encoding='utf-8') as s:
        stopwords = s.read()
    # 去除出现频率高但无实际意义的词汇，如“还是”、“那么”等连词
    string_split = []
    for word in string:
        if word not in stopwords:
            string_split.append(word)

    return string_split


# 统计词频并降序排序
def count(string_split):
    counts = {}  # 字典存放“词汇：出现次数”键值对

    # 修改昵称并统计词汇出现次数
    for word in string_split:
        if word == "ella" or word == "Ella" or word == "ELLA":
            cword = "陈嘉桦"
        elif word == "叉烧芬" or word == "娘娘":
            cword = "蔡少芬"
        elif word == "老龚" or word == "龚老师":
            cword = "龚琳娜"
        elif word == "悦姐":
            cword == "孙悦"
        elif word == "艾莉" or word == "艾丽":
            cword = "李彩桦"
        elif word == "品如" or word == "秋秋":
            cword = "秋瓷炫"
        elif word == "娜娜" or word == "娜姐":
            cword = "谢娜"
        elif word == "Alin" or word == "A-Lin" or word == "alin" or word == "房腻宁":
            cword = "黄丽玲"
        elif word == "珠珠":
            cword == "朱珠"
        elif word == "惜君":
            cword = "刘惜君"
        elif word == "欣欣":
            word == "谢欣"
        elif word == "小美" or word == "Maria":
            cword = "美依礼芽"
        elif word == "雅瑟" or word == "瑟姐" or word == "亚瑟":
            cword = "刘雅瑟"
        elif word == "yuki" or word == "Yuki":
            cword = "徐怀钰"
        elif word == "amber" or word == "a殿" or word == "A殿" or word == "刘逸云" or word == "berber":
            cword = "Amber"
        elif word == "Chipu" or word == "chipu":
            cword = "芝芙"
        elif word == "嘉倪":
            cword == "张嘉倪"
        elif word == "叨叨" or word == "丽娜":
            cword = "赵丽娜"
        elif word == "小敏":
            cword = "汪小敏"
        elif word == "倩倩":
            cword = "吴倩"
        elif word == "可妮":
            cword = "曾可妮"
        elif word == "李莎":
            cword = "李莎旻子"
        elif word == "凯丽":
            cword = "卡捷琳娜"
        elif word == "艺兴" or word == "lay" or word == "Lay":
            cword == "张艺兴"
        elif word == "Jessica" or word == "卡姐":
            cword == "郑秀妍"
        else:
            cword = word
        counts[cword] = counts.get(cword, 0) + 1  # 若字典中没有该词汇则创建键值对，有则值+1
        # 将“词汇：次数”存入counts

    # 按值降序排序并返回字典
    items = list(counts.items())  # 先将键值对转换为可排序的列表
    items.sort(key=lambda x: x[1], reverse=True)
    # lambda函数，指定每个元素的第二个部分是一个字典，reverse=True反向（降序）顺序
    descount = dict(items)  # 再将排序后的列表转回字典
    print(descount)
    return descount


# 生成词云
def draw_cloud(descount):
    mask = np.array(Image.open('乘风.jpg'))  # 定义背景图   # 图像的数组表示

    # 设置词云背景图、背景颜色、字体、显示词数、字体大小
    wc = wordcloud.WordCloud(
        mask=mask,
        background_color='white',
        font_path='simkai.ttf',
        max_words=300,
        max_font_size=80,
        min_font_size=9,
    )

    # 展示词云
    wc.generate_from_frequencies(descount)  # 从字典生成词云
    plt.figure(figsize=(8, 5), dpi=80)  # 设置屏幕大小
    plt.imshow(wc)  # 显示词云
    plt.axis('off')  # 关闭坐标轴
    plt.show()


def main():
    string_split = get_words()
    # print(string_split)——测试
    dict = count(string_split)
    draw_cloud(dict)


if __name__ == '__main__':
    main()


