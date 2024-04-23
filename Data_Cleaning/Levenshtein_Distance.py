def lev(a, b):
    # if leng a is 0, return length of b
    if len(a) == 0:
        return len(b)
    # if leng b is 0, return length of a
    elif len(b) == 0:
        return len(a)
    # if the first letter of a is the same as the first letter of b, return the distance of the rest of the strings
    elif a[0] == b[0]:
        return lev(a[1:], b[1:])
    # if the first letter of a is not the same as the first letter of b, return 1 + the minimum of the three possible distances
    else:
        return 1 + min(lev(a[1:], b), lev(a, b[1:]), lev(a[1:], b[1:]))


# Test cases for the function
def main():
    print(lev("kitten", "sitting"))
    print(lev("kitten", "kitten"))
    print(lev("kitten", "kittens"))


main()
