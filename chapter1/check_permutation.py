def is_permu(mystr1: str, mystr2: str) -> bool:
    if not len(mystr1) == len(mystr2):
        return False
    return set(mystr1) == set(mystr2)


if __name__ == '__main__':
    print(is_permu('ben', 'neb'))
    print(is_permu('ben', 'benny'))
    print(is_permu('ben', 'been'))
