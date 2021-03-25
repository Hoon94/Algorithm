def solution(food_times, k):
    answer = -1
    times = food_times[:]
    eat = 0
    types = len(food_times)

    while times and k >= min(times) * types:
        k -= min(times) * types
        eat += min(times)
        types -= 1
        times = [x - min(times) for x in times if x - min(times)]
        print(times, min(times), food_times)

    if k >= types:
        k = k % types

    answer = food_times.index(times[k] + eat) + 1 if times else -1
    return answer


if __name__ == '__main__':
    food_times = [3, 3, 2]
    k = 4

    print(solution(food_times, k))
