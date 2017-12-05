# String compression


def strCompress(string):
    if len(string) <= 1:
        return string

    nstr = []
    i = 0
    while i < len(string):
        common = 1
        nstr.append(string[i])
        j = i + 1
        while j < len(string):
            if string[i] == string[j]:
                j += 1
                common += 1
            else:
                break
        i = j
        nstr.append(str(common))

        if len(nstr) >= len(string):
            return string

    return ''.join(nstr)


case1 = 'abbcccc'
print(strCompress(case1))
