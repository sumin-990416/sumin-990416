n,m = map(int,input().split())

cnt = 1

while m != 1:
    if m % 10 == 1:
        m = m//10
        cnt += 1
    elif m % 2 == 0:
        m = m//2
        cnt += 1
    else:
        cnt = -1
        break

    if m == n:
        break
    elif m < n:
        cnt = -1
        break


print(cnt)