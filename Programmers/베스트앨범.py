def solution(genres, plays):
    answer = []
    d = {}
    d_r = {}
    album = []
    
    for i in range(len(genres)):
        d[genres[i]] = d.get(genres[i], []) + [[plays[i], i]]
        d_r[genres[i]] = d_r.get(genres[i], 0) + plays[i]
    
    album = list(d_r.items())
    album.sort(key=lambda x : x[1], reverse=True)
    
    for i in d:
        d[i].sort(key=lambda x : x[0])
            
    for i in range(len(album)):
        for j in range(2):
            if len(d[album[i][0]]) == 0:
                continue
            answer.append(d[album[i][0]][-1][1])
            d[album[i][0]] = d[album[i][0]][:-1]
        
    print(album)
    print(d_r)
    print(d)
    print(answer)
    return answer

if __name__ == "__main__":

    #Test case 1    
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    #result [4, 1, 3, 0]

    print(solution(genres, plays))