def urlify(mystr: str, length: int) -> str:
    return mystr.strip().replace(' ', '%20')


def urlify2(mystr: str, length: int) -> str:
    char_list = list(mystr)
    for i in reversed(range(length)):  # remove trailing spaces
        if char_list[i] == ' ':
            char_list.pop()
        else:
            break

    for idx, val in enumerate(char_list):  # replace spaces with %20
        if val == ' ':
            char_list[idx] = '%20'

    return ''.join(char_list)


if __name__ == '__main__':
    print(urlify2('Mr 3ohn Smith', 13))
