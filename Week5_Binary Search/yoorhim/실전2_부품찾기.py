n = int(input())
n_product = list(map(int, input().split()))
n_product.sort()
m = int(input())
m_product = list(map(int, input().split()))

for item in m_product:
    start = 0
    end = n - 1
    flag = True

    while start <= end:
        mid = (start + end) // 2
        if n_product[mid] == item:
            print('yes', end=' ')
            flag = False
            break
        elif n_product[mid] > item:
            end = mid - 1
        else:
            start = mid + 1
    if flag == True:
        print('no', end=' ')

"""
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) //2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in m_product:
    result = binary_search(n_product, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end= ' ')
"""
