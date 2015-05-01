'''
File: Gasoline_Final.py
Authors:  Jia-Ahn Pan and Kate Moody
Description:
    Prompts for the number of gallons of interest
    converts this to a float
    calculates the pounds of CO2 produced when that amount is combusted
    calculates the number of barrels of crude oil required to create the same ammount
    calcuates the cost of that gasoline.
    Prints this information.
'''

#asks the user for how many gallons of gasoline they are curious about
galgas = input('How many gallons of gasoline?  ')
gal_gas = float(galgas)

#calculates pounds of CO2 produced by gal_gas
co2_produced = 19.64*gal_gas
print("This amount of gasoline produces", co2_produced,
      "pounds of CO2.")

#caclulates the barrels of crude oil required to produce gal_gas
barrels = gal_gas/19
print("This amount of gasoline requires", barrels,
      "barrels of crude oil to produce.")

#caluclates the cost of gal_gas in the US
avg_cost = 2.598*gal_gas
print("This amount of gasoline costs", avg_cost, "dollars.")