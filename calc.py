# Method on the top
def seperator():
    print(30 * '-')

def menu():
    print('\n') #\n is like pressing enter
    seperator()
    print(" Welcome to PyCalc")
    seperator()
    print('[1] - Add')
    print('[2] - Subtract')
    print('[3] - Multiply')
    print('[4] - Divide')
    print('[x] - Exit')

# instructions on the bottom

opc = ''
while(opc != 'x'):
    menu() # Display Menu
    # Select an option
    opc = input('Select an option: ')
    if(opc == 'x'):
        break # Finish with the loop

    num1 = float(input('First Number: '))
    num2 = float(input('Second Number: '))

    if(opc == '1'):
        res = num1 + num2
        print('Result: ' + str(res))
    if(opc == '2'):
        res = num1 - num2
        print('Result: ' + str(res))
    if(opc == '3'):
        res = num1 * num2
        print('Result: ' + str(res))
    elif(opc == '4'):
        if(num1 == 0) or (num2 == 0): # After the if is the condition of the loop
            print("Can not put zero when dividing")
            # elif also requires a condition COMMENTS EFFECT IF LOOPS
        else: #Else do not have a condition
            res = num1 / num2
            print('Result: ' + str(res))
    
    input('Press Enter to continue...')

print('Thank you!!')