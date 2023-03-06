# 백준 10816번, 숫자 카드
import sys
n = int(sys.stdin.readline()) # n 의 카드 개수 입력 받기
my_card = list(map(int,sys.stdin.readline().split())) # 상근이가 가지고 있는 카드 입력 받기
m = int(sys.stdin.readline()) # m 의 카드 개수 입력 받기
m_card = list(map(int,sys.stdin.readline().split())) # m 개의 상근이가 몇개 가지고 있는 숫자 카드인지 구해야 할 m 개의 카드 입력 받기
m_dict = {} # dict 생성
for i in m_card: # m_card 를 dict 으로 생성
    m_dict[i] = 0
for l in my_card:
    if l not in m_dict: continue # my_card 의 카드가 m_dict 에 없다면 continue
    m_dict[l]+=1
for i in m_card: # m_card 에 중복되어 있는 카드가 있을 수 있기 때문에 m_card 의 원소의 개수를 출력
    print(m_dict[i], end = " ")