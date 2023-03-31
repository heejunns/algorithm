# 백준 25757번, 임스와 함계하는 미니게임
import sys
n, gameMode = map(str,sys.stdin.readline().rstrip().split()) # 플레이하기를 신청한 횟수 n, 플레이할 게임의 종류 입력받기
games = {"Y":2,"F":3,"O":4} # 게임의 종류에 따라서 플레이 할 수 있는 명수 dict 에 저장하기
game_player_list = {} # 게임을 플레이한 사람의 이름을 저장할 dict
game = [] # 현재 게임을 하고 있는 사람을 저장할 리스트
game_count = 0 # 플레이한 게임의 횟수 기록
for i in range(int(n)):
    game_player = sys.stdin.readline().rstrip() # 같이 플레이하는 사람들의 이름 입력받기
    if game_player not in game_player_list : # 게임을 플레이한 사람의 명단에 없다면
        game_player_list[game_player] = 0 # dict 에 저장
        game.append(game_player) # 현재 게임 플레이어로 추가
    if games[gameMode]-1 == len(game): # 임스의 인원은 빼고 현재 게임을 플레이할 사람의 인원과 게임을 진행해야 할 인원이 같다면
        game = [] # 현재 게임을 하고 있는 리스트 초기화
        game_count+=1 # 게임을 플레이한 횟수 +1
print(game_count)
        

