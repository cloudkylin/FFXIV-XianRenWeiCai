import itertools

money = {6:10000,7:36,8:720,9:360,10:80,11:252,
         12:108,13:72,14:54,15:180,16:72,17:180,
         18:119,19:36,20:306,21:1080,22:144,23:1800,24:3600}
way = ['第一行','第二行','第三行','第一列','第二列','第三列','左上至右下','右上至左下']
num = [1,2,3,4,5,6,7,8,9]

linsam = [[] for i in range(8)]
linmoney = [[] for i in range(8)]
x = []
y = []
avgmoney = []

def cal(list):
    global money
    global linsam
    global linmoney
    linsam[0].append(list[0] + list[1] + list[2])
    linsam[1].append(list[3] + list[4] + list[5])
    linsam[2].append(list[6] + list[7] + list[8])
    linsam[3].append(list[0] + list[3] + list[6])
    linsam[4].append(list[1] + list[4] + list[7])
    linsam[5].append(list[2] + list[5] + list[8])
    linsam[6].append(list[0] + list[4] + list[8])
    linsam[7].append(list[2] + list[4] + list[6])
    for i in range(8):
        num = linsam[i][-1]
        linmoney[i].append(money[num])

for i in range(4):
    x.append(int(input("位置：")))
    y.append(int(input("数：")))
    num.remove(y[i])
for i in itertools.permutations(num,5):
    comb = list(i)
    for j in range(4):
        comb.insert(x[j]-1,y[j])
    cal(comb)

maxmoney = 0
maxmoneyway = 0
for i in range(8):
    avgmoney.append(sum(linmoney[i]) / len(linmoney[i]))
    if avgmoney[i] > float(maxmoney):
        maxmoney = avgmoney[i]
        maxmoneyway = i
print('预计选择 '+way[maxmoneyway]+' 获得的金蝶币最多，为'+str(maxmoney))
input('按回车键退出...')