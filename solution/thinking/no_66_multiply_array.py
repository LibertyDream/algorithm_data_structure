'''面试题66：构建乘积数组

给定一个数组A[0，1，…，n-1]，请构建一个数组B[0，1，…，n-1]，其中B中的元素
B[]=A[0]×A[1]…×A[-1]×4[i+1]…×A[-1]。不能使用除法。
'''

def multiply(A_arr):

    if A_arr is None or len(A_arr) == 0:
        return None

    B_arr = A_arr.copy()
    
    B_arr[0] = 1
    for i in range(1, len(B_arr)):
        B_arr[i] = B_arr[i - 1] * A_arr[i - 1]
    temp = 1
    for i in range(len(B_arr) - 2, -1,-1):
        temp *= A_arr[i + 1]
        B_arr[i] *= temp
    return B_arr


if __name__ == "__main__":

    data = [1, 2, 3, 4]
    print(data)
    print(multiply(data))