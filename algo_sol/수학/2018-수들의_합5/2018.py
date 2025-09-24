def find_sum(n):
    result = 1
    for i in range(1,n):
        j = i
        num = 0
        while num < n:
            num += j
            j += 1

        if num == n:
            result += 1

    return result


print(find_sum(int(input())))
