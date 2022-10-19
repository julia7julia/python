string = input('')
while string != 'off':
    if string == 'game':
        print('угадай число')
        for i in range(3):
            number = input('')
            if number != '5':
                print('неверно')
            else:
                print('вы выиграли')
                break
    string = input('хотите сыграть')