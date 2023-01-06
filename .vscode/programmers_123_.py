# 프로그래머스 숫자 짝꿍 (level 1)
def solution(X, Y):
    answer = ""
    total = []
    for i in range(10):
        if str(i) in X and str(i) in Y:
            if X.count(str(i)) >= Y.count(str(i)):
                    total.extend([str(i)]*(Y.count(str(i))))
            else:
                total.extend([str(i)]*(X.count(str(i))))
    total.sort(reverse=True)
    if total == []: 
        answer="-1"
    elif total[0] == "0" and total[-1] == "0": # 첫번째 인덱스와 마지막 인덱스가 0이라는 말은 모든 원소가 0이라는 뜻이니까
        answer="0"
    else:
        answer = "".join(total)
    return answer