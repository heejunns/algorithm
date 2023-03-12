# 백준 1235 번, 학생 번호
import sys
n  = int(sys.stdin.readline()) # 학생의 수 입력받기
k = -1 # k 자리, 뒤에서부터 자리수를 세야 하니까 -1 부터 시작
student_list = [] # 학생의 번호를 입력받아 저장할 리스트
for i in range(n): # 각각의 학생의 번호를 입력받아 저장하기
    student_number = sys.stdin.readline().rstrip()
    student_list.append(student_number)
while True :
    same_check = [] # 같은 번호가 있는지 체크하기 위해 중복되는 번호가 아니면 저장할 리스트
    for i in student_list:
        if i[k:] not in same_check: # same_check 에 없다면 리스트에 저장
            same_check.append(i[k:])    
    if len(same_check) == 0: # smae_check 의 길이가 0 이라면 중복되는 번호가 없다는 뜻이니까 while 문 탈출
        break  
    k-=1
 
print(abs(k)) # k 자리 수를 출력 하는 거니까 k 의 절대값 출력하기

        
