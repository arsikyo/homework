try:
    temperature, pressure, pulse = map(float, input('Введите вашу температуру, давление и пульс через пробел').split())
    if (temperature>=36 and temperature<=37) and (pressure>=110 and pressure<=130) and (pulse>=60 and pulse<=100) :
        print('Ваше состояние в норме')
    elif (temperature>=35 and temperature<36) or (temperature>37 and temperature<=38) and (pressure>=105 and pressure<110) or (pressure>130 and pressure<=140) and (pulse>=55 and pulse<60) or (pulse>100 and pulse<=110):
        print('У вас легкое недомогание')
    elif temperature<35 or temperature>38 or pressure<105 or pressure>140 or pulse<55 or pulse>110:
        print('Вам срочно требуется врач')
except ValueError:
    print('Ошибка ввода: введите корректные занчения')