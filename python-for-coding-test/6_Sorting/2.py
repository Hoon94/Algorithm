# 0 인덱스와 1 인덱스의 원소 교체하기
array = [3, 5]
array[0], array[1] = array[1], array[0]

print(array)

"""
C 언어로 구현한 스와프 예제
다른 대부분의 프로그래밍 언어에서는 명시적으로 임시 저장용 변수(temp)를 만들어 두 원소의 값을 변경해야 한다.

int a = 3;
int b = 5;

스와프 진행
int temp = a;
a = b;
b = temp;
"""
