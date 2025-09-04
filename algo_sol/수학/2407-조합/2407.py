n, m = map(int,input().split())

result_1 = 1
result_2 = 1
def make_com(num,k):
    global result_1,result_2
    if k == m+1:
        print(result_1//result_2)
        return    
    
    result_1 *= num
    result_2 *= k
    make_com(num-1,k+1)

make_com(n,1)