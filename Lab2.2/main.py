def output(arr):
    tmp = ""
    for i in range(len(arr)):
       tmp += str(arr[i]) + " "
    return tmp

print("Введіть ВІДСОРТОВАНИЙ масив (розділяючи пробілом): ")
strarr = input()
arr = []
for element in strarr.split(" "):
    arr.append(int(element))
print("Початковий масив: " + output(arr))

print("Введіть шукане число x: ")
x = int(input())

found = False
left = 0
right = len(arr) - 1

while left <= right:
    mid = round((right + left) / 2)
    if x == arr[mid]:
        print("Знайдено! Індекс: " + str(mid))
        found = True
        break
    elif x < arr[mid]:
        right = mid - 1
    else:
        left = mid + 1

if not found:
    print("Шуканого числа x не існує у масиві arr")