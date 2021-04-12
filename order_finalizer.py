import pandas as pd
import random
import json
import ast
import itertools

def preprocess(str):
    str= str.replace('[','').replace(']','').replace("'",'')
    str = str.split(',')
    return str

data = pd.read_csv("single/dummyRestaurantData_2021.csv")

rest_id = int(input("Enter Restaurant ID you want to order from: "))
Restaurant_name,Restaurant_id,Expected_Time,promoted,category,location,Ratings,cost_for_two,offers,Veg_menu,Non_vegmenu,Healthy_Food = data.iloc[rest_id-1,:]


menu = {}


Veg_menu = Veg_menu.strip('][').split(', ')
Non_vegmenu = Non_vegmenu.strip('][').split(', ')
Healthy_Food = Healthy_Food.strip('][').split(', ')

for i , item in enumerate(Veg_menu):
    menu.update({i+1:item})
for k,item in enumerate(Non_vegmenu):
    menu.update({k+i+2:item})
for j , item in enumerate(Healthy_Food):
    menu.update({i+j+k+3:item})
print(menu)
for x,item in enumerate(menu):
        print(x+1," ", [key for key,value in (ast.literal_eval(menu[item])).items() ],"       Rs.",[value for key,value in (ast.literal_eval(menu[item])).items() ]) 
        #print(i+1," ", (ast.literal_eval(menu[item])).keys() ,"      ",type(ast.literal_eval(menu[item]))) 
    
order = input("Enter your food item id seperated with comma to proceed with the order:  ")
order = order.split(',')
order = [int(item) for item in order]
print(order)
ordered_item = [menu[item] for item in order]
print(ordered_item,type(ordered_item))
length = len(ordered_item)
ordered_item_price = []
for i in range(length):
    ordered_item_price.append([value for key,value in (ast.literal_eval(ordered_item[i])).items()])
#ordered_item_price = [value for key,value in (ast.literal_eval(ordered_item[i])).items()]
print(ordered_item_price)
print("\n\n\t\tBill: #",random.randint(1,100),"\n\n")
print('Restaurant Name:\t',Restaurant_name)
print('Restaurant Address:\t',location)
print('Expected Time:\t',Expected_Time)
print('Category:\t', category)
print('Ratings:\t', Ratings)
print('Cost for 2:\t', cost_for_two)
print('offer:\t',offers)

print('\nItems:\t',length)

print(length)
for i in range(length):
    print([key for key,value in (ast.literal_eval(ordered_item[i])).items()],":  \tRs. ",[value for key,value in (ast.literal_eval(ordered_item[i])).items()])
merged = list(itertools.chain(*ordered_item_price))


print("\nTotal Bill Amount= ",sum(merged))

