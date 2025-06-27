def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please give a valid number.")

def get_operation(promp):
    while True:
        try:
            op = input(promp)
            if op not in ['+','-','*','/']:
                raise ValueError
            return op
        except ValueError:
            print('Invalide operation')



def calculate(num1,num2,opt):

    if opt == '+':
        return num1+num2
    elif opt =='-':
        return num1 - num2
    elif opt =='*':
        return num1*num2
    elif opt =='/':
        if num2 == 0 :
            return  None
        else:
            return num1/num2
while True:
    num1 = get_number("enter 1st number:")
    num2 = get_number("enter 2nd number:")
    opt = get_operation("enter your operation sign:")

    result = calculate(num1,num2,opt)
    if result is None:
     print("error")
    else:
     print(f'result is {num1}{opt}{num2}={result}')
    again = input("any more calculation?") 
    if again!= 'yes':
        print("finished!")
        break
