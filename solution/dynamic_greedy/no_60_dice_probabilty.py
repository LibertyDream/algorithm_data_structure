'''面试题60：n个骰子的点数

把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。
输入n，打印出s的所有可能的值出现的概率。
'''

def dice_probability(dice_num,dice_max_value):

    if dice_num < 1 or dice_max_value < 2:
        print('None')
        return

    flag = 0
    temp = [[0]*(dice_max_value * dice_num + 1),[0]*(dice_max_value * dice_num + 1)]
    for i in range(1, dice_max_value + 1):
        temp[flag][i] = 1
    
    for j in range(2, dice_num+1):
        for i in range(j):
            temp[1-flag][i] = 0

        for i in range(j, dice_max_value*j+1):
            temp[1-flag][i] = 0
            value = 1
            while value <= i and value <= dice_max_value:
                temp[1-flag][i] += temp[flag][i-value]
                value += 1

        flag = 1-flag
    total = pow(dice_max_value, dice_num)
    idx = 0
    print('dice_num: %d, dice_max_value: %d' % (dice_num, dice_max_value))
    for num in temp[flag][dice_num:]:
        raito = num / total
        print('%d: %.3f'%(dice_num+idx, raito), end=' | ')
        idx += 1
    print()

if __name__ == '__main__':

    dice_probability(2,6)
    dice_probability(1,6)
    dice_probability(0,6)
