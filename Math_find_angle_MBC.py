#Hackkerarnk_ques_link: https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true

# Solution:
import math
ab = int(input())
bc = int(input())
ac = math.sqrt(pow(ab, 2)+pow(bc, 2))

theta = str(int(round(math.degrees(math.atan2(ab, bc)))))

print(f"{theta}\u00b0")