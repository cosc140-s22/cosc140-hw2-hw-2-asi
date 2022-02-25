#######################################################
#Asianna Sample HW 2
# COSC 140 Homework 2, "bus trip planner" problem
#
#######################################################
departure = input("What time will your bus depart? HHMM ")
distance = input ("How far do you need to travel? (KM) ")
stops = input ("How many stops before your destination? ")
departure = int(departure)
distance = int (distance)
stops = int (stops)

if departure <=2400:
  #seperating the hours an minutes
  hours = departure // 100
  minutes = departure % 100

  if minutes <= 59:
  #Turning it into seconds in order to math it 
    hours_insec = hours * 3600
    min_insec = minutes * 60
    total_sec = hours_insec + min_insec#Will need to subtract
  
  #The amount of time to get places 
    time_stops = stops * 30 #30 because everything is in sec 
    total_time = (distance / 40) * 3600 #40km/hour into sec 
    arrival_time = total_sec + (time_stops + total_time)

  #arrival_sec = (total_sec + time_stops)/ total_time 
    final_hours = int(arrival_time % 86400)//3600
    final_minutes = int(arrival_time % 3600)//60
    final_sec = int(arrival_time % 60)

    print (f" Your bus will arrive at {final_hours:02d}:{final_minutes:02d}:{final_sec:02d}")
  else:
    print("Minutes are not valid. Please enter something equal or less than 59.")
  
else:
  print("Sorry, the time you have entered is not valid. Please try to enter an hour that is or less than 24. ")
  
