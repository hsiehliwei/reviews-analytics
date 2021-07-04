data = []
count = 0 #計算次數的變數
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count = count + 1 
        if count % 1000 == 0: # %為求餘數
            print(len(data))
print(len(data))
print('=================')
print(data[0])
print('=================')
print(data[1])
