__winc_id__ = '25a8041d2d5e4e3ab61ab1be43bfb863'
__human_name__ = 'dictionaries'

#excersize 1

from os import name


def create_passport(name,date_of_birth,place_of_birth,height, nationality):
    passport = {
        'name' : name,
        'date_of_birth' : date_of_birth,
        'place_of_birth' : place_of_birth,
        'height' : height,
        'nationality': nationality}
    return passport 
create_passport('Mara test', '1993-01-01','Rotterdam', 1.75, 'Netherlands')

#excersize 2

def add_stamp(passport, country):
   if 'stamps' not in passport:
       if country not in passport.values():
            passport['stamps'] = [country]
            return passport
   elif country not in passport['stamps']:
    passport['stamps'].append(country)
    return passport
   return passport
print(add_stamp(create_passport('Mara Test', '1993-01-01','Rotterdam', 1.75, 'Netherlands'),'Belgium'))
print(add_stamp(create_passport('Mara Test', '1993-01-01','Rotterdam', 1.75, 'Netherlands'),'Netherlands'))

#excersize 3
def check_passport(passport,country,allowed, not_allowed):
    if country in allowed:
        if passport['nationality'] not in not_allowed:
            add_stamp(passport,country)
            return passport
        return False
    elif country not in allowed:
        return False
    elif passport['nationality'] in not_allowed:
        return False
  
check_passport(create_passport('Mara Test', '1993-01-01','Rotterdam', 1.75, 'Netherlands'),'Belgium',['Belgium', 'France'],['UK', 'Spain'])
print(check_passport(create_passport('Mara Test', '1993-01-01','Rotterdam', 1.75, 'Netherlands'),'UK',['Belgium', 'France'],['UK', 'Spain']))