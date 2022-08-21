# Задача 2. В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.

def find_fruits(list, let):
    bbol = False
    for word in list:
        if word[0] == let:
            print(word)
            bbol = True
    if bbol == False:
        print(f"В файле отсутсвуют фрукты, которые начинаются на букву '{let}'")

letter = input("Введите букву: ")

fts = open('fruits.txt', 'r', encoding='utf-8')
data = fts.readlines()
fruits_list = data[0].split(' ')
print(fruits_list)
find_fruits(fruits_list, letter)
fts.close()


        
    

