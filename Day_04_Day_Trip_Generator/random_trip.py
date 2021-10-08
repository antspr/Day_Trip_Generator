import random
#Make a list to store each of the available variables
cities = ['New York','Miami','Los Angeles','London','Paris','Dubai','Hong Kong','Tokyo']
restaurants = ["Morton's","Nobu","McCormick's","a Speakeasy"," a Dive Bar"," a Picnic","McDonald's"," some Street Food"]
vehicles = ["Car","Bus","Train","Bicycle","Walking","Taxi","Horse and Buggy","Electric Scooter"]
activities = ["Concert","Play","Niteclub","Bowling","Sightseeing","Museum","Voluteering","Networking"]
def randomization_tool(random_list):
  for element in random_list:
    element = (random.choice(random_list))
    return element
approved = True #Want to use this to complete selection
trip_package_list = [randomization_tool(cities),randomization_tool(restaurants),randomization_tool(vehicles),randomization_tool(activities)]
trip_package_mixed_string = (f'You will be visiting: {trip_package_list[0]}, where you will be having {trip_package_list[1]} for dinner, traveling by way of {trip_package_list[2]}, and spend the day...{trip_package_list[3]}')
approved_package = [trip_package_list[0],trip_package_list[1],trip_package_list[2],trip_package_list[3]]#would like to call "return" variable from function?
approval = input(f'We have put together a trip, {trip_package_mixed_string}, Would you like to go on this trip? Y/N?')
if approval.upper() == 'Y':
    approved == True
    print(f'The trip where {trip_package_mixed_string} selection process is complete. Congratulations!')
elif approval.upper() == 'N':
  approved == True

  new_selection = int(input("""What would you like to change? 
      Choose "1" to change the destination, 
      "2" for a different place to eat 
      "3" for a different mode of travel 
      "4" for a different activity:"""))
  if new_selection == 1:
          approved_package[0]= randomization_tool(cities)
  elif new_selection == 2:
          approved_package[1]= randomization_tool(restaurants)
  elif new_selection == 3:
          approved_package[2]= randomization_tool(vehicles)
  elif new_selection == 4:
          approved_package[3]= randomization_tool(activities)
  approved == False
  
  confirmed = input(f'''Your trip now has you traveling to {approved_package[0]},
          eating at {approved_package[1]}, 
          traveling by {approved_package[2]},
          and hanging out {approved_package[3]} Please enter "Y" to confirm, "N" to ammend.''')
  if confirmed.lower() == 'y':
            print("Your trip has been confirmed")
  else:
    print(trip_package_mixed_string)
      


