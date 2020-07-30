N = int(input())

data = []

for _ in range(N):
    data.append(int(input()))
data.sort()


for x in data:
    print(x)
#####################################


n1 = int(input())

array = list()

for _ in range(n1):
    array.append(int(input()))


for i in range(n1):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, n1):
        if array[min_index] > array[j]:
            min_index = j
            array[i], array[min_index] = array[min_index], array[i] # tmdhkvm


for i in array:
    print(i)



