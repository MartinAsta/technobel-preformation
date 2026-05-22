def longestCommonPrefix(arr1: list, arr2: list) -> int:
    arr1_prefixes = set()
    biggest_prefix = 0
    for i in arr1:
        num = str(i)
        for j in range(len(num)):
            arr1_prefixes.add(num[0:j+1])

    for i in arr2:
        num = str(i)
        for j in range(len(num), biggest_prefix, -1):
            if num[0:j] in arr1_prefixes:
                biggest_prefix = j
                break
    return biggest_prefix


arr1 = [1,10,100]
arr2 = [1000]
print(longestCommonPrefix(arr1, arr2))