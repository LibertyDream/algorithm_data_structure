'''面试题31：栈的压入、弹出序列

输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
假设压入栈的所有数字均不相等。
----------------
input:
    push:[1，2，3，4，5]
    pop:[4，5，3，2，1]
output: True
input:
    push:[1,2,3,4,5]
    pop:[4,3,5,1,2]
output:False
'''

def is_possible(ls_push, ls_pop):
    
    if ls_push is None or ls_pop is None or len(ls_push) == 0 or len(ls_pop) == 0:
        return False
    
    ret = False

    idx_push = 0
    idx_pop = 0
    stack = []
    while idx_pop < len(ls_pop):

        while len(stack) == 0 or stack[-1] != ls_pop[idx_pop]:
            
            if idx_push == len(ls_push):
                break
            stack.append(ls_push[idx_push])
            idx_push += 1
        
        if stack[-1] != ls_pop[idx_pop]:
            break

        stack.pop()
        idx_pop += 1
    if idx_pop == len(ls_pop):
        ret = True
    
    return ret


if __name__ == '__main__':

    ls_push = [1,2,3,4,5]
    ls_pop_1 = [4,5,3,2,1]
    ls_pop_2 = [4,3,5,1,2]

    print(is_possible(ls_push, ls_pop_1))
    print(is_possible(ls_push, ls_pop_2))
