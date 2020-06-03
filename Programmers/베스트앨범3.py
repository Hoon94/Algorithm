def solution(genres, plays):
    answer = []
    genre_total_play = {}
    genre_dic = {}
    
    for i in range(len(genres)):
        if genres[i] not in genre_dic.keys():
            genre_dic[genres[i]] = [(plays[i], i)]
            genre_total_play[genres[i]] = plays[i]
        else:
            genre_dic[genres[i]].append((plays[i], i))
            genre_total_play[genres[i]] = genre_total_play[genres[i]] + plays[i]
            
    # print(genre_total_play) 
    # print(genre_dic)
     
    sorted_total_play = sorted(genre_total_play.items(), key=lambda x: x[1], reverse=True)
    #print(sorted_total_play)
    
    for key in sorted_total_play:
        play_list = genre_dic[key[0]]
        
        play_list = sorted(play_list, key = lambda x : (-x[0], x[1]))
        #print(play_list)

        for i in range(len(play_list)):
            if i == 2:
                break
            answer.append(play_list[i][1])
            
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