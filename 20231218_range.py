# for_range

range(3) # [0, 1, 2]
range(5) # [0, 1, 2, 3, 4]
range(2,5) # [2, 3, 5] 含頭不含尾
range(2,10,3) # [2, 5, 8] (start, end, plus)
range(10,3,-2) # [10, 8, 6, 4]

import random

for i in range(10):
	r = random.randint(0, 100) # 產生0~100間的隨機數
	print(r)