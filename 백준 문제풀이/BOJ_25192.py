# 백준 25192번, 인사성 밝은 곰곰이 
import sys
n = int(sys.stdin.readline()) # 채팅방의 기록수 n 입력받기
gom_gom_ticon_count = 0 # 곰곰티콘 사용 횟수 기록하는 변수
chat_remember_dict = {} # 채팅을 입력한 유저의 닉네임을 저장할 dict
for i in range(n):
    chat = sys.stdin.readline().rstrip() # 새로운 사람의 입장 또는 채팅을 입력한 유저의 닉네임 입력받기
    if chat == "ENTER": # ENTER 라면 새로운 사람이 입장했기 때문에 이전에 채팅을 입력한 유저의 닉네임 초기화
        chat_remember_dict = {}
    elif chat not in chat_remember_dict: # 채팅을 입력한 유저의 닉네임이 dict 에 없다면
        chat_remember_dict[chat] = 0 # dict 에 닉네임 저장 값으로는 임의의 수 0 사용
        gom_gom_ticon_count+=1 # 곰곰티콘 사용횟수 +1
print(gom_gom_ticon_count)
    
