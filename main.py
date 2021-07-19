# First question's of project
def flatten(l):
    return flatten(l[0]) + (flatten(l[1:]) if len(l) > 1 else []) if type(l) is list else [l]


def reverseList(l):
    newl = l[::-1]
    return newl


if __name__ == '__main__':
    liste = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
    result1 = flatten(liste)
    result2 = reverseList(liste)
    print(result1)
    print(result2)
