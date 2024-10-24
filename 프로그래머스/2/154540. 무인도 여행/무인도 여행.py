from collections import deque

def solution(maps):
    answer = []
    row = len(maps)
    column = len(maps[0])

    visited = [[False] * column for _ in range(row)]
    parsed_maps = []
    for map in maps:
        parsed_maps.append(list(map))

    def bfs(start, maps, visited):
        queue = deque([start])
        max_date = 0
        while queue:
            [x, y] = queue.popleft()
            max_date += int(maps[x][y])
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                nx = x + dx
                ny = y + dy
                
                if 0 <= nx < row and 0 <= ny < column:
                    if visited[nx][ny] == False and maps[nx][ny] != 'X':
                    
                        visited[nx][ny] = True
                        queue.append([nx, ny])

        return max_date
    
    for x in range(0, row):
        for y in range(0, column):
            if visited[x][y] == False and parsed_maps[x][y] != 'X':
                visited[x][y] = True
                max_date = bfs([x, y], parsed_maps, visited)
                answer.append(max_date)
    
    if len(answer) == 0:
        return [-1]
    answer.sort()
    return answer