def nonRepeatingCharacter(string):
    hashTable = {}

    for character in string:
        if character in hashTable:
            hashTable[character] += 1
        else:
            hashTable[character] = 1

    for character, count in hashTable.items():
        if count == 1:
            return character

    return None

print(nonRepeatingCharacter("aabcb"))
print(nonRepeatingCharacter("xxyz"))
print(nonRepeatingCharacter("aabb"))
