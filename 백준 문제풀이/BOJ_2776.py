# 백준 27576 번, 암기왕
import sys
result = [] # 수첩 2에 적혀있는 내용이 수첩1에 있는지 확인하여 결과를 저장하는 리스트
test_number =int(sys.stdin.readline()) # 테스트 케이스 개수를 입력받기
for i in range(test_number):
    n_dict = {} # 수첩1의 정수들을 n_dict 으로 dict 으로 저장
    n = int( sys.stdin.readline()) # 수첩1에 적어 놓은 정수의 개수 입력받기
    n_list = list(map(int, sys.stdin.readline().rstrip().split()))  # 수첩1에 적혀있는 각각의 정수를 입력받기
    for j in n_list: # 입력받은 각각의 수첩1의 정수를 dict 으로 저장
        n_dict[j] = 0 # 수첩1의 각각의 정수를 key 값으로 dict 에 저장, value 값은 임의의 0 저장
    m = int( sys.stdin.readline()) # 수첩2에 적어 놓은 정수의 개수 입력받기
    m_list =  list(map(int, sys.stdin.readline().rstrip().split())) # 수첩2에 적어 놓은 각각의 정수 입력받기
    for l in m_list: # 입력받는 수첩2의 각각의 정수를 하나씩 꺼내기
        if l in n_dict: # 꺼낸 정수가 수첩1의 dict에 있다면
            result.append(1)
        else: # 꺼낸 정수가 수첩1의 dict에 없다면
            result.append(0)
for k in result:
    print(k)

