from collections import deque
with open('output.txt', 'w') as out_file:
    with open('input.txt', 'r') as in_file:
        v = deque()
        is_dg = True
        n = int(in_file.readline())
        visited = []
        i = 0
        color = [ 0 for i in range(n)]
        matrix = [[int(i) for i in in_file.readline().split()] for _ in range(n)]
        while is_dg and len(visited) != n:
            while i in visited:
                i+=1
            visited.append(i)
            v.append(i)
            color[i] = True
            while v:
                this = v.popleft()
                for k in range(n):
                    if matrix[this][k]:
                        if k in visited:
                            if color[this] == color[k]:
                                is_dg = False
                                break
                        else:
                            color[k] = not color[this]
                            visited.append(k)
                            v.append(k)
        if is_dg:
            print('YES', file=out_file)
            string = '1'
            if sum(color) == n:
                for i in range(1, n - 1):
                    string += ' ' + str(i+1)
            else:
                for i in range(1, n):
                    if color[i]:
                        string += ' ' + str(i+1)
            print(string, file=out_file)
        else:
            print('NO', file=out_file)
