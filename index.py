import requests, json, random
import pandas as pd


city_list = [
    ["上海", "fce2e3a36450422b7fad3f2b90370efd64d8acadd74fe416da09a4c05d7f8e51"],
    ["北京", "d5036cf54fcb57e9dceb9fefe3917fff64d8acadd74fe416da09a4c05d7f8e51"]
]

# 反反爬虫策略
# 请求头
USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"
]
head = {
    'User-Agent': '{0}'.format(random.sample(USER_AGENT_LIST, 1)[0])  # 随机获取
}

csv_headers = [
    "店铺名称","区域","人均消费","菜品分类","口味评分",
    "环境评分","服务评分","分店名称","所在的城市"
]

count = 0
def saveData(cityName,data):
    global count

    food_lists = []
    # 数据过滤 数据清洗 数据格式化
    for dd in json.loads(data)['shopBeans']:
        count += 1
        # 商店的地址
        shop_address = dd['mainRegionName']
        # 人均消费
        avg_price = dd['avgPrice']
        # 商店的名称
        shop_name = dd['shopName']
        # 菜品分类的名称
        main_nategory_name = dd['mainCategoryName']
        # 口味评分
        refined_score1 = dd['refinedScore1']
        # 环境评分
        refined_score2 = dd['refinedScore2']
        # 服务评分
        refined_score3 = dd['refinedScore3']
        # 分店名称
        branch_name = dd['branchName']

        shop = (shop_name, shop_address, avg_price,
                main_nategory_name,refined_score1,
                refined_score2,refined_score3,
                branch_name,cityName)
        food_lists.append(shop)

    # 数据分析
    result = pd.DataFrame(data=food_lists)
    # 保存数据
    # result.to_csv('food.csv',index=False,header=csv_headers,mode='a+',encoding='utf-8-sig')
    if count == 100:
        result.to_csv('food.csv', index=False, header=csv_headers, mode='a+', encoding='utf-8-sig')
    else:
        result.to_csv('food.csv', index=False, header=False, mode='a+', encoding='utf-8-sig')

    print(count)

def foodSpider(city):
    city_name = city[0]
    city_id = city[1]
    base_url = r'http://www.dianping.com/mylist/ajax/shoprank?rankId=' + city_id
    datas = requests.get(base_url, headers=head)
    # print(datas.content)
    saveData(city_name, str(datas.text))


if __name__ == '__main__':
    for city in city_list:
        foodSpider(city)
