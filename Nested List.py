if __name__ == '__main__':
    
    N = int(input())
    score_list =[]
    record = []
    name_list = []
    for i in range(N):
        name = input()
        score = float(input())
        st = [name,score]
        record.append(st)
    
    
    for i in range(N):
        score_list.append(record[i][1])

    score_list.sort()

    for i in range(N):
        if score_list[i]<score_list[i+1]:
            second_last = score_list[i+1]
            break
    
    for i in range(N):
        if record[i][1]==second_last:
            name_list.append(record[i][0])
    
    name_list.sort()
    for i in name_list:
        print(i)

"""







