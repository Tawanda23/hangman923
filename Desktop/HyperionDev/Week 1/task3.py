        #*** Defining Awards ***

#Provincial Colours =< 100
#Provincial Half Colours = 100 and less than or equal to  105
#Provincial Scroll = greater than 105 but equal or less than 110)
#No Aaward =  greater than 110

#User inputs the time taken during swimming
print("Swimming:")
swimming = input("Enter time taken to finish in minutes: ")
print("You completed swimming in: ", swimming , "minutes")

#User inputs the time taken during swimming
print("Cycling")
cycling = input("Enter time taken to finish in minutes: ")
print("You completed cycling in: ", cycling , "minutes")

#User inputs the time taken during swimming
print("Running")
running = input("Enter time taken to finish in minutes: ")
print("You completed running in: ", running , "minutes")

#Calculate the total time taken to do the triathalon
total = int(swimming) + int(cycling) + int(running)
print("You have completed the Triathalon in: ", total , "minutes")

#Conditions to find if the user will be getting an award
if total <= 100:
    print("Award: Provincial Colours")

#Provincal Half colours 
elif total >100 and total <= 105:
    print("Award: Provincial Half Colours")

#Provincial Scroll 
elif total >105 and total <110:
    print("Award: Provincial Scroll")

#No Award given
else: print("No Award")