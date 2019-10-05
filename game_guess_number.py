# Игра "Угадай число"
import random

print('Привет бро! Как тебя зовут игрок?')
name = input()
name = name.title()

def guessNumber():

    print('Окей, '+ name + ', я загадываю число от 1 до 20')

    number = random.randint(1,20)
    counter = 1

    for counter in range (6):
        print('Попробуй угадать')
        guess = input()


        while not guess.isdigit():
            print('должна быть цифра')
            guess = input()

        guess = int(guess)

        if guess > number:
            print('Твое число слишком большое')

        if guess < number:
            print('Твое число слишком маленькое')

        if guess == number:
            break

    if guess == number:
        counter = str(counter+1)
        print('Отлично '+name+'! Ты справился за '+counter+' попыток!')

    if guess != number:
        number = str(number)
        print('Увы, я загадала число '+number)

play_again = 'да'
while play_again == 'да':
    guessNumber()
    print('Попытаешь удачу ещё раз? (да или нет)')
    play_again = input()
    play_again = play_again.lower()

    while play_again not in {'да', 'нет'}:
        print("Должно быть да или нет")
        play_again = input()
        play_again = play_again.lower()
