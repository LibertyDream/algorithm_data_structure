'''面试题16：数值的整数次方

实现函数 double Power（double base，int exponent），求base的exponent次方。
不得使用库函数，同时不需要考虑大数问题
-------------
Example
input:2,3
output:8
---------------
功能、边界、负面测试，错误返回方式
'''

def power(base:float, exponent:int):

    if not isinstance(exponent, int):
        raise TypeError('exponent must be an integer')

    if abs(base - 0.0) < 1e-9 and exponent < 0:
        raise ValueError('base is 0, exponent cannot be negative')

    if exponent >= 0:
        return __unsinged_power(base, exponent)
    else:
        return 1.0 / __unsinged_power(base,abs(exponent))

def __unsinged_power(base, exponent):

    if exponent == 0:
        return 1
    
    if exponent == 1:
        return base
    
    res = __unsinged_power(base, exponent >> 1)
    res *= res
    if (exponent & 0b1) == 1:
        res *= base
    return res

if __name__ == "__main__":
    
    datas = [[2,3],[2,-1],[2,0],[-2,3],[-2,-2],[-2,0],[0,3],[0,0],[.5,2],[.5,0],[.5,-2]]

    for data in datas:
        print('power(%f,%d):%f'%(data[0],data[1],power(data[0],data[1])))
