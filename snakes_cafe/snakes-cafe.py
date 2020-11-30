
menu = ['Wings','Cookies', 'Spring Rolls', 'Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden', 'Ice Cream', 'Cake', 'Pie', 'Coffee', 'Tea', 'Unicorn Tears']

print('*******************************')
print('**    Welcome to the Snakes Cafe!   **')
print('**    Please see our menu below.    **')
print('**')
print('**')
print('** To quit at any time, type "quit" **')
print('*******************************')

print()



print(
    "--------Appetizers-------\n Wings \n Cookies \n Spring Rolls\n---------",
    "Entrees------\n Salmon \n Steak \n Meat Tornado \n A Literal Garden\n--------",
    "Desserts----\n Ice Cream \n Cake \n Pie\n----------",
    "Drinks------\n Coffee \n Tea \n Unicorn Tears \n"
    ),


print('****************************') 
print('** What would you like to order? **') 
print('*****************************') 

orders={}


while True:
    x = input('>')
    if (x=='quit'):
        break

    else:
        if (x in menu):
            if x in orders:
                orders[x]=orders[x]+1
            else:
                orders[x]=1
            print(f'**  {orders[x]} orders of{x} have been added to your meal **')
        else:
             print('sorry we do not have this item')
       