import sort_helper as sh
def bubble_sort(self, *arr):

    arr = list(arr)

    for i in range(len(arr) - 1):
        swap = False

        for j in range(len(arr)- 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
        if not swap:
            break

    return arr

if __name__ == "__main__":
    nums = 1000

    arr = sh.generate_int_array(nums, 0, nums)
    sh.sort_cost('bubble_sort', bubble_sort, arr)