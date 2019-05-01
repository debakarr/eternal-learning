def oneEditAway(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False

    changeCount = 0
    i = 0
    j = 0

    while i < len(str1) and j < len(str2):
        if str1[i] != str2[j]:
            changeCount += 1
            if changeCount > 1:
                return False
            if len(str1) != len(str2):
                if len(str1) > len(str2):
                    i += 1
                    continue
                else:
                    j += 1
                    continue

        i += 1
        j += 1

    return True


print(oneEditAway("abcde", "abfde"))
print(oneEditAway("abcde", "abcde"))
print(oneEditAway("abcde", "abde"))
