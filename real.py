data = []
count = 0 #計算次數的變數
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count = count + 1 
        if count % 1000 == 0: # %為求餘數
            print(len(data))

print('檔案已經讀取完畢, 總共有', len(data), '筆資料')

sum_len = 0 #累積每筆留言長度的變數
for d in data:
    sum_len = sum_len + len(d)

print('每筆留言的平均為', sum_len / len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '筆留言長度<100')
print(new[0])
print(new[1])

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有', len(good), '筆留言提到good')