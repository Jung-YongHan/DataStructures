# O(NlogN)
def quick_sort1(arr):  # not in-place 방식
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num == pivot:
            equal_arr.append(num)
        else:
            greater_arr.append(num)
    return quick_sort1(lesser_arr) + equal_arr + quick_sort1(greater_arr)


def quick_sort2(arr):  # in-place 방식
    def sort(low, high):
        if low >= high:
            return
        mid = partition(low, high)
        sort(low, mid-1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low+high)//2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low
    sort(0, len(arr)-1)
    return arr


def merge_sort1(arr):  # not in-place 방식
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    low_arr = merge_sort1(arr[:mid])
    high_arr = merge_sort1(arr[mid:])
    merge_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merge_arr.append(low_arr[l])
            l += 1
        else:
            merge_arr.append(high_arr[h])
            h += 1
    merge_arr += low_arr[l:]
    merge_arr += high_arr[h:]
    return merge_arr


def merge_sort2(arr):  # in-place 방식
    pass


def heap_sort(arr):

    def heapify(arr, index, length):
        largest = index
        left_index = 2 * index + 1
        right_index = 2 * index + 2

        if left_index < length and arr[left_index] > arr[largest]:
            largest = left_index
        if right_index < length and arr[right_index] > arr[largest]:
            largest = right_index
        if largest != index:
            arr[largest], arr[index] = arr[index], arr[largest]
            heapify(arr, largest, length)

    n = len(arr)
    for i in range(n//2-1, -1, -1):  # heap-order
        heapify(arr, i, n)

    for j in range(n-1, 0, -1):  # swapping top with end
        arr[0], arr[j] = arr[j], arr[0]
        heapify(arr, 0, j)

    return arr


# -----------------------------------------------------------------------------------
# O(N^2)
def bubble_sort1(arr):  # 매 단계 마다 앞, 뒤 원소 비교 후 스와핑
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubble_sort2(arr):  # 최적화1 - 이전 pass가 swap되지 않았다면 break
    for i in range(len(arr) - 1, 0, -1):
        swapped = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def bubble_sort3(arr):  # 최적화2 - 이전 pass에서 마지막으로 swap된 인덱스를 이용
    end = len(arr) - 1
    while end > 0:
        last_index = 0
        for i in range(end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                last_index = i
        end = last_index
    return arr


def insertion_sort1(arr):  # 비교 범위를 늘려가며 범위 내에 들어오는 값과 기존 값들을 비교하며 정렬
    for i in range(1, len(arr)):
        end = i
        for j in range(end, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr


def insertion_sort2(arr):  # 최적화 1: 기존 값과 비교 시에 스와핑이 이루어지지 않는다면 break
    for i in range(1, len(arr)):
        end = i
        for j in range(end, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swapped = True
            else:
                swapped = False
            if not swapped:
                break
    return arr


def selection_sort(arr):  # 매 단계 마다 최소 원소 값을 앞으로 스와핑
    for i in range(0, len(arr) - 1):
        min_index = i
        for j in range(i, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == '__main__':
    a = [6, 5, 7, 9, 11, 4, 2, 8, 10, 20, 14, 1]
    print(heap_sort(a))
