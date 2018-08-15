# -*- coding: UTF-8 -*-
from flask import Flask, request, render_template
import itertools

app = Flask(__name__)


class Analysis:
    def __init__(self, x, y):
        # 固定参数
        self.money = {6: 10000, 7: 36, 8: 720, 9: 360, 10: 80, 11: 252,
                      12: 108, 13: 72, 14: 54, 15: 180, 16: 72, 17: 180,
                      18: 119, 19: 36, 20: 306, 21: 1080, 22: 144, 23: 1800, 24: 3600}
        self.way = ['第一行', '第二行', '第三行', '第一列', '第二列', '第三列', '左上至右下', '右上至左下']
        self.num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.x = x  # 位置坐标
        self.y = y  # 数

        # 计算变量
        self.lineSum = [[] for i in range(8)]
        self.lineMoney = [[] for i in range(8)]
        self.lineStat = [dict() for i in range(8)]

        for i in range(4):
            self.num.remove(y[i])  # 从1-9中移除已知的数
        for i in itertools.permutations(self.num, 5):  # 全排列
            comb = list(i)
            for j in range(4):
                comb.insert(x[j], y[j])  # 将已知的数插入对应位置
            self.cal(comb)

    def cal(self, lists):
        # 计算每种情况的总合
        self.lineSum[0].append(lists[0] + lists[1] + lists[2])  # 第一行
        self.lineSum[1].append(lists[3] + lists[4] + lists[5])  # 第二行
        self.lineSum[2].append(lists[6] + lists[7] + lists[8])  # 第三行
        self.lineSum[3].append(lists[0] + lists[3] + lists[6])  # 第一列
        self.lineSum[4].append(lists[1] + lists[4] + lists[7])  # 第二列
        self.lineSum[5].append(lists[2] + lists[5] + lists[8])  # 第三列
        self.lineSum[6].append(lists[0] + lists[4] + lists[8])  # 左上至右下
        self.lineSum[7].append(lists[2] + lists[4] + lists[6])  # 右上至左下

        # 计算每种情况的奖励
        for i in range(8):
            num = self.lineSum[i][-1]
            money = self.money[num]
            self.lineMoney[i].append(money)
            if self.lineStat[i].get(money) is not None:
                self.lineStat[i][money] = self.lineStat[i].get(money) + 1
            else:
                self.lineStat[i][self.money[num]] = 1

    def max_avg(self):
        max_avg_money = 0
        max_avg_way = 0
        this_way = 0
        for line in self.lineStat:  # 获取每一行的统计结果
            sum_money = 0
            for money, times in line.items():
                sum_money += money * times
            sum_money /= 120  # 求每一行的平均值
            if sum_money > max_avg_money:  # 判断是否更新最大值
                max_avg_money = sum_money
                max_avg_way = this_way
            this_way += 1  # 计数
        return '预计选择 %s 获得的金蝶币最多，为 %d' % (self.way[max_avg_way], max_avg_money)

    def most_money(self):
        need_num = (10000, 3600, 1800)
        msg = ''
        for money in need_num:
            max_times_money = 0
            max_times_way = 0
            this_way = 0
            for line in self.lineStat:  # 获取每一行的统计结果
                if line.get(money, 0) > max_times_money:  # 判断是否需要更新最大值
                    max_times_money = line.get(money)
                    max_times_way = this_way
                this_way += 1
            if max_times_money == 0:  # 判断是否有需要的钱数
                msg += '没有可能获得 %d 金蝶币。<br/>' % money
            else:
                msg += '选择 %s 最有可能获得 %d 金蝶币，概率为 %d/120。<br/>' % (
                    self.way[max_times_way], money, max_times_money)
        return msg


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def cal():
    pos = []
    num = []
    if request.form['pos1'] != '':
        pos.append(0)
        num.append(int(request.form['pos1']))
    if request.form['pos2'] != '':
        pos.append(1)
        num.append(int(request.form['pos2']))
    if request.form['pos3'] != '':
        pos.append(2)
        num.append(int(request.form['pos3']))
    if request.form['pos4'] != '':
        pos.append(3)
        num.append(int(request.form['pos4']))
    if request.form['pos5'] != '':
        pos.append(4)
        num.append(int(request.form['pos5']))
    if request.form['pos6'] != '':
        pos.append(5)
        num.append(int(request.form['pos6']))
    if request.form['pos7'] != '':
        pos.append(6)
        num.append(int(request.form['pos7']))
    if request.form['pos8'] != '':
        pos.append(7)
        num.append(int(request.form['pos8']))
    if request.form['pos9'] != '':
        pos.append(8)
        num.append(int(request.form['pos9']))
    res = Analysis(pos, num)
    best_line = res.max_avg()
    max_money = res.most_money()
    return render_template('index.html', bestline=best_line, maxmoney=max_money)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5900)
