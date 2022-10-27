#Напишите программу, удаляющую из текста все слова, содержащие "абв". 
#Функции FIND и COUNT юзать нельзя.

givenText = 'АБВ Сказка посвящена АБВ истории женитьбы АБВ царя Салтана и АБВ рождению его сына,князя Гвидона.'
print(f"Заданный текст: {givenText}")

changedText = "АБВ"
lst = [i for i in givenText.split() if changedText not in i]
print(f'Результат: {" ".join(lst)}')
