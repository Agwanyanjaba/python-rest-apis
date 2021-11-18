altitude = 10000
speed = 250
propulsion = "Propeller"

print(altitude<1000)
print(speed>100)
print(altitude < 1000 and speed > 100) #Fand T  = F
print((propulsion == "Jet" or propulsion == "Turboprop") and speed < 300 and altitude > 20000) # F & T = F
print((altitude > 500 and speed > 100) or not propulsion == "Propeller") #F || T  = T
print(not (speed > 400 and propulsion == "Propeller")) #F & T = F but ! = T