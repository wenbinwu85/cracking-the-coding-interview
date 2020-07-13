def is_one_away(str1: str, str2: str) -> bool:
    # obivous cases
    if str1 == str2:
        return True

    if abs(len(str1) - len(str2)) > 1:
        return False

    # replace
    if len(str1) == len(str2):
        count = 0
        for a, b in zip(str1, str2):
            count += 1 if a != b else 0
            if count > 1:
                return False
        return True

    # insert/remove
    if len(str1) > len(str2):
        longer, shorter = str1, str2
    else:
        longer, shorter = str2, str1

    match_idx = 0
    for i in longer:
        try:
            j = shorter[match_idx]
        except IndexError:
            break
        if i == j:
            match_idx += 1
        elif longer[match_idx+1:] != shorter[match_idx:]:
            return False
    return True


if __name__ == '__main__':
    # replace 
    print(is_one_away('pale', 'bale'))
    print(is_one_away('pale', 'pall'))

    print(is_one_away('pennie', 'bannie'))

    # insert/remove
    print(is_one_away('pale', 'ple')) 
    print(is_one_away('pale', 'pal'))
    print(is_one_away('ale', 'pale'))
    print(is_one_away('pale', 'pales'))
    print(is_one_away('parle', 'pale'))
    print(is_one_away('a', 'a'))
    print(is_one_away('x', ' '))

    print(is_one_away('pale', 'paless'))
    print(is_one_away('apples', 'app'))
    print(is_one_away('apples', 'ple'))
