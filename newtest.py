import math
from time import sleep as sp 
print('Hi, I\'m here to help')

def mathematics():
    recieved = (input("\nWhat would you like me to solve?\nArea of a circle\n(r(cos£)^2 + r(sin$)^2)^1/2- B\nGradient\nfactorial\nConvert temperatures between fahrenheit and celsius degrees\n"))

    def area():
        radius = float(input("what is the radius of the circle\n"))
        result = math.pi * radius**2
        print(f'The area of the circle is {result}')

    def complexroot():
        a = float(input("What is the cosine angle\n"))
        b = float(input("What is the sine angle\n"))
        r = float(input("What is the constant term\n"))
        result = (r * (math.cos(a * (math.pi/180))**2 + math.sin(b * (math.pi/180))**2))**(1/2)
        print(f'The answer is {result}')

    def gradient():
        y1 = float(input("y1\n"))
        y2 = float(input("y2\n"))
        x1 = float(input("x1\n"))
        x2 = float(input("x2\n"))
        result = (y2 - y1) / (x2 - x1)
        print(f'The gredient, M = {result}')

    def factorial():
        n = int(input('Type a positive number. I\'ll give the factorial\n'))
        nfactorial = n

        for i in range(1, n):
            nfactorial *= (n - i)
        print(f"\nThe factorial of {n} is {nfactorial}")

    def celsius():
        fah = float(input('I currently do not have the ability to read temperatures myself. please What is the fahrenheit temperatur\n'))
        cel = 5/9 * (fah - 32)
        print('\n')
        print('Very well.\nThe temperature in degree celsius is', cel)

    def fah():
        cels = float(input("I'm currently under development and do not have the ability to read temperatures myself.\nPlease what is the temperature celsius\n"))
        fah = 9/5 * cels + 32
        print(f'\nThe temperature is {fah} fahrenheits')




    #control structure for user inputs
    recieved = recieved.split(' ')
    for i in recieved:
        if  (('area' and 'of' and 'a' and 'circle') in recieved) or 'Area' in recieved or 'Circle' in recieved or 'area' in recieved or 'circle' in recieved:
            sp(1)
            print('right there, I got you\n') 
            sp(1)
            area()
            break
        elif 'b' in recieved or 'B' in recieved or (('option' and 'b') in recieved)  or (('option' and 'B') in recieved):
            sp(.7)
            print('Here were go, I hope you understand')
            sp(1)
            complexroot()
            break
        elif 'gradient' in recieved or 'Gradient' in recieved:
            sp(.5)
            print('Sure!\ngive me details about the graph')
            sp(1)
            gradient()
            break
        elif 'D' in recieved or 'd' in recieved or 'factorial' in recieved and len(recieved) == 1:
            sp(1)
            factorial()
            break
        elif 'factorial' in recieved and len(recieved) != 1:
            print('Sure. I\'m happy to help you find the factorial of a number\n')
            factorial()
            break
        #The temperature input has proven that this code is not sufficient and Lol let me just leave here for now
        elif 'Temperature' in recieved or 'temperature' in recieved or 'convert' in recieved or 'Convert' in recieved or 'fahrenheit' in recieved or 'Fahrenheit' in recieved or 'celsius' in recieved or 'Celsius' in recieved:
            print('Okay')
            tempinput = input('What temperature convertion do you want to do\n').lower().split(' ')
            for i in tempinput:
                if (len(tempinput) == 3 and tempinput == ['fahrenheit', 'to' 'celsius']) or tempinput == ['i', 'want', 'fahrenheit' ] or ('fahrenheit' in tempinput and 'celsius' not in tempinput):
                    sp(.5)
                    print('Right\n')
                    celsius()
                    break
                elif (len(tempinput) == 3 and tempinput == ['celsius', 'to' 'fahrenheit']) or tempinput == ['i', 'want', 'celsius' ] or ('fahrenheit' in tempinput and 'celsius' not in tempinput):
                    sp(.5)
                    print('On it...')
                    fah()
                    break
                else:
                    print('Sorry. I do not understand that')
                    break
            break    
        else:
            sp(1.5)
            print("Sorry. I don't quite understand that")
            break

mathematics()

#loop for user's subsequent choice
print()
feedback = 'Yes'
while feedback == 'Yes':
    feedback = input('\nDo you want me to do something else for you?\n').split(' ')
    for i in feedback:
        if 'Yes' in feedback or 'yes' in feedback or 'yea' in feedback or 'yeah' in feedback or (('yes' and 'please') in feedback) or (('Yes' and 'please') in feedback):
            mathematics()
            feedback = 'Yes'
            break
        elif 'No' in feedback or 'no' in feedback or 'nah' in feedback or 'thanks' in feedback or 'Thanks' in feedback: 
            print('\nSure\nGoodbye!\nLet me know if you need any other operation')
            break
        elif (('your' and 'name') in feedback) or (('Your' and 'Name') in feedback):
            print("hmmm, my name is looni.\nI'm here to help you with your maths problems...")
            feedback = 'Yes'
            break
        else:
            sp(1.5)
            print('Ummm, I guess I can\'t help you with that at the moment...')
            feedback = 'Yes'

print()
input("Press enter to exit")
