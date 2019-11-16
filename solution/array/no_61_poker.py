'''面试题61：扑克牌中的顺子

从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
2~10为数字本身，A为1，J为11，Q为12，K为13，而大、小王可以看成任意数字。
'''

def is_continous(array):
    # 大小王用 0 表示
    if array is None or len(array) != 5:
        return False

    array.sort()

    zero_nums = 0
    for x in array:
        if x == 0:
            zero_nums += 1
    
    gap_nums = 0
    small = zero_nums
    big = zero_nums + 1
    while big < len(array):

        if array[small] == array[big]:
            return False
        
        gap_nums += array[big] - array[small] - 1
        small = big
        big += 1
    
    return True if zero_nums >= gap_nums else False


if __name__ == "__main__":

    datas = [None, [], [2,5,6,3,4], [0,10,7,0,8], [0,9,13,12,7], [4,6,5,7,5]]
    for data in datas:
        print(data, is_continous(data))