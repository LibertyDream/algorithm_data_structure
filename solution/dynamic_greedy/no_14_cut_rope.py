'''面试题14：剪绳子

给你一根长度为n的绳子，请把绳子剪成m段（m、n都是整数，n>1并且m>1），
每段绳子的长度记为k[0]，k[1]…，k[m]。请问k[0] × k[1] x … × k[m]可能的最大乘积是多少？
-----------------
Example:
input: 8
output: 18  # 2*3*3
'''

def cut_rope_dynamic(length):

    # O(n^2) time O(n) space

    if not isinstance(length, int) or length < 0:
        return -1

    if length == 0:
        return 0
    
    if length == 1:
        return 1

    if length == 2:
        return 1

    if length == 3:
        return 2

    products = [0] * (length + 1)

    products[0] = 0
    products[1] = 1
    products[2] = 2
    products[3] = 3

    for i in range(4, length + 1):
        max_product = 0
        for j in range(1, i // 2 + 1):
            if max_product < products[j] * products[i - j]:
                max_product = products[j] * products[i - j]
                products[i] = max_product

    return products[length]

def cut_rope_greedy(length):

    # O(1) time O(1) space

    if not isinstance(length, int) or length < 0:
        return -1

    if length == 0:
        return 0
    
    if length == 1:
        return 1

    if length == 2:
        return 1

    if length == 3:
        return 2

    times_3 = length // 3

    if length - 3 * times_3 == 1:
        times_3 -= 1
    
    times_2 = (length - 3 * times_3) // 2
 
    return 3 ** times_3 * 2 ** times_2

if __name__ == "__main__":

    lengths = [-1, 0, 1, 2, 3, 4, 5, 6, 7]
    for x in lengths:
        print('length:%d' % x)
        print('dynamic:%d, greedy:%d' % (cut_rope_dynamic(x),cut_rope_greedy(x)))
