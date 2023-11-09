my_name = 'Adnan Shah (That is me, hi)'
my_age = 18
my_height = 5.9 # feet
my_weight = 84 # kg
my_eyes = 'Brown, or Black, Blackish Brown (I dunno)'
my_teeth = 'White, I think'
my_hair = 'Black and White'

def variables(my_name, my_age, my_height, my_weight, my_eyes, my_hair, my_teeth):
    return (f"""Let's talk about {my_name}.\nHe's {my_age} and a half.
He's {my_height} feet tall.
He's {my_weight} kg... do some cardio.\nHe's got {my_eyes} eyes with {my_hair} hair.
His teeth are {my_teeth}.""")

print(variables(my_name, my_age, my_height, my_weight, my_eyes, my_hair, my_teeth))
