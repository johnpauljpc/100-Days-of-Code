#this code depicts how break, continue, and exit() functions
while(True):
    print('You are in the corridor Enter left or right option')
    opt = input('>>')
    if opt == 'left':
        print('You lost')
        break

    elif opt == 'right':
        continue

    else:
        print("You are a genius, You won")
        exit()
