# **kwargs - parameter that will pack all argumetns into a dictionary
           # useful for function accepting varying amount of keyword arguments

def hello(**kwargs):
    print('Hello, my name is '+kwargs['first']+ " " +kwargs['last'])

# Must have keyword arguments when passing into **kwargs parameter function
hello(first='Nino', last='Pino')

def introduction(**info):
    print('Hello, allow me to introduce myself. My full name is ', end="")
    for key,value in info.items():
        print(value,end=' ')

first_name = 'Percival'
nickname = 'Percy'
second_name = 'Fredrickstein'
third_name = 'von Musel'
fourth_name = 'Klossowski'
last_name = 'de Rolo'
title = 'the Third'

hello(first=nickname, last=last_name)
introduction(first=first_name, second=second_name, third=third_name, fourth=fourth_name, last=last_name, title=title)