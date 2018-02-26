import itertools

class analysis:
    def __init__(self, x, y):
        #固定参数
        self.money = {6: 10000, 7: 36, 8: 720, 9: 360, 10: 80, 11: 252,
                 12: 108, 13: 72, 14: 54, 15: 180, 16: 72, 17: 180,
                 18: 119, 19: 36, 20: 306, 21: 1080, 22: 144, 23: 1800, 24: 3600}
        self.way = ['第一行', '第二行', '第三行', '第一列', '第二列', '第三列', '左上至右下', '右上至左下']
        self.num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.x = x
        self.y = y

        #计算变量
        self.linsam = [[] for i in range(8)]
        self.linmoney = [[] for i in range(8)]

        for i in range(4):
            self.num.remove(y[i])
        for i in itertools.permutations(self.num, 5):
            comb = list(i)
            for j in range(4):
                comb.insert(x[j], y[j])
            self.cal(comb)

    def cal(self,list):
        #计算每一行的总合
        self.linsam[0].append(list[0] + list[1] + list[2])
        self.linsam[1].append(list[3] + list[4] + list[5])
        self.linsam[2].append(list[6] + list[7] + list[8])
        self.linsam[3].append(list[0] + list[3] + list[6])
        self.linsam[4].append(list[1] + list[4] + list[7])
        self.linsam[5].append(list[2] + list[5] + list[8])
        self.linsam[6].append(list[0] + list[4] + list[8])
        self.linsam[7].append(list[2] + list[4] + list[6])

        #计算每一行的奖励
        for i in range(8):
            num = self.linsam[i][-1]
            self.linmoney[i].append(self.money[num])

    def bestline(self):
        avgmoney = []
        maxmoney = 0
        maxmoneyline = 0
        for i in range(8):
            avgmoney.append(sum(self.linmoney[i]) / len(self.linmoney[i]))
            if avgmoney[i] > float(maxmoney):
                maxmoney = avgmoney[i]
                maxmoneyline = i
        return '预计选择 ' + self.way[maxmoneyline] + ' 获得的金蝶币最多，为 ' + str(maxmoney)

    def maxmoneyline(self):
        maxmoneyNum = (6, 24, 23)
        msg = ''
        for i in range(3):
            maxmoneyProbability = 0
            maxmoneyLine = 0
            for j in range(8):
                time = self.linsam[j].count(maxmoneyNum[i])
                if i ==0:
                    print(time)
                if time > maxmoneyProbability:
                    maxmoneyProbability = time
                    maxmoneyLine = j
            if maxmoneyProbability == 0:
                msg += '没有可能获得 %d 金蝶币。\n'% self.money[maxmoneyNum[i]]
            else:
                msg += '选择 %s 最有可能获得 %d 金蝶币，概率为 %d/120。\n'% (self.way[maxmoneyLine], self.money[maxmoneyNum[i]], maxmoneyProbability)
        return msg