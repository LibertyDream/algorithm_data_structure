import sort_helper as sh

def insertion_sort(*arr):

    arr = list(arr)
    for i in range(1, len(arr)):
        temp = arr[i]

        j = i
        while j > 0 and arr[j-1] > temp:
            arr[j] = arr[j-1]
            j -= 1

        arr[j] = temp
    
    return arr

if __name__ == "__main__":

    nums = 10000
    input_arr = sh.generate_int_array(nums, 0, nums)
    
    sh.sort_cost('insertion sort', insertion_sort, input_arr)

    input_arr = sh.generate_nearly_ordered_array(nums, 100)

    sh.sort_cost('insertion sort:', insertion_sort, input_arr)



