
morse = {
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-"
}

words = ["sun", "owl", "chameleon", "space", "family"]       #  Составляем список английских слов, которые будем расшифровывать.

import random                                                # Импортируем библиотеку

'''Функция, которая получает случайное слово из списка и возвращаем полученный случайный элемент'''
def get_word():
  random_word = random.choice(words)
  return random_word

'''
Функция, которая переводит слова на английском языке в последовательности точек и тирe
Создаем пустой список букв
В цикле перебираем каждую букву
По обращению к словарю morse получаем закодированную букву
Добавляем по одному значения (закодированные буквы) в конец к списку
Объединяем в строку все закодированные букы через пробел и получаем закодированное слово
Возвращаем закодированное слово
'''
def morse_encode(words):
  encoded_letters = []
  for letter in words:
    coded_letter = morse[letter]
    encoded_letters.append(coded_letter)
    encoded_word = " ".join(encoded_letters)
  return encoded_word


'''
Функция, которая выводит статистику ответов
Обнуление переменных, обозначающих верные и неверные ответы
Вводим переменную total - общее количество задач
В цикле перебираем каждый элемент в списке ответов
Инкриминируем количество верных и неверных ответов на  1
Выводим на печать статистику ответов
'''
def print_statistics(answers):
  correct_answers = 0
  uncorrect_answers = 0
  total = len(answers)
  for element in answers:
    if element == True:
      correct_answers += 1
    else:
      uncorrect_answers += 1
  print(f"Всего задачек: {total}\n"
        f"Отвечено верно: {correct_answers}\n"
        f"Отвечено неверно: {uncorrect_answers}")

# Приветствие при старте программы
print("Сегодня мы потренируемся расшифровывать морзянку.")
user = input("Нажмите Enter и начнем")
answers = []                                                # создаем пустой список ответов

for question in range(1, 6):                                # в цикле перебираем вопросы в диапазоне от 1 до 5 включительно
  random_word_new = get_word()                              # получаем случайное слово с помощью ранее написанной функции get_word()
  encoded_word = morse_encode(random_word_new)              # кодируем его с помощью ранее написанной функции
  print(f"Слово  {question} : {encoded_word}")              # выводим для пользователя
  answer = input().lower()                                  # получаем ответ от пользователя
  if answer == random_word_new:                             # сравниваем и если верно, то
        answers.append(True)                                # значение True добавляем в список ответов answers
        print(f"Верно, {random_word_new}!")                 # выводим на печать комментарий для пользователя
  else:                                                     # иначе
        answers.append(False)                               # значение False добавляем в список ответов answers
        print(f"Неверно, {random_word_new}!")               # выводим на печать комментарий для пользователя


print_statistics(answers)                                   # Вызываем функцию вывода статистики ответов



