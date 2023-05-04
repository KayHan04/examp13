price_all = 0 # счетчик
while True:
        ticket_number = input(f'Сколько билетов вы хотите приобрести ? ')
        ticket_number = int(ticket_number)
        if type(ticket_number) == int:
            break
        print(f'Введите целое число')
for i in range(ticket_number):
    i += 1
    while True:
            age_for_ticket = input(f'Для какого возраста билет №{i}? ')
            age_for_ticket = int(age_for_ticket)
            if age_for_ticket < 18:
                print(f'Билет бесплатный')
            elif 25 > age_for_ticket >= 18:
                price_all += 990
                print(f'Стоимость билета: 990 руб.')
            else:
                price_all += 1390
                print(f'Стоимость билета: 1390 руб.')
            if type(age_for_ticket) == int:
                break
if ticket_number > 3:
    price_all = price_all - ((price_all / 100) * 10)
    print(f'Сумма к оплате {price_all} руб. с учетом 10%-ой скидки  за регистрацию больше 3-х человек')
else:
    print(f'Сумма к оплате {price_all} руб.')