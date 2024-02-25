def lic(l, r):
    arr = None

    potyczkowa_number = []
    for i in range(l, r + 1):
        arr = list(dict.fromkeys(list(str(i))))
        # print(arr)
        if '0' in arr:
            continue

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
    l, r = list(map(int, input().split()))
    print(lic(l, r))
