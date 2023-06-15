import numpy as np
import matplotlib.pyplot as plt
import 词云
casts1 = ['瞿颖', '孙悦', '陈嘉桦', '蔡少芬', '龚琳娜', '李彩桦', '朱珠', '秋瓷炫', '谢娜', '黄丽玲', '卢靖姗', '刘惜君', '美依礼芽',
        '吉娜', '贾静雯', '陈意涵', '刘雅瑟', '徐怀钰', '张嘉倪', 'Amber', '芝芙', '赵丽娜', '谢欣', '汪小敏', '吴优', '吴倩',
        '曾可妮', '李莎旻子', '唐伯虎', '许靖韵', '卡捷琳娜', '陈冰', '王佳宇']


# 统计嘉宾词频并降序排序
def count_cast():
    castcounts = {}  # 字典存放“嘉宾：出现次数”键值对

    # 从词频中收集嘉宾词频
    for key in 词云.count(词云.get_words()).keys():
        if key in casts1:
            castcounts[key] = 词云.count(词云.get_words())[key]
    print(castcounts)

    return castcounts


# 生成柱状图
def draw_bar_chart(castcounts):
    # 载入数据
    x_label = list(castcounts.keys())  # x轴标签
    y = list(castcounts.values())  # y轴

    plt.figure(figsize=(25, 5), dpi=80)  # 定义图片大小
    x_loc = np.arange(len(x_label))  # 确定柱形个数
    color = ['red']  # 确定柱形颜色
    plt.rcParams["font.sans-serif"] = ['SimHei']  # 正确显示中文

    plt.xticks(x_loc, x_label)  # 绘制x刻度标签
    plt.bar(x_loc, y, color=color, width=0.8)  # 绘制y刻度标签
    plt.grid(True, linestyle=':', color='r', alpha=0.6)  # 设置网格刻度

    plt.title("乘风2023嘉宾热度")
    plt.xlabel("嘉宾")
    plt.ylabel("热度")

    plt.show()


def main():
    castcounts = count_cast()
    # print(castcounts)——测试
    draw_bar_chart(castcounts)


if __name__ == '__main__':
    main()
