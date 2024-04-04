# 리모컨

MAX_CHANNEL = 1000000
CURRENT_CHANNEL = 100

n = int(input())
m = int(input())

buttons = [True] * 10

not_work_btn_list = []
if m > 0:
  not_work_btn_list = list(map(int, input().split()))

for btn in not_work_btn_list:
  buttons[btn] = False

permutations = []

def get_channel(channel):
  if channel != '' and int(channel) > MAX_CHANNEL or len(channel) > 6:
    return
  if channel != '' and int(channel) <= MAX_CHANNEL:
    permutations.append(int(channel))
  
  for i in range(10):
    if buttons[i] and int(channel + str(i)) <= MAX_CHANNEL:
      get_channel(channel + str(i))

get_channel('')

def get_btn_count(channel, dist):
  if channel == CURRENT_CHANNEL:
    return dist
  else:
    return len(str(channel)) + dist

min_btn_cnt = get_btn_count(CURRENT_CHANNEL, abs(CURRENT_CHANNEL - n))

permutations = [CURRENT_CHANNEL] + permutations

for per in permutations:
  current_dist = abs(n - per)
  current_btn_cnt = get_btn_count(per, current_dist)
  if min_btn_cnt > current_btn_cnt:
    min_btn_cnt = current_btn_cnt

print(min_btn_cnt)