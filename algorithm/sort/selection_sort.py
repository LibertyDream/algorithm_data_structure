import sort_helper as sh

def selection_sort(*arr):

    arr = list(arr)
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def __str__(self):
        return '%s: %s' % (self.name, self.score)

    def __lt__(self, other):
        return self.score < other.score if self.score != other.score else self.name < other.name


if __name__ == "__main__":
    nums = 10000

    input_arr = sh.generate_int_array(nums, 0, nums)
    # sh.print_array(selection_sort(*input_arr))

    # input_arr = sh.generate_float_array(nums, 0, nums)
    # sh.print_array(selection_sort(*input_arr))

    # input_arr = sh.generate_string_array(nums, 2)
    # sh.print_array(selection_sort(*input_arr))

    # input_arr = [Student('Zhao',100),Student('Qian',95),Student('Sun',95),Student('Li',90)]
    # for _ in selection_sort(*input_arr):
    #     print(_)

    sh.sort_cost('selection_sort', selection_sort, input_arr)
