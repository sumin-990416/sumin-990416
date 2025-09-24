n, k = map(int, input().split())


def make_mod(n, k):
    mod = n % k
    if mod == 0:
        return 1

    mod_list = {mod}
    count = 1
    shift = 10 ** len(str(n))
    for _ in range(k):
        mod = (mod * shift + n) % k
        count += 1
        if mod == 0:
            return count

        if mod in mod_list:
            return -1
        mod_list.add(mod)
    return -1

result = make_mod(n, k)
print(result)