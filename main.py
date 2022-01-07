from tkinter import *
import time

#main data
full_name = 'Турчинович М. А.'
password = '5555'
balance = 100000.00
sms = True
expiration_date = '06.2025'
card = False


#creating a screen for an ATM
root = Tk()
root.title("MASHA'S BANK")
root.geometry('1200x800')
root.resizable(width=False, height=False)

photo = PhotoImage(file = 'ATM_back.png')
screen = Label(root, image=photo, bd=0)
screen.pack()

ent = Entry(root)
ent.pack()
ent.focus_set()


number_wrong_attempts = 3
number_check = 3

def attaching_card():
    """Attaching a card to an ATM"""
    contactless_payment.place_forget()
    button_insert_card.place_forget()
    img_card = PhotoImage(file='attaching_card.png')

    l = Label(image=img_card, bg='#929CC3')
    l.img = img_card
    l.place(x=1200, y=560)
    num = 1200

    for i in range(1, 245):
        num -= 1
        l.place(x=num, y=560)
        root.update()
        time.sleep(0.01)
    for i in range(1, 245):
        num += 1
        l.place(x=num, y=560)
        root.update()
        time.sleep(0.01)

    pass_entry()

def insert_card():
    """Inserting a card into an ATM"""
    global card
    contactless_payment.place_forget()
    button_insert_card.place_forget()
    for i in range(1, 44):
        name = 'insert_card_' + str(i) + '.png'
        img_ins_card = PhotoImage(file=name)
        screen.configure(image=img_ins_card)
        root.update()
        time.sleep(0.05)

    screen.configure(image=photo)
    card = True
    pass_entry()


def insert_cash():
    """Cash deposit at ATM"""
    label_information_check.place_forget()
    for i in range(1, 20):
        name = 'accepting_cash_' + str(i) + '.png'
        img_ins_cash = PhotoImage(file=name)
        screen.configure(image=img_ins_cash)
        root.update()
        time.sleep(0.05)

    screen.configure(image=photo)
    menu()

def get_card():
    """Getting the card back"""
    global card
    label_sms_disable.place_forget()
    label_sms_false.place_forget()
    label_sms_true.place_forget()
    label_sms_turn.place_forget()
    label_inf.place_forget()
    label_back_services.place_forget()
    label_number_attempts.place_forget()
    label_back_exit.place_forget()
    label_back_forth.place_forget()
    label_2.place_forget()
    label_menu.place_forget()

    for i in range(43, 0, -1):
        name = 'insert_card_' + str(i) + '.png'
        img_ins_card = PhotoImage(file=name)
        screen.configure(image=img_ins_card)
        root.update()
        time.sleep(0.05)
    time.sleep(0.1)

    screen.configure(image=photo)
    card = False

def close_window():
    """Closing the window"""
    if card:
        get_card()
    root.destroy()

def insert_cash_with_check():
    """Cash deposit into ATM with check"""
    label_information_check.place_forget()
    for i in range(1, 20):
        name = 'accepting_cash_' + str(i) + '.png'
        img_ins_cash = PhotoImage(file=name)
        screen.configure(image=img_ins_cash)
        root.update()
        time.sleep(0.1)
    time.sleep(0.1)
    screen.configure(image=photo)
    print_check()

def print_check():
    """Function that prints a receipt"""
    label_information_check.place_forget()

    for i in range(1, 20):
        name = 'print_check_' + str(i) + '.png'
        img_print_check = PhotoImage(file=name)
        screen.configure(image=img_print_check)
        root.update()
        time.sleep(0.1)

    screen.configure(image=photo)
    menu()

def withdrawal_cash_with_check():
    """Cash withdrawal from ATM with check"""
    label_information_check.place_forget()
    for i in range(19, 0, -1):
        name = 'accepting_cash_' + str(i) + '.png'
        img_ins_cash = PhotoImage(file=name)
        screen.configure(image=img_ins_cash)
        root.update()
        time.sleep(0.1)
    time.sleep(0.1)
    screen.configure(image=photo)
    print_check()

def withdrawal_cash_without_check():
    """Cash withdrawal from ATM without check"""
    label_information_check.place_forget()
    for i in range(19, 0, -1):
        name = 'accepting_cash_' + str(i) + '.png'
        img_ins_cash = PhotoImage(file=name)
        screen.configure(image=img_ins_cash)
        root.update()
        time.sleep(0.1)
    time.sleep(0.1)
    screen.configure(image=photo)
    menu()

def pass_entry():
    """Entering a PIN code into an ATM"""
    global num_1, num_2, num_3, num_4, num_5, num_6, num_7, num_8, num_9, num_00, num_0, num_point, clear, cancel, \
        enter, password
    label_2.configure(text='Введите ПИН-код', bg='#E5E5E4', height=1, width=40)
    label_2.place(x=258, y=150)
    pass_pin = Entry(root, bd=0, bg='#EFEFEF', show='*', font=('Arial', 50))
    pass_pin.place(x=545, y=210, width=110, height=60)

    #function for different button

    def get_num(num):
        if len(pass_pin.get()) < 4:
            pass_pin.insert(len(pass_pin.get()), str(num))

    def get_num_00():
        if len(pass_pin.get()) < 3:
            pass_pin.insert(len(pass_pin.get()), '00')
        if len(pass_pin.get()) == 3:
            pass_pin.insert(4, '0')

    def pin_clear():
        if len(pass_pin.get()) > 0:
            pass_pin.delete(0, len(pass_pin.get()))

    def pin_cancel():
        if len(pass_pin.get()) > 0:
            pass_pin.delete(len(pass_pin.get()) - 1)

    def pin_enter():
        if pass_pin.get() == password:
            label_2.place_forget()
            pass_pin.destroy()
            num_0['command'] = ''
            num_1['command'] = ''
            num_2['command'] = ''
            num_3['command'] = ''
            num_4['command'] = ''
            num_5['command'] = ''
            num_6['command'] = ''
            num_7['command'] = ''
            num_8['command'] = ''
            num_9['command'] = ''
            num_00['command'] = ''
            clear['command'] = ''
            cancel['command'] = ''
            enter['command'] = ''
            menu()
        else:
            check_pass_pin()

    def check_pass_pin():
        """PIN code check"""
        global number_wrong_attempts
        number_wrong_attempts -= 1
        label_number_attempts['text'] = 'Количество оставшихся попыток: ' + str(number_wrong_attempts)
        label_number_attempts.place(x=258, y=300)

        if number_wrong_attempts != 0:
            pass_pin.delete(0, 4)
            label_2.place_forget()
            label_2['text'] = 'Введён неверный ПИН-код!\nВведите ещё раз:'
            label_2['height'] = 3
            label_2.place(x=258, y=110)
            return

        else:
            label_2.place_forget()
            pass_pin.destroy()
            label_2['text'] = 'Количество попыток закончилось!\nКарта заблокирована!\nДля работы банкомата ' \
                              'перезапустите программу.'
            label_2['height'] = 5
            label_2.place(x=258, y=120)
            num_0['command'] = ''
            num_1['command'] = ''
            num_2['command'] = ''
            num_3['command'] = ''
            num_4['command'] = ''
            num_5['command'] = ''
            num_6['command'] = ''
            num_7['command'] = ''
            num_8['command'] = ''
            num_9['command'] = ''
            num_00['command'] = ''
            clear['command'] = ''
            cancel['command'] = ''
            enter['command'] = ''


    num_0['command'] = lambda: get_num(0)
    num_1['command'] = lambda: get_num(1)
    num_2['command'] = lambda: get_num(2)
    num_3['command'] = lambda: get_num(3)
    num_4['command'] = lambda: get_num(4)
    num_5['command'] = lambda: get_num(5)
    num_6['command'] = lambda: get_num(6)
    num_7['command'] = lambda: get_num(7)
    num_8['command'] = lambda: get_num(8)
    num_9['command'] = lambda: get_num(9)
    num_00['command'] = get_num_00
    clear['command'] = pin_clear
    cancel['command'] = pin_cancel
    enter['command'] = pin_enter


#Creation of the main labels and buttons for the ATM
img_menu = PhotoImage(file='MENU.png')
label_menu = Label(image=img_menu, bg='#E5E5E4')
label_menu.img = img_menu
label_menu.place(x=279, y=100)
label_menu.place_forget()

img_back_forth = PhotoImage(file='back_forth.png')
label_back_forth = Label(image=img_back_forth, bg='#E5E5E4')
label_back_forth.img = img_back_forth
label_back_forth.place(x=279, y=400)
label_back_forth.place_forget()

img_information_check = PhotoImage(file='check_function.png')
label_information_check = Label(image=img_information_check, bg='#E5E5E4')
label_information_check.img = img_information_check
label_information_check.place(x=279, y=400)
label_information_check.place_forget()

sum_money = Entry(root, bd=0, bg='#EFEFEF', font=('Arial', 25))
sum_money.place(x=392, y=210, width=410, height=50)
sum_money.place_forget()

img_back_exit = PhotoImage(file='back_exit.png')
label_back_exit = Label(image=img_back_exit, bg='#E5E5E4')
label_back_exit.img = img_back_exit
label_back_exit.place(x=279, y=400)
label_back_exit.place_forget()


label_number_attempts = Label(root, text='Количество оставшихся попыток: ' + str(number_wrong_attempts), bg='#E5E5E4',
                                fg='#2C2A30', font=('Arvo', 20, 'bold'), height=1, width=40)
label_number_attempts.place(x=258, y=300)
label_number_attempts.place_forget()

label_no_cash = Label(root, text='Недостаточно средств на карте!', bg='#E5E5E4', fg='#AC3535',
                      font=('Arvo', 20, 'bold'), height=1, width=40)
label_no_cash.place(x=258, y=300)
label_no_cash.place_forget()

img_back_services = PhotoImage(file='back_services.png')
label_back_services = Label(image=img_back_services, bg='#E5E5E4')
label_back_services.img = img_back_services
label_back_services.place(x=279, y=400)
label_back_services.place_forget()

#work with messages
img_sms_disable = PhotoImage(file='sms_disable.png')
label_sms_disable = Label(image=img_sms_disable, bg='#E5E5E4')
label_sms_disable.img = img_sms_disable
label_sms_disable.place(x=279, y=200)
label_sms_disable.place_forget()

img_sms_false= PhotoImage(file='sms_false.png')
label_sms_false = Label(image=img_sms_false, bg='#E5E5E4')
label_sms_false.img = img_sms_false
label_sms_false.place(x=279, y=400)
label_sms_false.place_forget()

img_sms_true = PhotoImage(file='sms_true.png')
label_sms_true = Label(image=img_sms_true, bg='#E5E5E4')
label_sms_true.img = img_sms_true
label_sms_true.place(x=279, y=400)
label_sms_true.place_forget()

img_sms_turn = PhotoImage(file='sms_turn.png')
label_sms_turn = Label(image=img_sms_turn, bg='#E5E5E4')
label_sms_turn.img = img_sms_turn
label_sms_turn.place(x=279, y=400)
label_sms_turn.place_forget()

def menu():
    """Creating the main menu"""
    label_no_cash.place_forget()
    label_sms_disable.place_forget()
    label_sms_false.place_forget()
    label_sms_true.place_forget()
    label_sms_turn.place_forget()
    label_inf.place_forget()
    label_back_services.place_forget()
    label_number_attempts.place_forget()
    label_back_exit.place_forget()
    label_back_forth.place_forget()
    label_2.place_forget()

    label_2.configure(justify=CENTER, anchor=N)

    sum_money.place_forget()
    label_menu.place(x=279, y=100)

    side_button_1['command'] = deposit_cash
    side_button_2['command'] = check_balance
    side_button_3['command'] = information_about_card
    side_button_4['command'] = close_window
    side_button_5['command'] = cash_withdrawal
    side_button_6['command'] = change_pass_pin
    side_button_7['command'] = sms_information
    side_button_8['command'] = money_transfers


def deposit_cash():
    """Depositing an amount into an ATM"""
    side_button_1['command'] = ''
    side_button_2['command'] = ''
    side_button_3['command'] = ''
    side_button_4['command'] = menu
    side_button_5['command'] = ''
    side_button_6['command'] = ''
    side_button_7['command'] = ''
    side_button_8['command'] = check_sum
    label_back_forth.place(x=279, y=300)
    label_menu.place_forget()
    label_2.configure(text='Введите сумму внесения:', bg='#E5E5E4', height=1, width=40)
    label_2.place(x=258, y=150)
    sum_money.place(x=392, y=210, width=410, height=50)

    #working with buttons on the keyboard
    def get_num(num):
        if sum_money.get().find('.') == -1:
            sum_money.insert(len(sum_money.get()), str(num))
        elif num == 0 and len(sum_money.get()) - sum_money.get().find('.') <= 2:
            sum_money.insert(len(sum_money.get()), '0')

    def get_num_00():
        if sum_money.get().find('.') == -1 or len(sum_money.get()) - sum_money.get().find('.') == 1:
            sum_money.insert(len(sum_money.get()), '00')

    def pin_clear():
        sum_money.delete(0, len(sum_money.get()))

    def pin_cancel():
        sum_money.delete(len(sum_money.get()) - 1)

    def plus_num_point():
        if sum_money.get().find('.') == -1 and len(sum_money.get()) != 0:
            sum_money.insert(len(sum_money.get()), '.00')

    num_0['command'] = lambda: get_num(0)
    num_1['command'] = lambda: get_num(1)
    num_2['command'] = lambda: get_num(2)
    num_3['command'] = lambda: get_num(3)
    num_4['command'] = lambda: get_num(4)
    num_5['command'] = lambda: get_num(5)
    num_6['command'] = lambda: get_num(6)
    num_7['command'] = lambda: get_num(7)
    num_8['command'] = lambda: get_num(8)
    num_9['command'] = lambda: get_num(9)
    num_00['command'] = get_num_00
    clear['command'] = pin_clear
    cancel['command'] = pin_cancel
    enter['command'] = insert_clarification_check
    num_point['command'] = plus_num_point

def check_sum():
    """Cheking sum of money"""
    if sum_money.get() != '' and float(sum_money.get()) > 0:
        insert_clarification_check()
    else:
        deposit_cash()

def insert_clarification_check():
    """Clarification of checks when making"""
    global balance
    side_button_4['command'] = insert_cash
    num_0['command'] = ''
    num_1['command'] = ''
    num_2['command'] = ''
    num_3['command'] = ''
    num_4['command'] = ''
    num_5['command'] = ''
    num_6['command'] = ''
    num_7['command'] = ''
    num_8['command'] = ''
    num_9['command'] = ''
    num_00['command'] = ''
    clear['command'] = ''
    cancel['command'] = ''
    enter['command'] = ''
    num_point['command'] = ''
    side_button_8['command'] = insert_cash_with_check
    label_2.place_forget()
    balance += float(str(sum_money.get()))
    sum_money.delete(0, len(sum_money.get()))
    sum_money.place_forget()
    label_back_forth.place_forget()
    label_information_check.place(x=279, y=300)

def check_balance():
    """Show balance"""
    global balance
    side_button_1['command'] = ''
    side_button_2['command'] = ''
    side_button_3['command'] = ''
    side_button_4['command'] = menu
    side_button_5['command'] = ''
    side_button_6['command'] = ''
    side_button_7['command'] = ''
    side_button_8['command'] = close_window
    label_menu.place_forget()
    label_2.place_forget()
    label_back_exit.place(x=279, y=300)
    label_2.configure(text='Баланс: ' + '%.2f' % (balance) + ' руб.', bg='#E5E5E4', height=1, width=40)
    label_2.place(x=258, y=170)

def information_about_card():
    """Show information about card"""
    side_button_1['command'] = ''
    side_button_2['command'] = ''
    side_button_3['command'] = ''
    side_button_4['command'] = menu
    side_button_5['command'] = ''
    side_button_6['command'] = ''
    side_button_7['command'] = ''
    side_button_8['command'] = close_window

    label_menu.place_forget()
    label_2.place_forget()
    label_back_exit.place(x=279, y=300)
    label_2.configure(text='Владелец карты:\n\nСрок действия карты:', bg='#E5E5E4', height=3, width=30, justify=LEFT,
                      anchor=W)
    label_2.place(x=270, y=150)
    label_inf.place(x=570, y=150)

def change_pass_pin():
    """Change user pin code"""
    global num_1, num_2, num_3, num_4, num_5, num_6, num_7, num_8, num_9, num_00, num_0, num_point, clear, cancel, \
        enter, password
    label_menu.place_forget()
    label_2.configure(text='Введите старый ПИН-код', bg='#E5E5E4', height=1, width=40)
    label_2.place(x=258, y=150)
    pass_pin = Entry(root, bd=0, bg='#EFEFEF', show='*', font=('Arial', 50))
    pass_pin.place(x=545, y=210, width=110, height=60)

    side_button_1['command'] = ''
    side_button_2['command'] = ''
    side_button_3['command'] = ''
    side_button_4['command'] = ''
    side_button_5['command'] = ''
    side_button_6['command'] = ''
    side_button_7['command'] = ''
    side_button_8['command'] = ''

    #working with buttons on the keyboard
    def get_num(num):
        if len(pass_pin.get()) < 4:
            pass_pin.insert(len(pass_pin.get()), str(num))

    def get_num_00():
        if len(pass_pin.get()) < 3:
            pass_pin.insert(len(pass_pin.get()), '00')
        if len(pass_pin.get()) == 3:
            pass_pin.insert(4, '0')

    def pin_clear():
        if len(pass_pin.get()) > 0:
            pass_pin.delete(0, len(pass_pin.get()))

    def pin_cancel():
        if len(pass_pin.get()) > 0:
            pass_pin.delete(len(pass_pin.get()) - 1)

    def pin_enter():
        if pass_pin.get() == password:
            new_pin()

        else:
            check_pass_pin()


    def new_pin():
        """Create new pin"""
        enter['command'] = information_new_pin
        label_2.place_forget()
        label_2.configure(text='Введите новый ПИН-код', bg='#E5E5E4', height=1, width=40)
        label_2.place(x=258, y=150)
        pass_pin.delete(0, 4)
        label_number_attempts.place_forget()

    def information_new_pin():
        """Check new pin"""
        global password
        if len(pass_pin.get()) != 4:
            new_pin()
            return
        password = pass_pin.get()
        pass_pin.destroy()
        label_2.place_forget()
        label_2.configure(text='ПИН-код успешно сменен!', bg='#E5E5E4', height=1, width=40)
        label_2.place(x=258, y=170)
        label_back_services.place(x=279, y=300)
        side_button_1['command'] = ''
        side_button_2['command'] = ''
        side_button_3['command'] = ''
        side_button_4['command'] = menu
        side_button_5['command'] = ''
        side_button_6['command'] = ''
        side_button_7['command'] = ''
        side_button_8['command'] = close_window

        num_0['command'] = ''
        num_1['command'] = ''
        num_2['command'] = ''
        num_3['command'] = ''
        num_4['command'] = ''
        num_5['command'] = ''
        num_6['command'] = ''
        num_7['command'] = ''
        num_8['command'] = ''
        num_9['command'] = ''
        num_00['command'] = ''
        clear['command'] = ''
        cancel['command'] = ''
        enter['command'] = ''

        pass_pin.destroy()

    def check_pass_pin():
        """Check pin"""
        global number_check
        number_check -= 1
        label_number_attempts['text'] = 'Количество оставшихся попыток: ' + str(number_check)
        label_number_attempts.place(x=258, y=300)

        if number_check != 0:
            pass_pin.delete(0, 4)
            label_2.place_forget()
            label_2['text'] = 'Введён неверный ПИН-код!\nВведите ещё раз:'
            label_2['height'] = 3
            label_2.place(x=258, y=110)
            return

        else:
            label_2.place_forget()
            pass_pin.destroy()
            label_2['text'] = 'Количество попыток закончилось!\nКарта заблокирована!\nДля работы банкомата ' \
                              'перезапустите программу.'
            label_2['height'] = 5
            label_2.place(x=258, y=120)
            num_0['command'] = ''
            num_1['command'] = ''
            num_2['command'] = ''
            num_3['command'] = ''
            num_4['command'] = ''
            num_5['command'] = ''
            num_6['command'] = ''
            num_7['command'] = ''
            num_8['command'] = ''
            num_9['command'] = ''
            num_00['command'] = ''
            clear['command'] = ''
            cancel['command'] = ''
            enter['command'] = ''

    num_0['command'] = lambda: get_num(0)
    num_1['command'] = lambda: get_num(1)
    num_2['command'] = lambda: get_num(2)
    num_3['command'] = lambda: get_num(3)
    num_4['command'] = lambda: get_num(4)
    num_5['command'] = lambda: get_num(5)
    num_6['command'] = lambda: get_num(6)
    num_7['command'] = lambda: get_num(7)
    num_8['command'] = lambda: get_num(8)
    num_9['command'] = lambda: get_num(9)
    num_00['command'] = get_num_00
    clear['command'] = pin_clear
    cancel['command'] = pin_cancel
    enter['command'] = pin_enter


def sms_information():
    """Show information about SMS notifications"""
    global sms
    label_menu.place_forget()
    label_sms_disable.place_forget()
    label_sms_false.place_forget()
    label_sms_true.place_forget()
    label_sms_turn.place_forget()

    side_button_1['command'] = ''
    side_button_2['command'] = ''
    side_button_3['command'] = ''
    side_button_4['command'] = menu
    side_button_5['command'] = ''
    side_button_6['command'] = ''
    side_button_7['command'] = ''
    side_button_8['command'] = change_sms_information

    if sms:
        label_sms_true.place(x=279, y=165)
        label_sms_disable.place(x=279, y=300)
    else:
        label_sms_false.place(x=279, y=165)
        label_sms_turn.place(x=279, y=300)

def change_sms_information():
    """Change information about SMS notifications"""
    global sms
    if sms:
        sms = False
    else:
        sms = True

    sms_information()

def cash_withdrawal():
    """Cash withdrawal from ATM"""
    side_button_1['command'] = ''
    side_button_2['command'] = ''
    side_button_3['command'] = ''
    side_button_4['command'] = menu
    side_button_5['command'] = ''
    side_button_6['command'] = ''
    side_button_7['command'] = ''
    side_button_8['command'] = check_cash_withdrawal
    label_back_forth.place(x=279, y=300)
    label_menu.place_forget()
    label_2.configure(text='Введите сумму для снятия:', bg='#E5E5E4', height=1, width=40)
    label_2.place(x=258, y=150)
    sum_money.place(x=392, y=210, width=410, height=50)

    # working with buttons on the keyboard
    def get_num(num):
        if sum_money.get().find('.') == -1:
            sum_money.insert(len(sum_money.get()), str(num))
        elif num == 0 and len(sum_money.get()) - sum_money.get().find('.') <= 2:
            sum_money.insert(len(sum_money.get()), '0')

    def get_num_00():
        if sum_money.get().find('.') == -1 or len(sum_money.get()) - sum_money.get().find('.') == 1:
            sum_money.insert(len(sum_money.get()), '00')

    def pin_clear():
        sum_money.delete(0, len(sum_money.get()))

    def pin_cancel():
        sum_money.delete(len(sum_money.get()) - 1)

    def plus_num_point():
        if sum_money.get().find('.') == -1:
            sum_money.insert(len(sum_money.get()), '.00')

    num_0['command'] = lambda: get_num(0)
    num_1['command'] = lambda: get_num(1)
    num_2['command'] = lambda: get_num(2)
    num_3['command'] = lambda: get_num(3)
    num_4['command'] = lambda: get_num(4)
    num_5['command'] = lambda: get_num(5)
    num_6['command'] = lambda: get_num(6)
    num_7['command'] = lambda: get_num(7)
    num_8['command'] = lambda: get_num(8)
    num_9['command'] = lambda: get_num(9)
    num_00['command'] = get_num_00
    clear['command'] = pin_clear
    cancel['command'] = pin_cancel
    enter['command'] = check_cash_withdrawal
    num_point['command'] = plus_num_point

def check_cash_withdrawal():
    """Checking the correct payment of cash"""
    if sum_money.get() != '' and float(sum_money.get()) > 0:
        if (balance - float(sum_money.get())) >= 0:
            cash_withdrawal_with_check()
        else:
            label_no_cash.place(x=258, y=265)
            sum_money.delete(0, len(sum_money.get()))
            cash_withdrawal()
    else:
        cash_withdrawal()

def cash_withdrawal_with_check():
    """Checking the correct payment of cash with check"""
    global balance
    label_no_cash.place_forget()
    side_button_4['command'] = withdrawal_cash_without_check
    num_0['command'] = ''
    num_1['command'] = ''
    num_2['command'] = ''
    num_3['command'] = ''
    num_4['command'] = ''
    num_5['command'] = ''
    num_6['command'] = ''
    num_7['command'] = ''
    num_8['command'] = ''
    num_9['command'] = ''
    num_00['command'] = ''
    clear['command'] = ''
    cancel['command'] = ''
    enter['command'] = ''
    num_point['command'] = ''
    side_button_8['command'] = withdrawal_cash_with_check
    label_2.place_forget()
    balance -= float(str(sum_money.get()))
    sum_money.delete(0, len(sum_money.get()))
    sum_money.place_forget()
    label_back_forth.place_forget()
    label_information_check.place(x=279, y=300)


def money_transfers():
    """Transferring money to another card"""
    side_button_1['command'] = ''
    side_button_2['command'] = ''
    side_button_3['command'] = ''
    side_button_4['command'] = menu
    side_button_5['command'] = ''
    side_button_6['command'] = ''
    side_button_7['command'] = ''
    side_button_8['command'] = check_transfer_card
    label_back_forth.place(x=279, y=300)
    label_menu.place_forget()
    label_2.configure(text='Введите номер карты:', bg='#E5E5E4', height=1, width=40)
    label_2.place(x=258, y=150)
    sum_money.place(x=442, y=210, width=320, height=50)

    # working with buttons on the keyboard
    def get_num(num):
        if len(sum_money.get()) < 19:
            if sum_money.get().rfind(' ') == -1 and len(sum_money.get()) == 4:
                sum_money.insert(len(sum_money.get()), ' ')
            elif sum_money.get().rfind(' ') != -1 and (len(sum_money.get()) == 5 or len(sum_money.get()) == 9
                                                       or len(sum_money.get()) == 14):
                sum_money.insert(len(sum_money.get()), ' ')

            sum_money.insert(len(sum_money.get()), str(num))

    def pin_clear():
        sum_money.delete(0, len(sum_money.get()))

    def pin_cancel():
        sum_money.delete(len(sum_money.get()) - 1)

    num_0['command'] = lambda: get_num(0)
    num_1['command'] = lambda: get_num(1)
    num_2['command'] = lambda: get_num(2)
    num_3['command'] = lambda: get_num(3)
    num_4['command'] = lambda: get_num(4)
    num_5['command'] = lambda: get_num(5)
    num_6['command'] = lambda: get_num(6)
    num_7['command'] = lambda: get_num(7)
    num_8['command'] = lambda: get_num(8)
    num_9['command'] = lambda: get_num(9)
    num_00['command'] = ''
    clear['command'] = pin_clear
    cancel['command'] = pin_cancel
    enter['command'] = check_transfer_card
    num_point['command'] = ''

def check_transfer_card():
    """Card data entry check"""
    if len(sum_money.get()) == 19:
        sum_transfer()
    else:
        money_transfers()

def sum_transfer():
    """Entering the transfer amount"""
    sum_money.delete(0, len(sum_money.get()))
    sum_money.place(x=392, y=210, width=410, height=50)
    side_button_1['command'] = ''
    side_button_2['command'] = ''
    side_button_3['command'] = ''
    side_button_4['command'] = menu
    side_button_5['command'] = ''
    side_button_6['command'] = ''
    side_button_7['command'] = ''
    side_button_8['command'] = check_sum_transfer
    label_back_forth.place(x=279, y=300)
    label_menu.place_forget()
    label_2.configure(text='Введите сумму для перевода:', bg='#E5E5E4', height=1, width=40)
    label_2.place(x=258, y=150)
    sum_money.place(x=392, y=210, width=410, height=50)

    # working with buttons on the keyboard
    def get_num(num):
            sum_money.insert(len(sum_money.get()), num)

    def get_num_00():
        sum_money.insert(len(sum_money.get()), '00')

    def pin_clear():
        sum_money.delete(0, len(sum_money.get()))

    def pin_cancel():
        sum_money.delete(len(sum_money.get()) - 1)

    def plus_num_point():
        if sum_money.get().find('.') == -1 and len(sum_money.get()) != 0:
            sum_money.insert(len(sum_money.get()), '.')

    num_0['command'] = lambda: get_num(0)
    num_1['command'] = lambda: get_num(1)
    num_2['command'] = lambda: get_num(2)
    num_3['command'] = lambda: get_num(3)
    num_4['command'] = lambda: get_num(4)
    num_5['command'] = lambda: get_num(5)
    num_6['command'] = lambda: get_num(6)
    num_7['command'] = lambda: get_num(7)
    num_8['command'] = lambda: get_num(8)
    num_9['command'] = lambda: get_num(9)
    num_00['command'] = get_num_00
    clear['command'] = pin_clear
    cancel['command'] = pin_cancel
    enter['command'] = check_sum_transfer
    num_point['command'] = plus_num_point

def check_sum_transfer():
    """Check the transfer amount"""
    if sum_money.get() != '' and float(sum_money.get()) > 0:
        if (balance - float(sum_money.get())) >= 0:
            transfer()
        else:
            label_no_cash.place(x=258, y=265)
            sum_money.delete(0, len(sum_money.get()))
            sum_transfer()
    else:
        sum_transfer()

def transfer():
    """Transferring money to another card"""
    global balance
    label_no_cash.place_forget()
    side_button_4['command'] = transfer_without_check
    num_0['command'] = ''
    num_1['command'] = ''
    num_2['command'] = ''
    num_3['command'] = ''
    num_4['command'] = ''
    num_5['command'] = ''
    num_6['command'] = ''
    num_7['command'] = ''
    num_8['command'] = ''
    num_9['command'] = ''
    num_00['command'] = ''
    clear['command'] = ''
    cancel['command'] = ''
    enter['command'] = ''
    num_point['command'] = ''
    side_button_8['command'] = transfer_with_check
    label_2.place_forget()
    balance -= float(str(sum_money.get()))
    sum_money.delete(0, len(sum_money.get()))
    sum_money.place_forget()
    label_back_forth.place_forget()
    label_information_check.place(x=279, y=300)

def transfer_with_check():
    """Transferring money to another card with check"""
    label_information_check.place_forget()
    label_2.place_forget()
    label_2.configure(text='Перевод успешно выполнен!\nПолучите чек!', bg='#E5E5E4', height=1, width=40)
    label_2.place(x=258, y=170)
    side_button_1['command'] = ''
    side_button_2['command'] = ''
    side_button_3['command'] = ''
    side_button_4['command'] = ''
    side_button_5['command'] = ''
    side_button_6['command'] = ''
    side_button_7['command'] = ''
    side_button_8['command'] = ''
    print_check()

def transfer_without_check():
    """Transferring money to another card without check"""
    label_information_check.place_forget()
    label_2.place_forget()
    label_2['text'] = 'Перевод успешно выполнен!'
    label_2.place(x=258, y=170)
    side_button_1['command'] = ''
    side_button_2['command'] = ''
    side_button_3['command'] = ''
    side_button_4['command'] = menu
    side_button_5['command'] = ''
    side_button_6['command'] = ''
    side_button_7['command'] = ''
    side_button_8['command'] = close_window
    label_back_exit.place(x=279, y=300)


#Establishing a major labels

label_2 = Label(root, text='Добро пожаловать!\nВставьте карту или прислоните её!\n(для этого нажмите на нужные кнопки)',
            bg='#E5E5E4', fg='#2C2A30', font=('Arvo', 20, 'bold'), height=9, width=39)
label_2.place(x=266, y=60)

label_3 = Label(root, text="MASHA'S BANK", bg='#E5E5E4', fg='#2C2A30', font=('Sylfaen', 20), width=13,
            height=0)
label_3.place(x=500, y=46)

label_inf = Label(root, text=full_name + '\n\n' + expiration_date, bg='#E5E5E4', fg='#2C2A30',
                  font=('Arvo', 20, 'bold'), height=3, width=21, justify=RIGHT, anchor=E)
label_inf.place(x=570, y=150)
label_inf.place_forget()


#placement of buttons with numbers

img_num_1 = PhotoImage(file='num_1.png')
num_1 = Button(root, image=img_num_1, highlightthickness=0, bd=0, width=40, height=36)
num_1.place(x=430, y=559)

img_num_2 = PhotoImage(file='num_2.png')
num_2 = Button(root, image=img_num_2, highlightthickness=0, bd=0, width=40, height=36)
num_2.place(x=494, y=559)

img_num_3 = PhotoImage(file='num_3.png')
num_3 = Button(root, image=img_num_3, highlightthickness=0, bd=0, width=40, height=36)
num_3.place(x=558, y=559)

img_num_4 = PhotoImage(file='num_4.png')
num_4 = Button(root, image=img_num_4, highlightthickness=0, bd=0, width=40, height=36)
num_4.place(x=430, y=614)

img_num_5 = PhotoImage(file='num_5.png')
num_5 = Button(root, image=img_num_5, highlightthickness=0, bd=0, width=40, height=36)
num_5.place(x=494, y=614)

img_num_6 = PhotoImage(file='num_6.png')
num_6 = Button(root, image=img_num_6, highlightthickness=0, bd=0, width=40, height=36)
num_6.place(x=558, y=614)

img_num_7 = PhotoImage(file='num_7.png')
num_7 = Button(root, image=img_num_7, highlightthickness=0, bd=0, width=40, height=36)
num_7.place(x=430, y=669)

img_num_8 = PhotoImage(file='num_8.png')
num_8 = Button(root, image=img_num_8, highlightthickness=0, bd=0, width=40, height=36)
num_8.place(x=494, y=669)

img_num_9 = PhotoImage(file='num_9.png')
num_9 = Button(root, image=img_num_9, highlightthickness=0, bd=0, width=40, height=36)
num_9.place(x=558, y=670)

img_num_point = PhotoImage(file='num_point.png')
num_point = Button(root, image=img_num_point, highlightthickness=0, bd=0, width=40, height=36)
num_point.place(x=430, y=729)

img_num_0 = PhotoImage(file='num_0.png')
num_0 = Button(root, image=img_num_0, highlightthickness=0, bd=0, width=40, height=36)
num_0.place(x=494, y=729)

img_num_00 = PhotoImage(file='num_00.png')
num_00 = Button(root, image=img_num_00, highlightthickness=0, bd=0, width=42, height=36)
num_00.place(x=557, y=729)

img_cancel = PhotoImage(file='cancel.png')
cancel = Button(root, image=img_cancel, highlightthickness=0, bd=0, width=71, height=36)
cancel.place(x=629, y=559)

img_clear = PhotoImage(file='clear.png')
clear = Button(root, image=img_clear, highlightthickness=0, bd=0, width=71, height=36)
clear.place(x=628, y=615)

img_enter = PhotoImage(file='enter.png')
enter = Button(root, image=img_enter, highlightthickness=0, bd=0, width=71, height=36)
enter.place(x=628, y=671)

img_blank_button = PhotoImage(file='blank_button.png')
blank_button = Button(root, image=img_blank_button, highlightthickness=0, bd=0, width=65, height=36)
blank_button.place(x=628, y=729)


#creating buttons near the screen
img_side_button_1 = PhotoImage(file='side_button.png')
side_button_1 = Button(root, image=img_side_button_1, highlightthickness=0, bd=0, width=65, height=40)
side_button_1.place(x=148, y=68)

img_side_button_2 = PhotoImage(file='side_button.png')
side_button_2 = Button(root, image=img_side_button_2, highlightthickness=0, bd=0, width=65, height=40)
side_button_2.place(x=148, y=148)

img_side_button_3 = PhotoImage(file='side_button.png')
side_button_3 = Button(root, image=img_side_button_3, highlightthickness=0, bd=0, width=65, height=40)
side_button_3.place(x=148, y=228)

img_side_button_4 = PhotoImage(file='side_button.png')
side_button_4 = Button(root, image=img_side_button_4, highlightthickness=0, bd=0, width=65, height=40)
side_button_4.place(x=148, y=308)

img_side_button_5 = PhotoImage(file='side_button.png')
side_button_5 = Button(root, image=img_side_button_5, highlightthickness=0, bd=0, width=65, height=40)
side_button_5.place(x=988, y=68)

img_side_button_6 = PhotoImage(file='side_button.png')
side_button_6 = Button(root, image=img_side_button_6, highlightthickness=0, bd=0, width=65, height=40)
side_button_6.place(x=988, y=148)

img_side_button_7 = PhotoImage(file='side_button.png')
side_button_7 = Button(root, image=img_side_button_7, highlightthickness=0, bd=0, width=65, height=40)
side_button_7.place(x=988, y=228)

img_side_button_8 = PhotoImage(file='side_button.png')
side_button_8 = Button(root, image=img_side_button_8, highlightthickness=0, bd=0, width=65, height=40)
side_button_8.place(x=988, y=308)

#card insertion button
img_button_insert_card = PhotoImage(file='button_insert_card.png')
button_insert_card = Button(root, image=img_button_insert_card, highlightthickness=0, bd=0, width=283, height=20,
                        command=insert_card)
button_insert_card.place(x=690, y=390)

#button for applying a card
img_contactless_payment = PhotoImage(file='contactless_payment.png')
contactless_payment = Button(root, image=img_contactless_payment, highlightthickness=0, bd=0, width=182, height=198,
                         command=attaching_card)
contactless_payment.place(x=960, y=562)


root.mainloop()