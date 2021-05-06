#imports
import os
import time
#variables
zero = (0)
healthf = (0)
healthinfo = (0)
with open("Foodeaten.txt") as f: #in read mode, not in write mode, careful
    caloriese=f.readlines()
calories2 = (caloriese[0])
calories = float(calories2)
with open("hieght.txt") as f: #in read mode, not in write mode, careful
    heighte=f.readlines()
height2 = (heighte[0])
height = float(height2)
with open("weight.txt") as f: #in read mode, not in write mode, careful
    weighte=f.readlines()
weight2 = weighte[0]
weight = float(weight2)
with open("awaketime.txt") as f: #in read mode, not in write mode, careful
    awaketimee=f.readlines()
awaketime2 = awaketimee[0]
awaketime = float(awaketime2)
with open("sleep.txt") as f: #in read mode, not in write mode, careful
    sleepe=f.readlines()
sleep2 = sleepe[0]
sleep = float(sleep2)
act = (0)
act2 = (0)
with open("bmi.txt") as f: #in read mode, not in write mode, careful
    bmie=f.readlines()
bmi2 = bmie[0]
bmi = float(bmi2)
#health facts
sd = ("Staying up for long periods of time can highten your chances of heart attacks or stroke. Try to get more sleep tonight!")
lc = ("Restricting calorie intake to fewer than 1,000 calories daily can slow down your metabolic rate and lead to fatigue since you're not taking in enough calories to support even the basic functions that keep you alive. Try eating another meal today!")
lcas = ("Not getting enough calories and sleep can lead to very quick fatigue and make it harder to focus, and take in information. Try eating another meal and get more sleep tonight!")
udw = ("From your BMI you seem to be underweight, being underweight can lead to malnutrition, osteoporosis, or weakened immune system. Try eating a big meal today!")
ovw = ("From your BMI you seem to be overweight being overweight can lead to cardiovascular diseases mainly heart disease and stroke, and type 2 diabetes. Try dieting it may help prevent these issues in teh future!")
prfct = ("You seem to be in perfect shape from your info provided, Keep up the good work!")
def healthfpu():
  hfact()
  if hfact.healthf == int(1):
    print("Restricting calorie intake to fewer than 1,000 calories daily can slow down your metabolic rate and lead to fatigue since you're not taking in enough calories to support even the basic functions that keep you alive. Try eating another meal today!")
  elif hfact.healthf == int(12):
    print("Not getting enough calories and sleep can lead to very quick fatigue and make it harder to focus, and take in information. Try eating another meal and get more sleep tonight!")
  elif hfact.healthf == int(117):
    print("Staying up for long periods of time can highten your chances of heart attacks or stroke. Try to get more sleep tonight!")
  elif hfact.healthf == int(8):
    print("From your BMI you seem to be underweight, being underweight can lead to malnutrition, osteoporosis, or weakened immune system. Try eating a big meal today!")
  elif hfact.healthf == int(26):
    print("From your BMI you seem to be overweight being overweight can lead to cardiovascular diseases mainly heart disease and stroke, and type 2 diabetes. Try dieting it may help prevent these issues in teh future!")
  elif hfact.healthf == int(100):
    print("You seem to be in perfect shape from your info provided, Keep up the good work!")
#functions
#health facts processor
def hfact():
  if (calories) < (150):
    hfact.healthf = (1)
    if (sleep) < (3):
      hfact.healthf = (12)
  elif (sleep) < (3):
    hfact.healthf = (117)
  elif (bmi) < (18):
    hfact.healthf = (8)
  elif (bmi) > (25):
    hfact.healthf = (26)
  elif (calories) > (700):
      if (sleep) > (7):
        if (bmi) > (8) and (bmi) < (25):
          hfact.healthf = (100)
  else:
    print("Critical error in system")
    wait = input("Pleae press enter")
def nothing():
  pass
def clearc():
  clear = lambda: os.system('clear')
  clear()
def yhb(): #your health bar
  #display heath bar stuff
  print("Welcome to your Genki health dashboard"), print("Your BMI is",bmi), print("You had gotten",sleep,"hours of sleep"), print("You've been awake for",awaketime,"hours")
  print("")
  print("Dashboard Options")
  print("[0] Facts about my health")
  print("[1] My info")
  print("[2] Update my info")
  print("[3] Delete my data")
  userinput = float(input())
  if userinput == 0:
    clearc()
    print("**************************************")
    healthfpu()
    print("***************************************")
    wait = input("Press enter to return to Genki Menu")
    clearc()
  elif userinput == 1:
    clearc()
    print("Time slept",sleep)
    print("Your weight",weight,"pounds")
    print("Your hight(inches)",height)
    print("Calories consumed today", calories)
    print("Time awake",awaketime,"hours")
    print("Your BMI", bmi)
    wait = input("Press enter to return to Genki Menu")
    clearc()
  elif userinput == 2:
    clearc()
    hightinput = float(input("Please enter the new updated weight "))
    clearc()
    weightinput = float(input("Please enter the new updated weight "))
    clearc()
    with open("hieght.txt","w") as f: #in write mode
      f.write("{}".format(hightinput))
    with open("weight.txt","w") as f: #in write mode
      f.write("{}".format(weightinput))
    print("Data has been updated")
    wait = input("Press enter to return to Genki Menu")
  elif userinput == 3:
    clearc()
    print("Are you sure you want to wipe all your data?")
    userinput = input("Type 1 to comfirm")
    clearc()
    #make data wipe here
    with open("hieght.txt","w") as f: #in write mode
      f.write("{}".format(zero))
    with open("weight.txt","w") as f: #in write mode
      f.write("{}".format(zero))
    with open("awaketime.txt","w") as f: #in write mode
      f.write("{}".format(zero))
    with open("bmi.txt","w") as f: #in write mode
      f.write("{}".format(zero))
    with open("sleep.txt","w") as f: #in write mode
      f.write("{}".format(zero))
    with open("Foodeaten.txt","w") as f: #in write mode
      f.write("{}".format(zero))
    print("All personal data has been deleted")
    wait = input("Press enter to return to Genki Menu")
    clearc
  else:
    print("Invalid option detected")
    wait = input("press enter to restart")
    clearc()

#display time
def ct():
  import time
  t = time.localtime()
  ct.ctc = time.strftime("%H:%M", t)
  print("The current time is",ct.ctc)


#test if started with info before
with open("hieght.txt") as f: #in read mode, not in write mode, careful
    hh=f.readlines()
ht = float(hh[0])
if (ht) == 0:
  act = (1)
else:
  nothing()
with open("weight.txt") as f: #in read mode, not in write mode, careful
    wh=f.readlines()
wt = float(wh[0])
if (wt) == 0:
  act2 = (1)
else:
  nothing()


#startup checker
if act == 1:
  wait = input("I see this is the first time running Genki™ press enter to begin setup? ")
  clearc()
  hightinput = float(input("Please enter your height in inches."))
  with open("hieght.txt","w") as f: #in write mode
    f.write("{}".format(hightinput))
    clearc()
else:
  nothing()

if act2 == 1:
  weightinput = float(input("Please enter your weight in pounds."))
  with open("weight.txt","w") as f: #in write mode
    f.write("{}".format(weightinput))
    clearc()
else:
  nothing()

#begin code comfirm
ct()
wait = input('Press enter to open Genki™')
clear = lambda: os.system('clear')
clear()

#main menu
while ("t") == ("t"):
  print("Welcome to Genki")
  print("[0] Health Menu")
  print("[1] Log Sleep & Health")
#main menu selector
  menuopt = float(input())
  clear()
  if menuopt == 0:
   yhb()
  elif menuopt == 1:
    sleepinput=float(input("How many hours of sleep did you get? "))
    sleep = (sleepinput)
    with open("sleep.txt","w") as f: #in write mode
      f.write("{}".format(sleep))
    clear = lambda: os.system('clear')
    clear()
  #calories question
    foodinput = int(input("How many calories have you consumed today?"))
    foodeaten = (foodinput)
    with open("Foodeaten.txt","w") as f: #in write mode
      f.write("{}".format(foodeaten))
    clearc()
  #time awake question
    awakeinput = int(input("How many hours have you been awake today?"))
    awaketime = (awakeinput)
    with open("awaketime.txt","w") as f: #in write mode
       f.write("{}".format(awaketime))
    clearc()
    bmi = int(wt / ht **2 * 703)
    with open("bmi.txt","w") as f: #in write mode
       f.write("{}".format(bmi))
       clearc()
       wait = input("Logging completed press enter to return to menu")
       clearc()