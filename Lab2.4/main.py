def output(arr):
    tmp = ""
    for i in range(len(arr)):
       tmp += str(arr[i]) + " "
    return tmp

print("Введіть масив (розділяючи пробілом): ")
strarr = input()
arr = []
for element in strarr.split(" "):
    arr.append(int(element))
print("Початковий масив: " + output(arr))
length = len(arr)

for i in range(length):
    minindex = i
    for j in range(i+1, length):
        if arr[minindex] > arr[j]:
            minindex = j
    arr[i], arr[minindex] = arr[minindex], arr[i]

print("Відсортований масив: " + output(arr))
        