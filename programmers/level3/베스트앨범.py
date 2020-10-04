def solution(genres, plays):
    answer = []
    musics = {}
    for i in range(len(genres)):
        if genres[i] not in musics:
            musics[genres[i]] = [plays[i], {i : plays[i]}]
        else:
            musics[genres[i]][0] += plays[i]
            musics[genres[i]][1][i] = plays[i]
    sortByTotal = sorted(musics.items(), key=(lambda x: x[1][0]), reverse=True)
    for i in range(len(sortByTotal)):
        sortByPlays = sorted(sortByTotal[i][1][1].items(), key=(lambda x: x[1]), reverse=True)[:2]
        for g in sortByPlays:
            answer.append(g[0])

    return answer

print(solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500]))