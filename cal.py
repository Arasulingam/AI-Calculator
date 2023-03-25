# * Copyright (C) 2023 Code Bin - All Rights Reserved
#   You may use, distribute and modify this code under the
#   terms of the codebin license
# * For More Details Mail to: arasulingam.7639@gmail.com


# Before Using This code run "pip install word2number" in terminal

import os 
from word2number import w2n
os.system('cls')
print('Enter Value Between Zero to hundred.')
print('''
OPERATORS:
plus,minus,multiply,divide
''')

def arithmetic_calculator():
    while True:
        user_input = input("You: ")
        tokens = user_input.split()
        if user_input.lower() == 'exit':
            break
        
        elif len(tokens)==3: 
            num1 = w2n.word_to_num(tokens[0])
            num2 = w2n.word_to_num(tokens[2])
            operator = tokens[1]
            if operator == 'plus':
               result = num1 + num2
            elif operator == 'minus':
               result = num1 - num2
            elif operator == 'multiply':
               result = num1 * num2
         
            elif operator == 'divide':
                try:
                    result = num1 / num2
                except ZeroDivisionError as e:
                    result="infinity"
                    print(f"Bot: {user_input} is {result}\n")
                    arithmetic_calculator()
            else:
               print("Invalid operator. Please enter one of plus, minus, multiply, divide")
               continue
            print(f"Bot: {user_input} is equal to {result}\n")
        elif len(tokens)==4 :
            if tokens[2]== 'plus' or tokens[2]== 'minus' or tokens[2]== 'multiply' or tokens[2]== 'divide':
                val1 = str(tokens[0]+ ' ' +tokens[1])
                num1=w2n.word_to_num(val1)
                num2=w2n.word_to_num(tokens[3])
                operator=tokens[2]
                if operator == 'plus':
                    result = num1 + num2
                elif operator == 'minus':
                    result = num1 - num2
                elif operator == 'multiply':
                    result = num1 * num2
                elif operator == 'divide':
                    try:
                       result = num1 / num2
                    except ZeroDivisionError as e:
                       result="infinity"
                       print(f"Bot: {user_input} is {result}\n")
                       arithmetic_calculator()
                else:
                     print("Invalid operator. Please enter one of plus, minus, multiply, divide")
                     continue
                print(f"Bot: {user_input} is equal to {result}\n")

            elif tokens[1]=='plus'  or tokens[1]=='minus' or tokens[1]=='multiply' or tokens[1]=='divide':
                val2 = str(tokens[2]+ ' ' +tokens[3])
                
                num1=w2n.word_to_num(tokens[0])
                num2=w2n.word_to_num(val2)
                operator=tokens[1]
                if operator == 'plus':
                    result = num1 + num2
                elif operator == 'minus':
                    result = num1 - num2
                elif operator == 'multiply':
                    result = num1 * num2
                elif operator == 'divide':
                    try:
                        result = num1 / num2
                    except ZeroDivisionError as e:
                        result="infinity"
                        print(f"Bot: {user_input} is {result}\n")
                        arithmetic_calculator()
                else:
                     print("Invalid operator. Please enter one of plus, minus, multiply, divide")
                     continue
                print(f"Bot: {user_input} is equal to {result}\n")
        elif len(tokens)==5 : 
            if tokens[2]== 'plus' or tokens[2]=='minus' or tokens[2]=='multiply' or tokens[2]=='divide':
                val1 = str(tokens[0]+ ' ' +tokens[1])
                val2= str(tokens[3]+ ' ' +tokens[4])
                num1=w2n.word_to_num(val1)
                num2=w2n.word_to_num(val2)
                operator=tokens[2]
                if operator == 'plus':
                    result = num1 + num2
                elif operator == 'minus':
                    result = num1 - num2
                elif operator == 'multiply':
                    result = num1 * num2
                elif operator == 'divide':
                    try:
                       result = num1 / num2
                    except ZeroDivisionError as e:
                       result="infinity"
                       print(f"Bot: {user_input} is {result}\n")
                       arithmetic_calculator()
                else:
                     print("Invalid operator. Please enter one of plus, minus, multiply, divide")
                     continue
                print(f"Bot: {user_input} is equal to {result}\n")

arithmetic_calculator()