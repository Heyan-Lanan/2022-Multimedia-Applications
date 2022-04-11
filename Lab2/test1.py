import math

with open('test.txt', 'r') as read_f, open('res.txt', 'w') as write_f:
    sumof = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    maxof = 0
    for line in read_f:
        num = float(line)
        num2 = math.log(1 + 255*math.fabs(num), math.e) / math.log(1 + 255, math.e)
        write_f.write(str(num2))
        write_f.write('\n')
        lei = math.floor(num2 / 0.0625)
        if lei == 16:
            lei = lei - 1
        sumof[lei] = sumof[lei] + 1
        if num2 > maxof:
            maxof = num2
    print(sumof)
    print(maxof)

