data = []
count = 0
c = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		c = len(line) + c
		if count % 1000 == 0:
			#print(len(data))

print('讀取完畢，總共有：', len(data),' 筆資料')

b = len(data)
c = float(c)
b = float(b)

avg = c / b

print(avg)

sum_len = 0
for d in data:
	sum_len += len(d)
	#print(sum_len)

print('留言的平均長度是： ', sum_len/ len(data))


