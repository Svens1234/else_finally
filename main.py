#number = input('Enter some number')

#try:
    #print(int(number) / 2)
#except:
    #print('You have to enter a number')


#number = input('Enter some number ')

#try:
    #print(int(number) / 2)
#except:
    #print('You have to enter a number')
#else:
    #print('Else block')
#finally:
    #print('Finally block')

#print('Code after error handling')




#number = input('Enter some number ')

#try:
    #print(int(number) / 2)
#except:
    #print('You have to enter a number')
#else:
    #print('Else block')
#finally:
    #print('Finally block')

#print('Code after error handling')


#while True:
    #try:
        #number = int(input('Enter some number '))
        #print(int(number) / 2)
    #except:
        #print('You have to enter a number')
    #else:
        #print('Good job! This is a number')
        #break
    #finally:
        #print('Finally block')

#print('Code after error handling')


#def divide(x,y):
    #try:
        #return x/y
    #except ZeroDivisionError:
        #print('You can\'t divide by zero')
    #except TypeError:
        #print('x and y must be numbers')
    #else:
        #print(' x has divided by y')
    #finally:
        #print('finally block')


#print(divide(4, 2))
#print(divide(4, 'w'))
#print(divide(4, 0))


def divide(x,y):
    try:
        return x/y
    except ZeroDivisionError as e:
        print('You can\'t divide by zero')
        print(e)
    except TypeError as e:
        print('x and y must be numbers')
        print(e)
    else:
        print(' x was divided by y')
    finally:
        print('finally block')


#print(divide(4, 2))
#print(divide(4, 'w'))
print(divide(4, 0))