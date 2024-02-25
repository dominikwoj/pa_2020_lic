def lic(l, r):
    arr = None

    potyczkowa_number = []

    def gen(l, r):
        for i in range(l, r + 1):
            arr = list(dict.fromkeys(list(str(i))))
            # print(arr)
            if '0' in arr:
                continue
            yield (i, arr)

    # for i in range(l, r + 1):
    #     arr = list(dict.fromkeys(list(str(i))))
    #     # print(arr)
    #     if '0' in arr:
    #         continue

    ite = gen(l, r)
    for i, arr in ite:
        is_potyczkowa_number = True
        for j in arr:
            if j == '1':
                continue
            elif i % int(j) == 0:
                continue
            else:
                is_potyczkowa_number = False
                break
        if is_potyczkowa_number == True:
            potyczkowa_number.append(i)

    # print(potyczkowa_number)
    # print(arr)

    return len(potyczkowa_number)


if __name__ == '__main__':
    print(lic(1, 100))
    # print(lic(1000000, 10000000))
    # print(lic(1000000, 100000000))
