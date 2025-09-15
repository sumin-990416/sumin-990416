T = int(input())
for _ in range(T):
    n = int(input())
    numbers = [input() for _ in range(n)]
    numbers.sort()
    
    result = 'YES'
    for i in range(n - 1):
        if numbers[i+1].startswith(numbers[i]):
            result = 'NO'
            break
            
    print(result)