# write your code here
def check(v1, v2, v3):
    msg = ''
    msg_6 = " ... lazy"
    msg_7 = " ... very lazy"
    msg_8 = " ... very, very lazy"
    msg_9 = "You are"
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg = msg + msg_8
    if msg != '':
        msg = msg_9 + msg
        print(msg)
    
    
def is_one_digit(v):
    output = False
    if v > -10 and v < 10 and v.is_integer():
        output = True
    return output

memory = 0
DO_NOT_STOP = True
msg_4 = 'Do you want to store the result? (y / n):'
while DO_NOT_STOP:
    print('Enter an equation')
    calc = input()
    x, oper, y = calc.split()
    #checks if user has informed 'M'
    if x == 'M':
        x = memory
        if y == 'M':
            y = memory
    elif y == 'M':
        y = memory
    #checks if x and y are numbers
    try:
        x = float(x)
        y = float(y)
    except Exception:
        print('Do you even know what numbers are? Stay focused!')
        continue
    result = ''
    #checks operator and calculates operation
    if oper == '+' or oper == '-' or oper == '*' or oper == '/':
        # insulta o usuario (lazy, very lazy, very, very lazy...)
        check(x, y, oper)
        if oper == '+':
            result = x + y
        elif oper == '-':
            result = x - y
        elif oper == '*':
            result = x * y
        elif oper == '/' and y != 0:
            result = x / y
        else:
            print('Yeah... division by zero. Smart move...') 
            continue
        # prints operation result
        print(result)
        # places result in memory
        answer = ''
        while answer != 'y' and answer != 'n':
            print(msg_4)
            answer = input()
        if answer == 'y':
            #novo fluxo para checar se vai armazenar apenas um digito
            msg_10 = "Are you sure? It is only one digit! (y / n)"
            msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
            msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
            msg_ = {10: msg_10, 11: msg_11, 12: msg_12}
            if is_one_digit(result):
                answer1 = ''
                msg_index = 10
                while True:
                    print(msg_[msg_index])
                    answer1 = input()
                    if answer1 == 'y':
                        if msg_index < 12:
                            msg_index += 1
                        else:
                            memory = result
                            break
                    elif answer1 == 'n':
                        break
            else:
                memory = result
        answer = ''
        while answer != 'y' and answer != 'n':
            print('Do you want to continue calculations? (y / n):')
            answer = input()
        if answer == 'n':
            DO_NOT_STOP = False
    else:
        print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
