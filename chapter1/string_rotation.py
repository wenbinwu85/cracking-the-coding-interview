def is_substring(s1: str, s2: str) -> bool:
    return s2 in s1

def is_string_rotation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    return is_substring(s1*2, s2)


if __name__ == '__main__':
    rotation = 'waterbottle'
    original = 'erbottlewat'
    print(is_string_rotation(original, rotation))
