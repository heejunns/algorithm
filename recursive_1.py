# 재귀함수의 조건을 명시한 예제 

def recursive_1(i):
    if i == 150:
        return
    print(i,"번째 재귀 함수에서 ",i+1,"번째 재귀 함수를 호출 합니다.")
    recursive_1(i+1)
    print(i,"번째 재귀 함수를 종료합니다.")

print(recursive_1(120))