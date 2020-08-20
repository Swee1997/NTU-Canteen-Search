# The canteenInfo dictionary will contain the info of all the canteens
# The necessary info of a canteen contains canteen name, image of the canteen, address, map,
# location, contact, operating time, seating capacity, stalls
# canteenInfo[str_canteenName][0] = image
# canteenInfo[str_canteenName][1] = address
# canteenInfo[str_canteenName][2] = map
# canteenInfo[str_canteenName][3] = location
# canteenInfo[str_canteenName][4] = contact
# canteenInfo[str_canteenName][5] = operating time
# canteenInfo[str_canteenName][6] = seating capacity
# canteenInfo[str_canteenName][7] = [x,y] coordinate
# canteenInfo[str_canteenName][8] = dictionary of stalls = canteenName_stallInfo{}
# canteenInfo[str_canteenName][9]= ranking of canteen
# canteenName_stallInfo[str_stallName][0] = whether halal or not
# canteenName_stallInfo[str_stallName][1] = whether vegetarian or not
# canteenName_stallInfo[str_stallName][i][0] = name of the ith dish
# canteenName_stallInfo[str_stallName][i][1] = price of the ith dish



# noinspection PyUnresolvedReferences
import pygame

# noinspection PyUnresolvedReferences
from pygame.locals import *

# noinspection PyUnresolvedReferences
from time import sleep

# to load file
import pickle

a_file = open( "data_file", "rb" )
datas_to_pack = pickle.load(a_file)
# info about stalls in each canteen, feedback dictionary, password for admin are being un-packed from the file.

canteen1_stallInfo = datas_to_pack[0][0]
canteen2_stallInfo = datas_to_pack[1][0]
canteen9_stallInfo = datas_to_pack[2][0]
canteen11_stallInfo = datas_to_pack[3][0]
canteen13_stallInfo = datas_to_pack[4][0]
canteen14_stallInfo = datas_to_pack[5][0]
canteen16_stallInfo = datas_to_pack[6][0]
ananda_stallInfo = datas_to_pack[7][0]
foodgle_stallInfo = datas_to_pack[8][0]
north_stallInfo = datas_to_pack[9][0]
pioneer_stallInfo = datas_to_pack[10][0]
quad_stallInfo = datas_to_pack[11][0]
feedback_dict = datas_to_pack[12]
password = datas_to_pack[13]

# below are the data structure for the canteen stall info, replaced now by file

# canteen1_stallInfo = {
#     "Korean Food" : [True, False, ["Bibimbap", 3.5], ["Kimchi Fried Rice", 3.0]],
#     "Chicken Rice" : [True, False, ["Steamed Chicken Rice", 2.5], ["Roasted Chicken Rice", 3.0]]
# }
#
# canteen2_stallInfo = {
#     "Indian Cuisine" : [True, False, ["Curry Chicken", 3.4], ["Egg Onion Prata", 1.0]],
#     "Pasta Express" : [False, False, ["Seafood Pasta", 4.0], ["Meatball Pasta", 3.5]]
# }
#
# canteen9_stallInfo = {
#     "Chinese Dishes" : [False, False, ["Sweet and Sour Pork", 3.5], ["Fried Beef Rice", 4.5]],
#     "Japanese Food" : [True, False, ["Teriyaki Chicken", 3.0], ["Egg Don", 3.2]]
# }
#
# canteen11_stallInfo = {
#     "Mala Hot Food" : [False, False, ["Fried Assorted Veggies", 3.6], ["Spicy Ribs", 4.1]],
#     "Veggie Land" : [True, True, ["Steamed Tofu", 1.5], ["Fried Broccoli", 1.0]]
# }
#
# canteen13_stallInfo = {
#     "Noodles Stall" : [False, False, ["Tom Yum Noodles", 3.5], ["Fishball Noodles", 3.0]],
#     "Thai Food" : [False, False, ["Pineapple Fried Rice", 3.3], ["Basil Leaf Chicken Rice", 4.7]]
# }
#
# canteen14_stallInfo = {
#     "Roasted Meat" : [True, False, ["Roasted Duck Rice", 3.8], ["Roasted Chicken Set", 4.3]],
#     "Veggie Land" : [True, True, ["Sweet and Sour Vegan Meat", 3.1], ["Special Set", 2.9]]
# }
#
# canteen16_stallInfo = {
#     "Japanese Ramen" : [False, False, ["Pork Broth Ramen", 4.9], ["Miso Soup Ramen", 4.7]],
#     "Dessert" : [True, True, ["Chocolate Cake", 2.3], ["Strawberry Short Cake", 2.2]]
# }
#
# ananda_stallInfo = {
#     "Korean Food" : [True, False, ["Bibimbap", 3.5], ["Kimchi Fried Rice", 3.0]],
#     "Chinese Dishes" : [False, False, ["Stir Fried Vegetables", 2.6], ["Chicken Soup", 3.0]]
# }
#
# foodgle_stallInfo = {
#     "Roasted Meat" : [False, False, ["Roasted Duck Rice", 3.5], ["Roasted Chicken Rice", 3.0]],
#     "Chicken Rice" : [True, False, ["Steamed Chicken Rice", 2.5], ["Roasted Chicken Rice", 3.0]]
# }
#
# north_stallInfo = {
#     "Korean Food" : [True, False, ["Bibimbap", 3.5], ["Kimchi Fried Rice", 3.0]],
#     "Chicken Rice" : [True, False, ["Steamed Chicken Rice", 2.5], ["Roasted Chicken Rice", 3.0]]
# }
#
# pioneer_stallInfo = {
#     "Japanese Food" : [True, False, ["Tampura", 3.5], ["Curry Chicken Udon", 3.0]],
#     "Chicken Rice" : [True, False, ["Steamed Chicken Rice", 2.5], ["Roasted Chicken Rice", 3.0]]
# }
#
# quad_stallInfo = {
#     "Japanese Ramen" : [False, False, ["Pork Broth Ramen", 3.5], ["Miso Soup Ramen", 3.0]],
#     "Mexican Food" : [True, False, ["Chipotle", 4.0], ["Corn Chips with Guacamole", 3.0]]
# }

canteenInfo = {
    "Canteen 1" : [["can1.jpg", 463, 260],
                    "21 Nanyang Circle Singapore 639778",
                    ["can1_map.png", 563 , 562],
                    "Hall 1",
                    "Tel: 6334 3033",
                    "Daily 7am to 9pm",
                     310,
                    (420,536),
                    canteen1_stallInfo,
                     1],
    "Canteen 2" : [["can2.png", 574, 312],
                    "35 Students Walk Singapore 639548",
                    ["can2_map.png", 563, 562],
                    "Hall 2",
                    "Tel: 6334 3033",
                    "Daily 7am to 9pm",
                    446,
                    (394,468),
                    canteen2_stallInfo,
                     2],
    "Canteen 9" : [["can9.png", 463, 260],
                    "50 Nanyang Avenue Singapore 639798",
                    ["can9_map.png", 563, 562],
                    "Hall 9",
                    "Tel: 9834 3844",
                    "Daily 7am to 9pm",
                    210,
                    (401,296),
                    canteen9_stallInfo,
                    3],
    "Canteen 11" : [["can11.png", 463, 260],
                    "20 Nanyang Avenue Singapore 639809",
                    ["can11_map.png", 463, 260],
                    "Hall 11",
                    "Tel: 9364 3746",
                    "Daily 7am to 9pm",
                    210,
                    (435,201),
                    canteen11_stallInfo,
                    4],
    "Canteen 13" : [["can13.png", 463, 260],
                    "32 Nanyang Cresent Singapore 637658",
                    ["can13_map.png", 463, 260],
                    "Hall 13",
                    "Tel: 9244 2324",
                    "Daily 7am to 9pm",
                    210,
                    (216,324),
                    canteen13_stallInfo,
                    5],
    "Canteen 14" : [["can14.png", 463, 260],
                    "34 Nanyang Crescent Singapore 637634",
                    ["can14_map.png", 463, 260],
                    "Hall 14",
                    "Tel: 9244 2324",
                    "Daily 7am to 9pm",
                    270,
                    (262,278),
                    canteen14_stallInfo,
                    6],
    "Canteen 16" : [["can16.png", 463, 260],
                    "50 Nanyang Walk Singapore 639929",
                    ["can16_map.png", 463, 260],
                    "Hall 16",
                    "Tel: 9244 2324",
                    "Daily 7am to 9pm",
                    300,
                    (214,379),
                    canteen16_stallInfo,
                    7],
    "Ananda Kitchen" : [["ananda.png", 463, 260],
                         "60 Nanyang Crescent Blk 19A #01-02 Singapore 636957",
                         ["ananda_map.png", 463, 260],
                         "North Hill Precinct",
                         "Tel: 9244 2324",
                         "Daily 7am to 9pm",
                         90,
                         (560,340),
                         ananda_stallInfo,
                         8],
    "Foodgle Food Court" : [["foodgle.png", 463, 260],
                             "38 Nanyang Crescent Blk 23, #051 - 058 Singapore 636866",
                             ["foodgle_map.png", 463, 260],
                             "Nanyang Crescent",
                             "Tel: 9244 2324",
                             "Daily 7am to 9pm",
                             120,
                             (516,239),
                             foodgle_stallInfo,
                             9],
    "North Hill Food Court" : [["north_hill.png", 463, 260],
                                "60 Nanyang Crescent Blk 21A, 02-02 Singapore 636957",
                                ["north_hill_map.png", 463, 260],
                                "North Hill Precinct",
                                "Tel: 9244 2324",
                                "Daily 7am to 9pm",
                                230,
                                (566,345),
                                north_stallInfo,
                                10],
    "Pioneer Food Court" : [["pioneer.png", 463, 260],
                             "162 Nanyang Cresent Singapore 637033",
                             ["pioneer_map.png", 463, 260],
                             "Pioneer Hall",
                             "Tel: 9244 2324",
                             "Daily 7am to 9pm",
                             230,
                             (532,561),
                             pioneer_stallInfo,
                             11],
    "Quad Cafe" : [["quad.png", 463, 260],
                    "60 Nanyang Drive SBS-B1N-10 Singapore 637551",
                    ["quad_map.png", 463, 260],
                    "School of Biological Sciences",
                    "Tel: 9244 2324",
                    "Daily 7am to 9pm",
                    190,
                    (235,587),
                    quad_stallInfo,
                    12]
}


# the loadImage function is used to display the image or the map of a canteen
def loadImage(background, length, height):

    pygame.init()

    screen = pygame.display.set_mode((length,height), 0 , 32)

    display = pygame.image.load(background).convert()

    pygame.event.get()
    screen.blit(display, (0,0))
    pygame.display.update()
    sleep(5)


# below is to display the map of campus to get the x,y coordinates of the user's location
pygame.init()
introScreenImage = pygame.image.load(r"campus_map.jpeg")
screen = pygame.display.set_mode((635, 867))
pygame.display.set_caption('NTU campus')
introScreenImage, (0, 0)

fault = False
p = 0
time = 0
while not fault and p < 3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fault = True

            elif event.type == pygame.MOUSEBUTTONUP:
                print('mouse at (x,y):', event.pos)
                user_location = event.pos
                p = p + 1

        screen.blit(introScreenImage, (0, 0))
        pygame.display.update()



# noinspection PyUnresolvedReferences
import math


# below is the function to calculate straight line distance between 2 points by using pythogoras' theorem
def distance_a_b(user_location, location_of_dest):
    displacement = math.sqrt((abs(user_location[0] - location_of_dest[0])) ** 2 +
                             abs((user_location[1] - location_of_dest[1])) ** 2)
    return round(displacement*2.65, 1)

dist_dicc = {}


# below is the function to sort distance by converting from a dictionary based on user's location
def sort_distance():
    for key in canteenInfo.keys():
        canteen_location = canteenInfo[key][7]
        displacement = distance_a_b(user_location, canteen_location)
        dist_dicc[key] = displacement
    sorted_value_dict = sorted(dist_dicc.items(), key=lambda t: t[1])
    return dict(sorted_value_dict)
    # dictionary sorted by value to give tuples in a list, then converted back to a dict.
    # key=lambda t:t[1] takes the 2nd elements in dist_dicc.items() and sort them, then assign them into tuple with the
    # corresponding key. Since the list now consist of key-value tuple pairs, dict() can be applied to give back dict.

ranking_dict = {}


def sort_rank():
    for key in canteenInfo.keys():
        canteen_ranking = canteenInfo[key][9]
        ranking_dict[key] = canteen_ranking
    sorted_ranking_dict = sorted(ranking_dict.items(), key=lambda t: t[1])
    return dict(sorted_ranking_dict)
    # dictionary sorted by value to give tuples in a list, then converted back to a dict.
    # key=lambda t:t[1] takes the 2nd elements in ranking_dict.items() and sort them, then assign them into
    # tuple with the corresponding key.
    # Since the list now consist of key-value tuple pairs, dict() can be applied to give back dict.


# the four funcs below are various search functions to filter the canteens
# so as to return the desired ones for the user
# search_by_food is a function to filter by the type of food
def search_by_food(food):
    for canteen in canteenInfo.keys():
        for stallName in canteenInfo[canteen][8].keys():
            if food == stallName:
                print(canteen, " has the food.")


# search_by_price is a function that returns recommended canteen/stall/dish/price according to the user's budget
def search_by_price(price):
    priceDict = {}
    for canteen in canteenInfo.keys():
        for stallName in canteenInfo[canteen][8].keys():
            try:
                for i in canteenInfo[canteen][8][stallName][2:4]:
                    canteenStallFood = (canteen, stallName, i[0])
                    priceDict[canteenStallFood] = i[1]
            except TypeError:
                pass

    return priceDict


# search_by_halal is a function that returns halal/non-halal canteens according to the user's preference
def search_by_halal(halal):
    halalDict = {}
    if halal == True:
        for canteen in canteenInfo.keys():
            for stallName in canteenInfo[canteen][8].keys():
               if canteenInfo[canteen][8][stallName][0] == True:
                   halalDict[canteen] = stallName
    return halalDict


# search_by_vegetarian is a function that returns vegetarian/non-vegetarian canteens according to the user's like
def search_by_vegetarian(vege):
    vegeDict = {}
    if vege == True:
        for canteen in canteenInfo.keys():
            for stallName in canteenInfo[canteen][8].keys():
               if canteenInfo[canteen][8][stallName][1] == True:
                   vegeDict[canteen] = stallName
    return vegeDict


# below is the function for user to input feedback
def give_feedback():
    while True:
        user_feedback = input("Please type any feedback you would want to give to the particular canteen: ")
        return user_feedback


# below is the function to determine under which canteen is the feedback directed to and store feedback in a dictionary
def feedback_dict_add(canteen_no):
    feedback = feedback_dict
    # assign dict to feedback
    for keys in canteenInfo.keys():
        if keys == canteen_in_order[(canteen_no-1)]:
            try:
                feedback[keys] = str.join('.',(feedback[keys] , give_feedback())) # adding on to previous feedback
            except KeyError:                                                       # with '.' as seperator
                feedback[keys] = give_feedback()                                   # for cases that do not have
    return feedback                                                                # pre-loaded feedback


# function to get the canteen_coor from user's input
def get_canteen_coor(canteen_no):
    for keys in canteenInfo.keys():
        if keys == canteen_in_order[(canteen_no-1)]:
            canteen_location = canteenInfo[keys][7]
            return canteen_location


# below is the function to get the name and price of the dish that admin wants to update
def get_name_price_dish():
    while True:
        name_dish = input("Please enter a dish name")
        while True:
            price_of_dish = input("Please input the price the dish")
            try:
                price_of_dish_1dec = round(float(price_of_dish), 1)
                break
            except:         # when admin inputs other than int/float
                print("Please input an integer")
        name_price = [name_dish, price_of_dish_1dec]           # puts name and price of dish into a list
        print("The dish name is", name_dish, "and the price of", name_dish, "is", price_of_dish_1dec)
        while True:
            proceed_or_not = input("Please input '1' to confirm or '0' to re-enter")    # to confirm with admin of input
            if proceed_or_not == "0":
                break
            elif proceed_or_not == "1":
                return name_price
            else:            # inputs other than '0' or '1'
                print("Invalid input")

# below is the function ask admin whether stall is halal or veg
def stall_is(halal_or_veg):
    while True:
        print("Please input '1' if the stall is", halal_or_veg, ", '0' if it is not")
        type_of_food = input("Please input here ")
        if type_of_food == "1":
            while True:
                proceed_or_not = input("You have entered 'Yes' for halal"
                                       "Please input '1' to confirm or '0' to re-enter ")
                if proceed_or_not == "1":
                    return True              # Returns halal_or_veg is True
                elif proceed_or_not == "0":
                    break
                else:                    # inputs other than '0' or '1'
                    print("Invalid input")

        elif type_of_food == "0":
            while True:
                proceed_or_not = input("You have entered 'No' for halal"
                                       " Please input '1' to confirm or '0' to re-enter ")
                if proceed_or_not == "1":
                    return False                # Returns halal_or_veg is False
                elif proceed_or_not == "0":
                    break
                else:                           # inputs other than '0' or '1'
                    print("Invalid input")

        else:
            print("Invalid input")


# below is the function to get the updated list, using the data structure format for the canteen stall info dict
def update_stall_dictionary():
    canteen_stall_info = [stall_is("halal"), stall_is("veg"), get_name_price_dish()]
    while True:
        print(canteen_stall_info)
        add_more_dish = input("Please input '1' to add more dish, '0' to exit")
        if add_more_dish == "1":
            canteen_stall_info.append(get_name_price_dish())        # append the name & price of dish in list
        elif add_more_dish == "0":
            return canteen_stall_info              # returns into the format of the data structure
        else:
            print("invalid input")


# below is the function to add the updated list into the dictionary with it's canteen stall name
def update_stall_dict_canteen(canteen):
    while True:
        keys = input("Please input your new stall name ")
        print("You have input ", keys, "as your stall name, Please input '1' to confirm or '0' to re-enter")
        proceed_or_not = input("Please input here ")
        if proceed_or_not == "1":
            for key in canteenInfo.keys():
                if key == canteen_in_order[(canteen - 1)]:        # match the order of the list of canteen_in_order
                    canteenInfo[key][8][keys] = update_stall_dictionary()
                    return canteenInfo[key][8][keys]              # return the updated canteen stall info
        elif proceed_or_not == "0":                    # go back to loop
            continue
        else:
            print("Invalid input")                   # inputs other than '1' or '0'


# below is the function to delete the key:pair of the canteen store
def delete_stall_dict_canteen(canteen):
    canteen_del = input("Please key in the canteen store's name that you would "
                        "want to delete, caps and space sensitive")
    canteen_stalls = canteen_stalls_in_order[(canteen - 1)]       # match the order of the list of canteen_in_order
    for key in canteen_stalls.keys():
        if key == canteen_del:                                    # check if the input has canteen store name in dict
            canteen_stalls_new = canteen_stalls.pop(key)
            return canteen_stalls_new                             # returns the deleted canteen_store dict




# BUS ROUTE FUNCTION
# Canteen : [x,y,busstop index,Canteen_x,Canteen_y]

Bus_red = {"Canteen 1" : [439,488,1,420,536],
           "Canteen 2" : [394,441,2,394,468],
           "Canteen 9" : [406,335,3,401,296],
           "Ananda Kitchen" : [455,225,4,560,340],
           "North Hill Food Court" : [455,255,4,566,345],
           "Canteen 11" : [455,225,4,435,201],
           "busstop 1" : [432,155,5,0,0],
           "Foodgle Food Court" : [345,201,6,516,239],
           "Canteen 14" : [259,260,7,262,278],
           "Canteen 13" : [200,316,8,216,324],
           "Canteen 16" : [200,316,8,214,379],
           "Quad Cafe" : [106,548,10,235,587],
           "busstop 2" : [126,717,11,0,0],
           "busstop 3" : [232,798,12,0,0],
           "busstop 4" : [314,715,13,0,0],
           "busstop 5" : [428,651,14,0,0],
           "Pioneer Food Court" : [498,576,15,532,561]
           }

Bus_blue = {"Canteen 1" : [439,488,1,420,536],
            "Canteen 2" : [394,441,13,394,468],
            "Canteen 9" : [406,335,12,401,296],
            "Ananda Kitchen" : [455,225,11,560,340],
            "North Hill Food Court" : [455,255,11,566,345],
            "Canteen 11" : [455,225,11,435,201],
            "Foodgle Food Court" : [345,201,10,516,239],
            "Canteen 14" : [259,260,9,262,278],
            "Canteen 13" : [200,316,8,216,324],
            "Canteen 16" : [200,316,8,214,379],
            "Quad Cafe" : [106,548,6,235,587],
            "Pioneer Food Court" : [498,576,2,532,561]
           }


# 1. Print out the first 5 canteens for the particular category (need to fliter to show only top 5 canteen)
# 2. Let user choose out of the 5 canteen (user to choose 1,2,3,4,5, x put into the key value to get location)
# OR JUST CR8 CHOOSE CANTEEN FUNCTION
# 3. Give the keys, values for the coordinate of the particular canteen, give to the function
# 4. Direction will be written( walk how long, take how many bus stops,
# functions will cover pythagoras to bus stop or canteen)
# 5. Tell user to walk or to take bus
def routes(user_x,user_y,canteen_x,canteen_y):
    Final_busstop_Blue=0
    Bus_index_blue=0
    Final_busstop_red=0
    Bus_index_red=0
    finalBus_x=0
    finalBus_y=0
    #initial declarations

    dist_canteen = distance_a_b((user_x,user_y),(canteen_x,canteen_y))/2.65
    distsmallest_bus=10000

    for l in Bus_blue.keys():
        if(canteen_x == Bus_blue[l][3] ):
            Final_busstop_Blue = Bus_blue[l][2]
            finalBus_x = Bus_blue[l][0]
            finalBus_y = Bus_blue[l][1]     # Coordinates of final bus stop
            break
            # get final blue bus stop index

    for r in Bus_red.keys():
        if (canteen_x == Bus_red[r][3]):
            Final_busstop_red = Bus_red[r][2]
            break
            # get final red bus stop index

    for i in Bus_red.keys():
        dist_bus = distance_a_b((user_x,user_y),(Bus_red[i][0],Bus_red[i][1]))/2.65
        # distance from user to each red bus stop
        if(dist_bus < distsmallest_bus):
            distsmallest_bus = dist_bus
            smallest_index_r = i                    # Finds out the nearest red bus stop coordinates
            bus_x = Bus_red[smallest_index_r][0]
            bus_y = Bus_red[smallest_index_r][1]
            # get initial red busstop x,y

    for a in Bus_red.keys():
        if(bus_x == Bus_red[a][0] and bus_y == Bus_red[a][1]):
            Bus_index_red=Bus_red[a][2]       # Find out the nearest red bus stop index
            break
            # get initial red busstop index

    for k in Bus_blue.keys():
        dist_bus = distance_a_b((user_x,user_y),(Bus_blue[i][0],Bus_blue[i][1]))/2.65
        if(dist_bus < distsmallest_bus):
            distsmallest_bus = dist_bus
            smallest_index_b = k                # Finds out the nearest Blue bus stop coordinates
            bus_x = Bus_blue[smallest_index_b][0]
            bus_y = Bus_blue[smallest_index_b][1]
            # get initial blue busstop x,y

    for n in Bus_blue.keys():
        if(bus_x == Bus_blue[n][0] and bus_y == Bus_blue[n][1]):
            Bus_index_blue=Bus_blue[n][2]       # Finds out the nearest Blue bus stop index
            break
            # get initial blue busstop index

    if (dist_canteen <= distsmallest_bus):
        time = math.sqrt((user_x - canteen_x) ** 2 + (user_y - canteen_y) ** 2) / 17.2
        return print("Walk for", round(time,1), "minutes")
            # deciding to walk there only

    elif (dist_canteen >= distsmallest_bus):
        time = math.sqrt((user_x - bus_x) ** 2 + (user_y - bus_y) ** 2) / 17.2
        print("Walk for", round(time,1), "minutes to the nearest bus stop.")
            # deciding to walk to the busstop (bus_x,y already the nearest busstop form user)

    busBlue_index_distance = Final_busstop_Blue - Bus_index_blue
    if(busBlue_index_distance < 0):
        busBlue_index_distance += 13
            # In the case where bus route goes over the loop index.
    busRed_index_distance = Final_busstop_red - Bus_index_red
    if(busRed_index_distance < 0):
        busRed_index_distance += 15
            # In the case where bus route goes over the loop index.
    if (abs(busRed_index_distance) <= abs(busBlue_index_distance)):
        print("Take red line bus for", abs(busRed_index_distance), " stops")
        time_buscanteen = math.sqrt(abs(finalBus_x - canteen_x) ** 2 + abs(finalBus_y - canteen_y) ** 2)/17.2
        print("From the busstop walk",round(time_buscanteen,1),"minutes to get to the the canteen :)")
    else:
        print("Take Blue Line Bus for", abs(busBlue_index_distance), "stops")
        time_buscanteen = math.sqrt(abs(finalBus_x - canteen_x) ** 2 + abs(finalBus_y - canteen_y) ** 2) / 17.2
        print("From the busstop walk", round(time_buscanteen,1), "minutes to get to the the canteen :)")
        # Deciding to take red or blue bus.
    return " "

# User Interface
# 1. request for user's location whenever program starts

# Main Menu:
# 1. Sort canteen by...
# 2. Feedback for canteen
# 3. Update info
# 4. Info about canteen

# Sort canteen by
# 1 Distance
# 2 Ranking
# 3 Food > Types of food, halal and vegetarian P.S.(we provide the options for users to choose)
# 4 Price

def option_input_int():
    while True:
        option_input = input("Please enter your option: ")
        try:
            option_input_int = int(option_input)
            return option_input_int
        except:
            print("Invalid input")


def showMsg_main():
    print("Welcome to the NTU canteen informatory app!")
    print("1: Sort canteen by")
    print("2: Feedback for canteen")
    print("3: Update of database,(admin)")
    print("4. Info about each canteen")
    print("5: Direction to your preferred canteen")
    print("0: Exit")


def showMsg_sort():
    print("1: Sort by distance")
    print("2: Sort by ranking")
    print("3: Sort by types of food")
    print("4: Sort by price")
    print("0: Exit")


def showMsg_sort_type():
    print("1: Korean food")
    print("2: Chicken rice")
    print("3: Indian cuisine")
    print("4: Pasta")
    print("5: Chinese dishes")
    print("6: Japanese food")
    print("7: Japanese ramen")
    print("8: Mala hot food")
    print("9: Veggie")
    print("10: Noddles")
    print("11: Thai food")
    print("12: Roasted meat")
    print("13: Mexican food")
    print("14: Dessert")
    print("15: Halal")
    print("16: Vegetarian")
    print("0: Exit")


def showMsg_feedback():
    print("Welcome to the feedback section, please input the canteen's option number to provide feedbacks regarding that canteen")
    print("1: Canteen 1")
    print("2: Canteen 2")
    print("3: Canteen 9")
    print("4: Canteen 11")
    print("5: Canteen 13")
    print("6: Canteen 14")
    print("7: Canteen 16")
    print("8: Anada Kitchen")
    print("9: Foodgle Food Court")
    print("10: North Hill Food Court")
    print("11: Pioneer Food Court")
    print("12: Quad Cafe")
    print("0: Exit")


def showMsg_info():
    print("1: canteen 1")
    print("2: canteen 2")
    print("3: canteen 9")
    print("4: canteen 11")
    print("5: canteen 13")
    print("6: canteen 14")
    print("7: canteen 16")
    print("8: canteen Ananda Kitchen")
    print("9: canteen Foodgle Food Court")
    print("10: canteen North Hill Food Court")
    print("11: canteen Pioneer Food Court")
    print("12: canteen Quad Cafe")
    print("0: Exit")


def showMsg_admin1():
    print("Welcome admin! Please enter your option")
    print("1: View of feedback")
    print("2: Delete all feedback")
    print("3: Update of new stall of a certain canteen")
    print("4: Remove of stall of a certain canteen")
    print("0: Exit")


def display_info(canteen, pic, map):
    while True:
        print("Address: ", canteenInfo[canteen][1])
        print("Location: ", canteenInfo[canteen][3])
        print("Contact: ", canteenInfo[canteen][4])
        print("Operating time: ", canteenInfo[canteen][5])
        print("Seating capacity: ", canteenInfo[canteen][6])
        print("Ranking: ", canteenInfo[canteen][9])
        print("Information about each stall in the canteen: ", canteenInfo[canteen][8])
        print("1: Show picture of the canteen")
        print("2: Show map of the canteen")
        print("0: Exit")
        option2_1 = option_input_int()
        if option2_1 == SHOWPIC:
            loadImage(pic, 463, 260)
        elif option2_1 == SHOWMAP:
            loadImage(map, 463, 260)
        elif option2_1 == EXIT:
            break



SORT = DISTANCE = KOREAN = CANTEEN1 = SHOWPIC = VIEW = 1
FEEDBACK = RANKING = CHICKEN = CANTEEN2 = SHOWMAP = WIPE = 2
ADMIN = TYPE_OF_FOOD = INDIAN = CANTEEN9 = UPDATE_STALL = 3
PASTA = PRICE = INFO = CANTEEN11 = DELETE_STALL = 4
CHINESE = CANTEEN13 = DIRECTIONS = 5
JAPANESE_FOOD = CANTEEN14 = 6
JAPANESE_RAMEN = CANTEEN16 = 7
MALA = ANANDA = 8
VEGGIE = FOODGLE = 9
NOODLE = NORTHHILL = 10
THAI = PIONEER = 11
ROASTED_MEAT = QUAD = 12
MEXICAN = 13
DESSERT = 14
HALAL = 15
VEGETARIAN = 16
EXIT = 0

canteen_in_order = ["Canteen 1","Canteen 2","Canteen 9","Canteen 11","Canteen 13","Canteen 14","Canteen 16",
                    "Ananda Kitchen","Foodgle Food Court","North Hill Food Court","Pioneer Food Court","Quad Cafe"]

canteen_stalls_in_order = [canteen1_stallInfo, canteen2_stallInfo,canteen9_stallInfo,canteen11_stallInfo,
                           canteen13_stallInfo,canteen14_stallInfo,canteen16_stallInfo,ananda_stallInfo,
                           foodgle_stallInfo,north_stallInfo,pioneer_stallInfo,quad_stallInfo]

# the following codes are to print out data that user wants to see
while True:
    print()
    showMsg_main()
    option = option_input_int()     # function to check if it's valid
    if option == SORT:
        while True:
            print()
            showMsg_sort()
            option_1 = option_input_int()       # function to check if it's valid
            if option_1 == DISTANCE:
                canteens_by_distance = sort_distance()
                print("The nearest canteens (distance in metre) are: ", canteens_by_distance, " in ascending order.")
            elif option_1 == RANKING:
                canteens_by_rank = sort_rank()
                print("The best canteens are: ", canteens_by_rank, " in descending order.")
            elif option_1 == TYPE_OF_FOOD:
                while True:
                    print()
                    showMsg_sort_type()
                    option1_3 = option_input_int()      # function to check if it's valid
                    if option1_3 == KOREAN:
                        search_by_food("Korean Food")
                    elif option1_3 == CHICKEN:
                        search_by_food("Chicken Rice")
                    elif option1_3 == INDIAN:
                        search_by_food("Indian Cuisine")
                    elif option1_3 == PASTA:
                        search_by_food("Pasta Express")
                    elif option1_3 == CHINESE:
                        search_by_food("Chinese Dishes")
                    elif option1_3 == JAPANESE_FOOD:
                        search_by_food("Japanese Food")
                    elif option1_3 == JAPANESE_RAMEN:
                        search_by_food("Japanese Ramen")
                    elif option1_3 == MALA:
                        search_by_food("Mala Hot Food")
                    elif option1_3 == VEGGIE:
                        search_by_food("Veggie Land")
                    elif option1_3 == NOODLE:
                        search_by_food("Noodles Stall")
                    elif option1_3 == THAI:
                        search_by_food("Thai Food")
                    elif option1_3 == ROASTED_MEAT:
                        search_by_food("Roasted Meat")
                    elif option1_3 == MEXICAN:
                        search_by_food("Mexican Food")
                    elif option1_3 == DESSERT:
                        search_by_food("Dessert")
                    elif option1_3 == HALAL:
                        print(search_by_halal(halal=True))
                    elif option1_3 == VEGETARIAN:
                        print(search_by_vegetarian(vege=True))
                    elif option1_3 == EXIT:
                        break
            elif option_1 == PRICE:
                price_str = input("Enter the maximum price you would like to afford: ")
                price_float = float(price_str)
                print(search_by_price(price_float))
            elif option_1 == EXIT:
                break
    elif option == INFO:
        while True:
            showMsg_info()
            option_2 = option_input_int()
            if option_2 == CANTEEN1:
                display_info("Canteen 1","can1.jpg","can1_map.png")
            elif option_2 == CANTEEN2:
                display_info("Canteen 2","can2.png","can2_map.png")
            elif option_2 == CANTEEN9:
                display_info("Canteen 9","can9.png","can9_map.png")
            elif option_2 == CANTEEN11:
                display_info("Canteen 11","can11.png","can11_map.png")
            elif option_2 == CANTEEN13:
                display_info("Canteen 13","can13.png","can13_map.png")
            elif option_2 == CANTEEN14:
                display_info("Canteen 14","can14.png","can14_map.png")
            elif option_2 == CANTEEN16:
                display_info("Canteen 16","can16.png","can16_map.png")
            elif option_2 == ANANDA:
                display_info("Ananda Kitchen","ananda.png","ananda_map.png")
            elif option_2 == FOODGLE:
                display_info("Foodgle Food Court","foodgle.png","foodgle_map.png")
            elif option_2 == NORTHHILL:
                display_info("North Hill Food Court","north_hill.png","north_hill_map.png")
            elif option_2 == PIONEER:
                display_info("Pioneer Food Court","pionner.png","pioneer_map.png")
            elif option_2 == QUAD:
                display_info("Quad Cafe","quad.jpg","quad_map.png")
            elif option_2 == EXIT:
                break
    elif option == FEEDBACK:
        while True:
            print()
            showMsg_feedback()
            option_2 = option_input_int()
            if option_2 == CANTEEN1:
                feedback_dict = feedback_dict_add(1)
            elif option_2 == CANTEEN2:
                feedback_dict = feedback_dict_add(2)
            elif option_2 == CANTEEN9:
                feedback_dict = feedback_dict_add(3)
            elif option_2 == CANTEEN11:
                feedback_dict = feedback_dict_add(4)
            elif option_2 == CANTEEN13:
                feedback_dict = feedback_dict_add(5)
            elif option_2 == CANTEEN14:
                feedback_dict = feedback_dict_add(6)
            elif option_2 == CANTEEN16:
                feedback_dict = feedback_dict_add(7)
            elif option_2 == ANANDA:
                feedback_dict = feedback_dict_add(8)
            elif option_2 == FOODGLE:
                feedback_dict = feedback_dict_add(9)
            elif option_2 == NORTHHILL:
                feedback_dict = feedback_dict_add(10)
            elif option_2 == PIONEER:
                feedback_dict = feedback_dict_add(11)
            elif option_2 == QUAD:
                feedback_dict = feedback_dict_add(12)
            elif option_2 == EXIT:
                break
            else:
                print("invalid input")
                continue
    elif option == ADMIN:
        print("Welcome admin!")
        while True:
            password_input = input("Please enter your password to verify your identity, else press '0' to go exit: ")
            if password == password_input:
                showMsg_admin1()
                option_3 = option_input_int()
                if option_3 == VIEW:
                    print(feedback_dict)
                elif option_3 == WIPE:
                    feedback_dict = {}
                elif option_3 == UPDATE_STALL:
                    while True:
                        print()
                        print("Please select the canteen that the new stall will be in")
                        showMsg_info()
                        option3_3 = option_input_int()  # function to check if it's valid
                        if option3_3 == CANTEEN1:
                            update_stall_dict_canteen(1)
                        elif option3_3 == CANTEEN2:
                            update_stall_dict_canteen(2)
                        elif option3_3 == CANTEEN9:
                            update_stall_dict_canteen(3)
                        elif option3_3 == CANTEEN11:
                            update_stall_dict_canteen(4)
                        elif option3_3 == CANTEEN13:
                            update_stall_dict_canteen(5)
                        elif option3_3 == CANTEEN14:
                            update_stall_dict_canteen(6)
                        elif option3_3 == CANTEEN16:
                            update_stall_dict_canteen(7)
                        elif option3_3 == ANANDA:
                            update_stall_dict_canteen(8)
                        elif option3_3 == FOODGLE:
                            update_stall_dict_canteen(9)
                        elif option3_3 == NORTHHILL:
                            update_stall_dict_canteen(10)
                        elif option3_3 == PIONEER:
                            update_stall_dict_canteen(11)
                        elif option3_3 == QUAD:
                            update_stall_dict_canteen(12)
                        elif option3_3 == EXIT:
                            break
                        else:
                            print("invalid input")
                            continue
                elif option_3 == DELETE_STALL:
                    while True:
                        print()
                        print("Please select the store's canteen that you want to delete")
                        showMsg_info()
                        option3_4 = option_input_int()  # function to check if it's valid
                        if option3_4 == CANTEEN1:
                            delete_stall_dict_canteen(1)
                        elif option3_4 == CANTEEN2:
                            delete_stall_dict_canteen(2)
                        elif option3_4 == CANTEEN9:
                            delete_stall_dict_canteen(3)
                        elif option3_4 == CANTEEN11:
                            delete_stall_dict_canteen(4)
                        elif option3_4 == CANTEEN13:
                            delete_stall_dict_canteen(5)
                        elif option3_4 == CANTEEN14:
                            delete_stall_dict_canteen(6)
                        elif option3_4 == CANTEEN16:
                            delete_stall_dict_canteen(7)
                        elif option3_4 == ANANDA:
                            delete_stall_dict_canteen(8)
                        elif option3_4 == FOODGLE:
                            delete_stall_dict_canteen(9)
                        elif option3_4 == NORTHHILL:
                            delete_stall_dict_canteen(10)
                        elif option3_4 == PIONEER:
                            delete_stall_dict_canteen(11)
                        elif option3_4 == QUAD:
                            delete_stall_dict_canteen(12)
                        elif option3_4 == EXIT:
                            break
                        else:
                            print("invalid input")
                            continue
                elif option_3 == EXIT:
                    break
            elif password_input == "0":
                break
            else:
                print("Invalid input.")
    elif option == DIRECTIONS:
        print()
        showMsg_info()
        option_4 = option_input_int()
        if option_4 == CANTEEN1:
            canteen_location = get_canteen_coor(1)
            routes(user_location[0], user_location[1], canteen_location[0], canteen_location[1])
        elif option_4 == CANTEEN2:
            canteen_location = get_canteen_coor(2)
            routes(user_location[0], user_location[1], canteen_location[0], canteen_location[1])
        elif option_4 == CANTEEN9:
            canteen_location = get_canteen_coor(3)
            routes(user_location[0], user_location[1], canteen_location[0], canteen_location[1])
        elif option_4 == CANTEEN11:
            canteen_location = get_canteen_coor(4)
            routes(user_location[0], user_location[1], canteen_location[0], canteen_location[1])
        elif option_4 == CANTEEN13:
            canteen_location = get_canteen_coor(5)
            routes(user_location[0], user_location[1], canteen_location[0], canteen_location[1])
        elif option_4 == CANTEEN14:
            canteen_location = get_canteen_coor(6)
            routes(user_location[0], user_location[1], canteen_location[0], canteen_location[1])
        elif option_4 == CANTEEN16:
            canteen_location = get_canteen_coor(7)
            routes(user_location[0], user_location[1], canteen_location[0], canteen_location[1])
        elif option_4 == ANANDA:
            canteen_location = get_canteen_coor(8)
            routes(user_location[0], user_location[1], canteen_location[0], canteen_location[1])
        elif option_4 == FOODGLE:
            canteen_location = get_canteen_coor(9)
            routes(user_location[0], user_location[1], canteen_location[0], canteen_location[1])
        elif option_4 == NORTHHILL:
            canteen_location = get_canteen_coor(10)
            routes(user_location[0], user_location[1], canteen_location[0], canteen_location[1])
        elif option_4 == PIONEER:
            canteen_location = get_canteen_coor(11)
            routes(user_location[0], user_location[1], canteen_location[0], canteen_location[1])
        elif option_4 == QUAD:
            canteen_location = get_canteen_coor(12)
            routes(user_location[0], user_location[1], canteen_location[0], canteen_location[1])
        elif option_4 == EXIT:
            break
        else:
            print("invalid input")
            continue
    elif option == EXIT:
        break
    else:
        print("invalid input")
        continue

print("Thank you for using the app")


datas_to_pack = []                              # the data in a list going to be loaded into the file
for key in canteenInfo.keys():
    canteen_stalls_end = [canteenInfo[key][8]]
    datas_to_pack.append(canteen_stalls_end)    # add all canteen stall info into list for storing

datas_to_pack.append(feedback_dict)         # add into the list for file storing
datas_to_pack.append(password)

a_file = open("data_file", "wb")
pickle.dump(datas_to_pack, a_file)

a_file.close()

