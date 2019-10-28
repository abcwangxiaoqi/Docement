
import random;

# 随机数 数量
randNum = 1000

# 随机数范围 0～1000
randMax = 1000

randResultArray = []

randArray = []

for index in range(0,randMax) :
    randArray.append(index+1)

for index in range(0,randNum) :
    randomIndex = random.randint(index,randMax-1)
   # print(randomIndex)

    # 交换randomIndex 和 index 之间的数据
    temp = randArray[randomIndex]
    randArray[randomIndex] = randArray[index]
    randArray[index] = temp

    print(temp)

print('dd')

