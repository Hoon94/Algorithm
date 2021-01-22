import re

def solve(s, p):
    pattern = re.compile(f'{p}')

    #print([pattern])
    #print(pattern.match('aaac'))
    print(pattern)
    result = pattern.match(s).group() if pattern.match(s) else None
    print(result)

    if s == result:
        return True
    else:
        return False

s = 'ab'
p = '.*c'
print(solve(s, p))


# pattern = re.compile('b*')
# print(pattern)

# pattern.match('aaaaa')
# # <_sre.SRE_Match object; span=(0, 5), match='aaaaa'>

# result = pattern.match('bbbbbbbbb')
# # <_sre.SRE_Match object; span=(0, 9), match='bbbbbbbbb'>

# print(result.group())
# # aaa

# print(result.start())
# # 1

# print(result.end())
# # 4

# print(result.span())
# # (1, 4)

# pattern.match('1aaaa')
# # None

# pattern.match('aaa1aaa')
# # <_sre.SRE_Match object; span=(0, 3), match='aaa'>

# pattern.search('aaaaa')
# # <_sre.SRE_Match object; span=(0, 5), match='aaaaa'>

# pattern.search('11aaaa')
# # <_sre.SRE_Match object; span=(2, 6), match='aaaa'>

# pattern.search('aaa11aaa')
# # <_sre.SRE_Match object; span=(0, 3), match='aaa'>

# pattern.search('1aaa11aaa1')
# # <_sre.SRE_Match object; span=(1, 4), match='aaa'>

# pattern.findall('aaa')
# # ['aaa']

# pattern.findall('11aaa')
# # ['aaa']

# pattern.findall('1a1a1a1a1a')
# # ['a', 'a', 'a', 'a', 'a']

# pattern.findall('1aa1aaa1a1aa1aaa')
# # ['aa', 'aaa', 'a', 'aa', 'aaa']

# pattern.finditer('a1bb1ccc')
# # <callable_iterator object at 0x7f850c4285f8>

# f_iter = pattern.finditer('a1bb1ccc')
# for i in f_iter:
#     print(i)

# pattern = re.search('(hello)(world)', 'helloworld')
# print(pattern)
# grouping = pattern.groups()
# print(grouping)

# print(pattern.group())

# print(pattern.group(0))

# print(pattern.group(1))

# print(pattern.group(2))

# pattern = re.match('(?P<first>hello)(?P<second>world)', 'helloworld')
# print(pattern)
# grouping = pattern.groups()
# print(grouping)

# print(pattern.group())

# print(pattern.group(0))

# print(pattern.group(1))

# print(pattern.group(2))
