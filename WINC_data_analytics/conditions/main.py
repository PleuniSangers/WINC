# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line

def farm_action(Weather, Time_of_day, Cow_milking_status, Locations_of_the_cows, Season, Slurry_tank, Grass_status):
    if Locations_of_the_cows == 'pasture' and (Weather == 'rainy' or Time_of_day == 'night'):
        return 'take cows to cowshed'
    elif Cow_milking_status == True:
        if Locations_of_the_cows == 'cowshed' :
            return 'milk cows'
        else: 
            return """take cows to cowshed 
milk cows 
take cows back to pasture"""
    elif Slurry_tank == True: 
        if Locations_of_the_cows == 'cowshed' and (Weather == 'rainy' or 'neutral'):
            return'fertilize pasture'
        if Locations_of_the_cows == 'pasture':
            return 'take cows to pasture \n fertilize pasture'
    elif Grass_status == True and Season =='spring' and Weather == 'sunny':
        if Locations_of_the_cows == 'cowshed':
            return 'mow grass'
        else:
            return 'take cows to cowshed \n mow grass'
        
    else:
        return 'wait'
print(farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True))
print(farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True))
print(farm_action('windy', 'night', True, 'cowshed', 'winter', True, True))
print(farm_action('sunny', 'day', True, 'pasture', 'spring', False, True))


