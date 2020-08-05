import re

case = int(input())

for i in range(case):
    instr = input()  # 와일드카드 문자열 입력
    newin = instr.replace('*', '.*').replace('?', '.')  # 와일드카드 문자열을 정규 표현식 형태로
    filename = []
    filenum = int(input())  # 파일의 수

    for k in range(filenum):
        filename.append(input())  # 파일이름 입력

    p = re.compile(newin)  # 정규표현식
    result = []

    for o in filename:  # 파일마다 검사
        if p.match(o):  # 파일이 와일드카드에 포함이 되고
            if p.match(o).group() == o:  # 포함된 것이 원래 파일과 같다면 (포함된 것이 다르면 답에 넣지 말아야 함)
                result.append(o)  # 답에 넣고

    result.sort()  # 정렬하고

    for j in result:  # 출력
        print(j)