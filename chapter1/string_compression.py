def compression(mystr: str) -> bool:
    if len(mystr) <= 2:
        return mystr

    compressed = ''
    count = 1
    current_char = mystr[0]
    for c in mystr[1:]:
        if not c == current_char:
            compressed += current_char
            compressed += str(count)
            current_char = c
            count = 1
            continue
        count += 1
    compressed += current_char
    compressed += str(count)

    return mystr if len(mystr) < len(compressed) else compressed


if __name__ == '__main__':
    print(compression('aabbbcccccaad'))
    print(compression('aabcdd'))
    print(compression('xx'))