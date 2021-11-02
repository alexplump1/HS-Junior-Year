"""
world_list = ['w','o','r','l','d',]

integers = [-3,-2,-1,0,1,2,3]
floats = [-5.0, 0.5]
multi_type = ["hello", 2, "the", world_list]
empty = []
print(world_list)
print(world_list[0], world_list[1], world_list[2], world_list[3], world_list[4], type('a_list_element'), 'another_list_element','the_last_list_element')
"""
response = "string";
while(response != "end"):
    foodList = ["burger", "fries", "shake", "hotdog", "steak"];
    alternateFoodList = ["cheese"];
    response = raw_input("Pick a food and we'll tell you if it is in the list ")
    in_list = response in foodList
    in_otherList = response in alternateFoodList
    if in_list == True:
        print( str(response) + " is in the main list");
    else:
        print(str(response) + " is not in the main food list")
        if in_otherList == True:
            print(str(response) + " is already in the alternate list");
        elif in_otherList == False:
            foodList.append(response);
            #alternateFoodList[1] = response;
            #foodList.insert(0, response)
            print(str(response) + " has been added to the alternate list");
        else:
            print("There has been an error")
print(alternateFoodList);