def func1(list_1, list_2):
    for i in list_1:
        for j in list_2:
            if i == j:
                return True
    return False


def func2(list_1, list_2):
    temp_dic = {}
    for i in list_1:
        temp_dic[i] = True
    for j in list_2:
        item = temp_dic.get(j)
        if item == True:
            return True
    return False


def reverse_func(test_str: str):
    arr = list(test_str)
    arr_size = len(arr)
    j = arr_size - 1
    for i in range(arr_size):
        if j <= i:
            break
        else:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j = j - 1

    return (''.join(arr))


def mergeSortedArrays(list_1, list_2):
    size = (len(list_1) + len(list_2))
    ret_arr = [None] * size
    i = 0
    j = 0
    k = 0
    while i < size:
        if j < len(list_1) and k < len(list_2):
            if list_1[j] <= list_2[k]:
                ret_arr[i] = list_1[j]
                j = j + 1
            else:
                ret_arr[i] = list_2[k]
                k = k + 1
        elif j < len(list_1) and not (k < len(list_2)):
            ret_arr[i] = list_1[j]
            j = j + 1
        elif k < len(list_2) and not j < len(list_1):
            ret_arr[i] = list_2[k]
            k = k + 1

        i = i + 1

    return ret_arr


def firstRecurringChar(list):
    charDict = {}
    for num in list:
        if charDict.get(num) == None:
            charDict[num] = True
        elif charDict.get(num) == True:
            return num
    return None


listTest_1 = [2, 5, 1, 2, 3, 5, 1, 2, 4]
listTest_2 = [2, 1, 1, 2, 3, 5, 1, 2, 4]
listTest_3 = [2, 3, 4, 5]

print(mergeSortedArrays([4, 6, 30], [0, 3, 4, 31]))
print(firstRecurringChar(listTest_1))
print(firstRecurringChar(listTest_2))
print(firstRecurringChar(listTest_3))