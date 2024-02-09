def permutations(elements):
    if len(elements) <= 1:
        return [elements]
    else:
        perms = []
        for perm in permutations(elements[1:]):
            for i in range(len(elements)):
                print(perm[:i] + elements[0:1] + perm[i:])

# Пример использования
string = input()
perms = permutations(string)