'''面试题64：求1+2+…+n

求1+2+…+n，要求不能使用乘除法、for、while、if else、switch、case等关键字
及条件判断语句（A？B:C）
'''

class Sum(object):

    sums = 0
    count = 0

    def __init__(self):
       Sum.count += 1
       Sum.sums += Sum.count

def get_sum():
    sums = 0
    count = 0
    def in_sum():
        nonlocal count
        nonlocal sums
        count += 1
        sums += count
    return in_sum

if __name__ == '__main__':

    n = 100
    
    temp = [Sum() for _ in range(n)]
    print(Sum.sums)

    bag = get_sum()
    for _ in range(n):
        bag()
    print(bag.__closure__[1].cell_contents)