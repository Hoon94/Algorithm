# answer에 넣고 계속 확인해보자..
# https://programmers.co.kr/learn/courses/30/lessons/60061
n = 5
build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [
    1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]


def make_pillar(frame, answer):

    x = frame[0]
    y = frame[1]
    # a = frame[2]

    if y == 0:  # 바닥
        answer.append(frame)
    elif [x, y-1, 0] in answer:  # 다른 기둥
        answer.append(frame)
    elif ([x-1, y, 1] in answer) or ([x, y, 1] in answer):  # 양쪽이 보
        answer.append(frame)

    print("make_pillar")
    print(answer)


def make_step(frame, answer):

    x = frame[0]
    y = frame[1]
    # a = frame[2]

    if ([x, y-1, 0] in answer) or ([x+1, y-1, 0] in answer):  # 한쪽이 기둥
        answer.append(frame)
    elif ([x-1, y, 1] in answer) and ([x+1, y, 1] in answer):  # 양쪽이 보
        answer.append(frame)
    print("make_step")
    print(answer)


def del_pillar(frame, answer):
    x = frame[0]
    y = frame[1]
    a = frame[2]

    nx = ny = na = 0
    # direction = 0

    dx = [-1, 1, 0, 0, 0, -1]
    dy = [1, 0, 0, -1, -1, 1]
    da = [1, -1, 1, 0, -1, 1]

    answer.remove(frame)  # 지우고 뒤에 확인

    for i in range(6):  # 다시 만들어야 할 것이 있는지를 찾는 것
        pre_len = 0
        nx = x + dx[i]
        ny = y + dy[i]
        na = a + da[i]
        if [nx, ny, na] in answer:
            if na == 0:  # 기둥을 지우고 다시 만들기
                pre_len = len(answer)
                answer.remove([nx, ny, na])
                make_pillar([nx, ny, na], answer)
                if pre_len != len(answer):  # 다시만들었을 때 다르다면 지운거 복구.
                    answer.append(frame)
                    break
                else:  # 다시만들었는데 같다 -> 지워도 된다.
                    break
            elif na == 1:
                pre_len = len(answer)
                answer.remove([nx, ny, na])
                make_step([nx, ny, na], answer)
                if pre_len != len(answer):  # 다시만들었을 때 다르다면 지운거 복구.
                    answer.append(frame)
                    break
                else:
                    break

    print("del_pillar")
    print(answer)


def del_step(frame, answer):
    x = frame[0]
    y = frame[1]
    a = frame[2]

    nx = ny = na = 0
    # direction = 0

    dx = [0, -1, 1, 1, 0, 0]
    dy = [-1, 1, 0, 0, 0, -1]
    da = [-1, 1, -1, 0, 1, -1]

    answer.remove(frame)  # 지우고 뒤에 확인

    for i in range(6):  # 다시 만들어야 할 것이 있는지를 찾는 것
        pre_len = 0
        nx = x + dx[i]
        ny = y + dy[i]
        na = a + da[i]
        if [nx, ny, na] in answer:
            if na == 0:  # 기둥을 지우고 다시 만들기
                pre_len = len(answer)
                answer.remove([nx, ny, na])
                make_pillar([nx, ny, na], answer)
                if pre_len != len(answer):  # 다시만들었을 때 다르다면 지운거 복구.
                    answer.append([nx, ny, na])
                    answer.append(frame)
                    break
                else:  # 다시만들었는데 같다 -> 지워도 된다.
                    break
            elif na == 1:
                pre_len = len(answer)
                answer.remove([nx, ny, na])
                make_step([nx, ny, na], answer)
                if pre_len != len(answer):  # 다시만들었을 때 다르다면 만들수 없는 것.
                    answer.append(frame)
                    answer.append([nx, ny, na])
                    break
                else:
                    break

    print("del_step")
    print(answer)


def solution(n, build_frame):
    answer = []
    # x = y = a = b = 0

    for frame in build_frame:
        a = frame[2]
        b = frame[3]
        frame = frame[:3]

        if a == 0 and b == 0:
            del_pillar(frame, answer)
        elif a == 0 and b == 1:
            make_pillar(frame, answer)
        elif a == 1 and b == 0:
            del_step(frame, answer)
        else:
            make_step(frame, answer)
    answer = sorted(answer, key=lambda x: (x[0], x[1], x[2]))
    return answer


print(solution(n, build_frame))
