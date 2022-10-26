from operator import indexOf


username = input('Please enter your name: \n')
allowedPass = ['passJ', 'passP', 'passC', 'passR']
allowedUser = ['john', 'paul', 'chigozie', 'raphael']
userid = allowedUser.index(username)
print(userid)

if (username in allowedUser):
    passw = input('please %s enter your password: \n' % username)
    if (passw == allowedPass[userid]):
        print('welcome %s ' % username)
        print('these are the available options:')
        print('1. Withdrawal')
        print('2. Cash deposit')
        print('3. Complaint')

        selectOpt = int(input('please enter an input:'))
        if (selectOpt == 1):
            pass
        elif (selectOpt == 2):
            pass
        elif (selectOpt == 3):
            print('###################')
        else:
            print('your input is invalid')

    else:
        print('Incorrect Password')
else:
    print('User does not exist')
