# -*- coding: utf-8 -*-

import random


def get_random_number() -> int:
    return random.randrange(100, 1000)


def is_digit(user_input_number : str) -> bool:
    result = None

    # try:
    #     if int(user_input_number):
    #         result = True
    #     return result

    # except Exception:
    #     result = False
    #     return result

    if user_input_number.isdigit():
        result = True
    else:
        result = False

    return result


def is_between_100_and_999(user_input_number : str) -> bool:
    result = None

    if 100 <= int(user_input_number) and int(user_input_number) < 1000:
        result = True
    else:
        result = False

    return result


def is_duplicated_number(three_digit : str) -> bool:
    result = None

    for num in three_digit:
        if three_digit.count(num) > 1:
            result = True
            break
    else:
        result = False

    return result


def is_validated_number(user_input_number : str) -> bool:
    result = None

    if is_digit(user_input_number) \
        and is_between_100_and_999(user_input_number) \
            and not is_duplicated_number(user_input_number):
            
            result = True
    else:
        result = False

    return result


def get_not_duplicated_three_digit_number() -> int:
    result = "333"

    while is_duplicated_number(result):
        result = get_random_number()

    return result


def get_strikes_or_ball(user_input_number : str, random_number : str) -> list:
    result = None

    strike, ball = 0, 0

    for index, num in enumerate(user_input_number):
        if num in random_number:
            if num == random_number[index]: # strike
                strike += 1
            else: # ball
                ball += 1

    result = [strike, ball]
    return result


def is_yes(one_more_input : str) -> bool:
    result = None

    if str(one_more_input).lower() == 'y' or str(one_more_input).lower() == 'yes':
        result = True
    else:
        result = False

    return result


def is_no(one_more_input):
    result = None

    if str(one_more_input).lower() == 'n' or str(one_more_input).lower() == 'no':
        result = True
    else:
        result = False

    return result


def main():
    print("Play Baseball")
    random_number = str(get_not_duplicated_three_digit_number())
    print("Random Number is : ", random_number)
    # ===Modify codes below=============
    # 위의 코드를 포함하여 자유로운 수정이 가능함
    check = True
    while check:
        user_input = input("Input guess number :")
        if is_yes(user_input) or is_no(user_input) or is_validated_number(user_input):
            pass
        elif user_input == '0':
            break
        else:
            print("Wrong Input, Input again")
            continue

        count = get_strikes_or_ball(user_input, random_number)
        print(f"Strikes : {count[0]} , Balls : {count[1]}")

        if count[0] == 3:
            again = input("You win, one more(Y/N) ?")
            if is_yes(again):
                return True
            elif is_no(again):
                return False

    # ==================================
    print("Thank you for using this program")
    print("End of the Game")

    return False

if __name__ == "__main__":
    check = True
    while True:
        check = main()
