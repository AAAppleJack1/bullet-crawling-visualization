import requests  # HTTP库 HTTP协议采用URL（统一资源定位符）作为定位网络资源的标识符
import json  # 轻量级数据交换格式，Javascript的子集
import pandas  # 数据挖掘库

url1 = 'https://bullet-ali.hitv.com/bullet/tx/2023/06/14/152835/18923668/{}.json'
url2 = 'https://bullet-ali.hitv.com/bullet/tx/2023/06/13/114235/18379264/{}.json'  # 弹幕URL，每日更新


# 选择节目
def choose_show():
    choice = input('请选择想要爬取的节目名称（乘风2023/大侦探）： ')
    if choice == '乘风2023':
        url_0 = url1
    elif choice == '大侦探':
        url_0 = url2
    else:
        print('抱歉，暂时无法提供信息。\n')
        url_0 = 0
    return url_0


# 提取整个视频的数据
def get_danmu_total():
    danmu_all = []
    url_0 = choose_show()
    page = int(input('请输入节目总时长（分钟）： '))
    for i in range(page):
        danmu_all.extend(get_danmu_single(url_0, i))
        # 将每一页的数据整合到一起
    return danmu_all


# 通过URL地址获取数据
def get_danmu_single(url_0, i):

    try:  # 提取每一页（分钟）json文件数据
        url_single = url_0.format(i)
        # 每分钟的弹幕真实URL
        response = requests.get(url_single)
        # 向指定的资源发出请求,并返回一个包含服务器资源的response对象
        response.encoding = 'utf-8'
        # 从http header中猜测的响应内容编码方式
        # print(response.text)——测试
        data = json.loads(response.text)
        # response.text http响应内容的字符串形式，即URL对应的页面内容
        # json.loads()将str类型的数据转换成字典
    except:
        print("无法连接到弹幕数据")

    informations = []  # 存放每一页的弹幕具体数据
    for j in range(len(data['data']['items'])):
        # 弹幕数据存储在'data'的'items'中，items列表中以字典形式存储各用户的弹幕信息
        usertem = {}
        # 暂时存储每一个用户的信息及弹幕
        usertem['id'] = data['data']['items'][j]['uid']  # 获取用户id
        usertem['content'] = data['data']['items'][j]['content']  # 获取弹幕内容
        usertem['time'] = data['data']['items'][j]['time']  # 获取弹幕相对视频发布时间（以秒数计算）
        try:  # 弹幕点赞数不一定存在，尝试获取
            usertem['like_num'] = data['data']['items'][j]['v2_up_count']
        except:
            usertem['Like_num'] = ''
        informations.append(usertem)  # 将所有用户的信息及弹幕生成一个列表

    return informations


# 把df中的content列生成一个TXT文件
def content_txt(df):
    for i in df['content']:
        with open('danmu.txt', mode='a', encoding='utf-8') as f:
            f.write(i)
            f.write('\n')


def main():
    df = pandas.DataFrame(get_danmu_total())  # 表格型数据结构
    content_txt(df)


if __name__ == '__main__':
    main()
