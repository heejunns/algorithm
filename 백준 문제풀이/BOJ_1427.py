# 백준 1427번, 소트인사이드
n = list(input()) # 정렬하려는 수 입력받기, 각각의 요소들을 리스트로 만들기
result = list(map(int,n)) # 리스트의 각각의 요소들을 int 형으로 변환하기
result.sort(reverse=True) # 내림차순으로 정렬
result = list(map(str,result)) # 리스트의 각각의 요소들을 문자열로 변환
print("".join(result)) # join 함수로 다시 하나의 문자열로 만들기