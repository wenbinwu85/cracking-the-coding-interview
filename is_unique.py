def is_unique(mystr: str) -> bool:
    return len(set(mystr)) == len(mystr)


def is_unique2(mystr: str) -> bool:
    chars = []
    for c in mystr:
        if c in chars:
            return False
        chars.append(c)
    return True


def is_unique3(mystr: str) -> bool:
    for idx, val in enumerate(mystr):
        if val in mystr[idx+1:]:
            return False
    return True


if __name__ == '__main__':
    print(is_unique3('abcdefghij'))
    print(is_unique3('helloworld'))
