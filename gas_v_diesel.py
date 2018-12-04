def miles_per_dollar(dpg, mpg):
	return (mpg / dpg)

def cost_efficiency(diesel_mpd, gas_mpd):
	return round(((gas_mpd - diesel_mpd) / gas_mpd) * 100)

gas_price = 2.5
diesel_price = 3.21

diesel_mpd = miles_per_dollar(diesel_price, 35)	
gas_mpd = miles_per_dollar(gas_price, 29)

diesel_efficiency = cost_efficiency(diesel_mpd, gas_mpd)
gasoline_efficiency = cost_efficiency(gas_mpd, diesel_mpd)

cost_efficiency_value = min(diesel_efficiency, gasoline_efficiency)

if (diesel_efficiency > gasoline_efficiency):
	print("Gasoline is currently " + str(cost_efficiency(diesel_mpd, gas_mpd)) + "% more cost efficient than diesel fuel.") 

	print("Diesel prices need to be at or under $" + str(((cost_efficiency_value / 100) + 1) * diesel_price) + 
      	      " for your diesel car to be more cost efficient than a $" 
              + str(gas_price) + " gallon of gasoline.")	
else:
	print("Diesel is currently " + str(cost_efficiency(gas_mpd, diesel_mpd)) + "% more cost efficient than gasoline.") 

	print("Gasoline prices need to be at or under $" + str(((cost_efficiency_value / 100) + 1) * gas_price) + 
      	      " for your gas car to be more cost efficient than a $" 
              + str(diesel_price) + " gallon of diesel.")	
	
