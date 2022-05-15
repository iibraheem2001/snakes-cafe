intro = '''
$ python snakes_cafe.py
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
'''
print(intro)
appetizers = '''
Appetizers
----------
Wings
Cookies
Spring Rolls
'''
print(appetizers)
entrees = '''
Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden
'''
print(entrees)
desserts = '''
Desserts
--------
Ice Cream
Cake
Pie
'''
print(desserts)
drinks = '''
Drinks
------
Coffee
Tea
Unicorn Tears
'''
print(drinks)
what_order = '''
***********************************
** What would you like to order? **
***********************************
'''
print(what_order)

my_order = []
while True:
    order = input('> ')
    my_order.append(order)
    count = my_order.count(order)
    if order == ('quit'):
        break
    if order in appetizers or order in entrees or order in desserts or order in drinks:
        print(f'** {count} Order of {order} have been added to your meal **')


