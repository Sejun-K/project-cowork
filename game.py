import random

rn = random.randint(1, 5)
gn = 0

count = 0

while rn !=gn :
    gn = int(input('랜덤 숫자를 추측해 보세요 : '))
    count += 1

print(f'축하합니다! {count}회 만에 맞췄습니다!')

