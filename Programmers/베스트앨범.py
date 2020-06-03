def solution(genres, plays):
    answer = []
    d = {}
    album = {}
    
    for i in range(len(genres)):
        d[genres[i]] = d.get(genres[i], []) + [[plays[i], i]]
        album[genres[i]] = album.get(genres[i], 0) + plays[i]
        
    for i in d:
        d[i].sort(key= lambda x : (x[0], -x[1]))
    
    s_album = sorted(album.items(), key= lambda x : x[1], reverse=True)

    print(d)
    
    for i in s_album:
        for j in range(2):
            if len(d[i[0]]) == 0:
                break
            answer.append(d[i[0]][-1][1])
            d[i[0]] = d[i[0]][:-1]

    return answer

if __name__ == "__main__":

    '''
    #Test case 1
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    #result [4, 1, 3, 0]
    '''

    #Test case 2
    genres = ["pop", "classic", "classic", "classic", "pop"]
    plays = [500, 500, 150, 800, 500]
    #result [3, 1, 0, 4]

    print(solution(genres, plays))