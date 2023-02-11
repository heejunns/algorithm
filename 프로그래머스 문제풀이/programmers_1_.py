# 프로그래머스 level 0 , 옹알이
def solution(babbling):
    answer = 0 
    count = 0
    count_if = 0 
    str = ""
    x = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        count = 0 
        for l in i:
            str+=l
            if str in x:
                print(str)
                str = ""
                count+=1
        if count > 0 and str == "" :
            answer+=1
        else:
            str = ""
    print(answer)
    return answer

print(solution(["aya", "yee", "u", "maa", "wyeoo"])) 
