def output(arr):
    tmp = ""
    for i in range(len(arr)):
       tmp += str(arr[i]) + " "
    return tmp

print("Введіть довжину масиву: ")
length = int(input())
arr = []
print("Введіть елементи масиву: ")
for i in range(length):
    arr.append(int(input()))
print("Введіть шукане значення: ")
x = int(input())

print("Початковий масив: \n" + output(arr))

found = False
for i in range(length):
    if x == arr[i]:
        found = True
        print("Знайдено! Індекс: " + str(i))
        break

if not found:   
    print("Шуканого числа x не існує у масиві arr")