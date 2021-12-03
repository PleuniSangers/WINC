# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorer1 = 'Ruud Gullit'
scorer2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = scorer1 + ' ' + str(goal_0) + ','+ ' '+ scorer2 + ' '+ str(goal_1)
report = f'{scorer1} scored in the {goal_0}nd minute\n{scorer2} scored in the {goal_1}th minute'
player = 'Jan Wouters'
first_name = player[:3]
last_name_len = len(player[4:])
name_short = first_name[0:1] + '. ' + player[4:11]
chant = (f'{first_name}! ') * len(first_name)
chant = chant[:-1]
good_chant = (chant !=' ')
print(scorers)
print(first_name)
print(last_name_len)
print(name_short)
print(chant)