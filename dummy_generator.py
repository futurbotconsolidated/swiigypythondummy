import datetime
import calendar
import random
import numpy
import pandas as pd
import uuid

import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        


createFolder('./single/')
createFolder('./half_separate/')
createFolder('./separate/')

restuarants = []

with open('template.txt', 'r') as filehandle:
    restuarants = [current_place.rstrip() for current_place in filehandle.readlines()]



veg_menu = [{"burger":random.randint(55,250)}, {"fries":random.randint(55,250)}, {"vegbiriyani":random.randint(55,250)},{"chole":random.randint(55,250)},{"chapati":random.randint(55,250)},{"dal":random.randint(55,250)},{"special dal makhani":random.randint(55,250)},{"butter Naan":random.randint(55,250)},{"mix Naan":random.randint(55,250)},{"Dosa":random.randint(55,250)},{"paneer uttpam":random.randint(55,250)}]
non_vegmen = [{"drumstick":random.randint(55,250)}, {"chicken Tikka":random.randint(55,250)}, {"chickenBiriyani":random.randint(55,250)},{"chiceknRoll":random.randint(55,250)},{"chicken burger":random.randint(55,250)}, {"mutton Seekh Kabab":random.randint(55,250)}, {"mutton burger":random.randint(55,250)},{"fish burger":random.randint(55,250)},{"deluxe juicycheese burger":random.randint(55,250)}]
Healthy_food_items = [{"veg salad":random.randint(55,250)},{"Chicken Salad":random.randint(55,250)}, {"sugar free coffee":random.randint(55,250)}, {"Diet Free Coke":random.randint(55,250)}, {"apple Juice":random.randint(55,250)}, {"Pineapple juice":random.randint(55,250)}, {"kerelaJuice":random.randint(55,250)},{"healthy breakfast meal":random.randint(55,250)}, {"Custurd":random.randint(55,250)}, {"almondCurd":random.randint(55,250)}]
category = ["FastFood","North Indian","south Indian","Cuisine","Italian","mangolian","chinese","Drinks"]

def generate_random_time(month):
  day = generate_random_day(month)
  if random.random() < 0.5:
    date = datetime.datetime(2021, month, day,00,00)
  else:
    date = datetime.datetime(2021, month, day,00,00)
  time_offset = numpy.random.normal(loc=0.0, scale=180)
  final_date = date + datetime.timedelta(minutes=time_offset)
  return final_date.strftime("%M")


def generate_random_day(month):
  day_range = calendar.monthrange(2021,month)[1]
  return random.randint(1,day_range)



def generate_random_address():
  street_names = ['Bahadur Shah Zafar Marg', 'Ajmal Khan Road', 'Baba kharak singh Marg', 'Maulana Azad Road', 'Jawaharlal Nehru Marg', 'Tilak Marg', 'Maharaja Agrasen Road', 'Cannought Place', 'Rajiv Chowk', 'Prithvi Raj Road', 'Ansari Road', 'Sri Aurobindo Marg', 'Shyam Nath Marg']
  cities = ['Old delhi', 'NewDelhi', 'Central Delhi', 'East Delhi', 'West Delhi', 'South Delhi', 'North Delhi', 'Delhi_NCR', 'Border-Region']
  weights = [9,4,5,2,3,3,2,5,5]
  zips = ['110001', '110002', '110003', '110004', '110005', '110006', '110007', '110008', '110009', '110010']
  state = ['Delhi']
  street = random.choice(street_names)
  index = random.choices(range(len(cities)), weights=weights)[0]

  return f"{random.randint(1,999)} {street} St, {cities[index]}, {state[0]} {zips[index]}"

def generate_offers():
    percentage_off = ['10%','20%','30%','40%','50%','60%']
    by_using = ['paytmWallet',"on first order", "Axis bank Payment"]
    return f"{random.choice(percentage_off)} - {random.choice(by_using)}"

df = pd.DataFrame(columns=restuarants)
df1 = pd.DataFrame(columns=restuarants)
df2 = pd.DataFrame(columns=restuarants)


dummynumber = int(input("how much dummy data you want to generate? Enter in numbers: "))

for x in range(1, dummynumber+1):
    #rest = {}
    Restaurant_name = "Restaurant_"+str(x)
    Restaurant_id= "0"*(6-len(str(x))) + str(x)   
    '''
    0000      
    '''
    #ordering in the month of April
    Expected_Time= generate_random_time(4)
    promoted = random.choice(['yes','no'])
    category = random.choice(["FastFood","North Indian","south Indian","Cuisine","Italian","mangolian","chinese","Drinks"])
    location = generate_random_address()
    Ratings = random.randint(2,5)
    cost_for_two = random.randint(500,10000)
    offers = generate_offers()
    #menu is choosen randomly not according to the data ass more segregation of data is required.
    Veg_menu = random.sample(veg_menu,(numpy.random.randint(3,7)))
    Non_vegmenu = random.sample(non_vegmen,(numpy.random.randint(3,7)))
    Healthy_Food = random.sample(Healthy_food_items,(numpy.random.randint(3,7)))
    df1.loc[0] = [Restaurant_name,Restaurant_id,Expected_Time,promoted,category,location,Ratings,cost_for_two,offers,Veg_menu,Non_vegmenu,Healthy_Food]
    df1.to_csv('separate/dummyRestaurantData_20221{}.csv'.format(x),index=False)
    if x%2 != 0:
      df2.loc[0] = [Restaurant_name,Restaurant_id,Expected_Time,promoted,category,location,Ratings,cost_for_two,offers,Veg_menu,Non_vegmenu,Healthy_Food]
    else:
      df2.loc[1] = [Restaurant_name,Restaurant_id,Expected_Time,promoted,category,location,Ratings,cost_for_two,offers,Veg_menu,Non_vegmenu,Healthy_Food]
    if x%2==0:
        df2.to_csv('half_separate/dummy_RestaurantData_2021{}.csv'.format(int(x/2)),index=False)

    df.loc[x] = [Restaurant_name,Restaurant_id,Expected_Time,promoted,category,location,Ratings,cost_for_two,offers,Veg_menu,Non_vegmenu,Healthy_Food]
df.to_csv('single/dummyRestaurantData_2021.csv',index=False)

1
