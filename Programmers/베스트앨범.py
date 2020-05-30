def solution(genres, plays):
    answer = []
    d = {}
    album = []
    
    for i in range(len(genres)):
        d[genres[i]] = d.get(genres[i], []) + [plays[i]]
        
    for i in d:
        d[i].sort()
        album.append([i, sum(d[i])])
    
    album.sort(key=lambda x : x[1], reverse=True)
    
    for i in album:
        for j in range(2):
            if len(d[i[0]]) == 0:
                break
            where = plays.index(d[i[0]][-1])
            answer.append(where)
            plays[where] = -1
            d[i[0]] = d[i[0]][:-1]
    
    return answer

if __name__ == "__main__":

    #Test case 1    
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    #result [4, 1, 3, 0]

    print(solution(genres, plays))