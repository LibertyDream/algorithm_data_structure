'''面试题63：股票的最大利润

假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？
-----------
input:[9，11，8，5，7，12，16，14]
output:11  #5买入，16卖出
'''

def max_diff(array):

    if array is None or len(array) < 2:
        return None

    buy = array[0]
    max_diff = array[1] - buy
    for idx in range(1, len(array)):
        if buy > array[idx]:
            buy = array[idx]
        else:
            diff = array[idx] - buy
            if diff > max_diff:
                max_diff = diff

        
    
    return max_diff

if __name__ == '__main__':

    datas = [[9,11,8,5,7,12,16,14],[9,11,8,7,19,5,12],[1,2,4,5],[5,4,3,2,1],[5,6],None,[1]]
    for data in datas:
        print(data, max_diff(data))

        
