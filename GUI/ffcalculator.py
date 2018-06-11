import itertools


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

    def cal(self, list):
        # 计算每种情况的总合
        self.lineSum[0].append(list[0] + list[1] + list[2])  # 第一行
        self.lineSum[1].append(list[3] + list[4] + list[5])  # 第二行
        self.lineSum[2].append(list[6] + list[7] + list[8])  # 第三行
        self.lineSum[3].append(list[0] + list[3] + list[6])  # 第一列
        self.lineSum[4].append(list[1] + list[4] + list[7])  # 第二列
        self.lineSum[5].append(list[2] + list[5] + list[8])  # 第三列
        self.lineSum[6].append(list[0] + list[4] + list[8])  # 左上至右下
        self.lineSum[7].append(list[2] + list[4] + list[6])  # 右上至左下

        # 计算每种情况的奖励
        for i in range(8):
            num = self.lineSum[i][-1]
            money = self.money[num]
            self.lineMoney[i].append(money)
            if self.lineStat[i].get(money) is not None:
                self.lineStat[i][money] = self.lineStat[i].get(money) + 1
            else:
                self.lineStat[i][self.money[num]] = 1

    def maxavg(self):
        maxavg_money = 0
        maxavg_way = 0
        thisway = 0
        for line in self.lineStat:  # 获取每一行的统计结果
            sum = 0
            for money, times in line.items():
                sum += money * times
            sum /= 120  # 求每一行的平均值
            if sum > maxavg_money:  # 判断是否更新最大值
                maxavg_money = sum
                maxavg_way = thisway
            thisway += 1  # 计数
        return '预计选择 %s 获得的金蝶币最多，为 %d' % (self.way[maxavg_way], maxavg_money)

    def mostmoney(self):
        neednum = (10000, 3600, 1800)
        msg = ''
        for money in neednum:
            maxtimes_money = 0
            maxtimes_way = 0
            thisway = 0
            for line in self.lineStat:  # 获取每一行的统计结果
                if line.get(money, 0) > maxtimes_money:  # 判断是否需要更新最大值
                    maxtimes_money = line.get(money)
                    maxtimes_way = thisway
                thisway += 1
            if maxtimes_money == 0:  # 判断是否有需要的钱数
                msg += '没有可能获得 %d 金蝶币。\n' % money
            else:
                msg += '选择 %s 最有可能获得 %d 金蝶币，概率为 %d/120。\n' % (
                    self.way[maxtimes_way], money, maxtimes_money)
        return msg
