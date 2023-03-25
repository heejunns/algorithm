# 백준 20291번, 파일 정리
import sys
n = int(sys.stdin.readline()) # 바탕화면의 파일 개수 n 입력받기
file_dict = {} # 파일의 확장자의 개수를 기록할 dict
for i in range(n):
    a,b = map(str,sys.stdin.readline().rstrip().split(".")) # 파일의 이름 입력받기, 
    # "." 을 기준으로 파일의 이름을 쪼개기, a 는 파일이름, b 는 확장자 이름
    if b not in file_dict: # file_dict 에 확장자 이름이 없다면 
        file_dict[b] = 1 # 등록
    else: # file_dict 에 확장자 이름이 있다면
        file_dict[b]+=1 # 해당하는 확장자 개수 +1
file_key_list = list(file_dict.keys()) # file_dict 의 key 를 리스트로 만들기
file_key_list.sort() # 오름차순으로 정렬
for i in file_key_list: # file_dict 의 key 를 오름차순 정렬한 리스트의 요소를 하나씩 꺼내기
    print(i, file_dict[i]) # key 와 key 에 해당하는 파일의 개수를 출력