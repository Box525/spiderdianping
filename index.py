import requests, json
import pandas as pd


city_list = [
    ["上海", "fce2e3a36450422b7fad3f2b90370efd64d8acadd74fe416da09a4c05d7f8e51"]
]

def saveData(cityName,data):
    food_lists = []
    # 数据过滤 数据清洗 数据格式化
    for dd in json.loads(data)['shopBeans']:
        # 商店的地址
        shop_address = dd['mainRegionName']
        # 人均消费
        avg_price = dd['avgPrice']
        # 商店的名称
        shop_name = dd['shopName']

        shop = (shop_name, shop_address, avg_price)
        food_lists.append(shop)

    # 数据分析
    result = pd.DataFrame(data=food_lists)
    # 保存数据
    result.to_csv('food.csv',index=False,header=False,mode='a+',encoding='utf-8-sig')



def foodSpider(city):
    city_name = city[0]
    city_id = city[1]
    base_url = r'http://www.dianping.com/mylist/ajax/shoprank?rankId=' + city_id
    datas = requests.get(base_url)
    # print(datas.content)
    saveData(city_name, str(datas.text))


if __name__ == '__main__':
    foodSpider(city_list[0])
