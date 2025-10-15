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

for i in range(length-1):
    for j in range(length-i-1):
        if arr[j] > arr[j+1]:
            tmp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = tmp

print("Відсортований масив: " + output(arr))