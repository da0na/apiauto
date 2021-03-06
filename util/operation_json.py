# coding:utf-8
import json
# fp = open("../dataconfig/login.json")
# data = json.load(fp)
# print(data['login'])


class OperationJson:
    def __init__(self):
        self.data = self.read_data()
    def read_data(self):
        with open('../dataconfig/login.json') as fp:
            data = json.load(fp)
            return data


# 根据关键字获取数据
    def get_data(self, id):
        return self.data[id]


if __name__ == "__main__":
    opjson = OperationJson()
    print(opjson.get_data("addcart"))


