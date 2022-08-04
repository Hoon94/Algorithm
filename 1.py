def myisalpha(char):
    if ord(char) in asc:
        return True
    else:
        return False


def check(password, admin):
    alphabet, number, other = False, False, False
    length = False

    if admin:
        if len(password) > 10:
            length = True

        for char in password:
            if myisalpha(char):
                alphabet = True
            elif char.isdigit():
                number = True
            elif ord(char) in special:
                other = True

            if alphabet and number and other and length:
                return [True]

        return [alphabet, number, length, other]

    else:
        if len(password) > 7:
            length = True

        for char in password:
            if myisalpha(char):
                alphabet = True
            elif char.isdigit():
                number = True

            if alphabet and number and length:
                return [True]

        return [alphabet, number, length]


passwords = [["aabb11", False], ["123asd", False], [
    "as12vkasd", False], ["54alflfaa", False], ["aaaaaaa!!bbbb333", True], ["aaxmdd", True]]
asc = [x for x in range(65, 91)] + [y for y in range(97, 123)]
special = [z for z in range(33, 48)]


# print(check(password))
for password, flag in passwords:
    checksum = check(password, flag)
    if all(checksum):
        print("Strong")
    elif flag:
        if not checksum[0]:
            print("alphabet error")
        if not checksum[1]:
            print("number error")
        if not checksum[2]:
            print("length error")
        if not checksum[3]:
            print("special error")
    else:
        if not checksum[0]:
            print("alphabet error")
        if not checksum[1]:
            print("number error")
        if not checksum[2]:
            print("length error")


# print("aaaa\0bbbb11")
# print(int('a', 16))
# print([1, 2, 3] + [4, 5, 6])
