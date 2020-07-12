def is_palidrome_permutaion(mystr: str) -> bool:
    mystr = mystr.lower()
    char_dict = dict.fromkeys(list(mystr), 0)
    for i in set(mystr):
        if ord('a') <= ord(i) <= ord('z'):
            char_dict[i] = mystr.count(i)

    oddcount = 0
    for j in char_dict.values():
        if j % 2:
            oddcount += 1

    return oddcount <= 1

    



if __name__ == '__main__':
    print(is_palidrome_permutaion('tacocat'))
    print(is_palidrome_permutaion('taco cat'))
    print(is_palidrome_permutaion('cat o cat'))
    print(is_palidrome_permutaion('cat, o cat!'))
    print(is_palidrome_permutaion('taco cats'))
    print(is_palidrome_permutaion('hello world'))

