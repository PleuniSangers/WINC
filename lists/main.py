# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line
#list lower case:https://www.kite.com/python/answers/how-to-make-the-elements-in-a-list-of-strings-lowercase-in-python
list_movies = ['Jaws','Star Wars IV','Superman','E.T.', 'Schindler\'s list', 'The river','Fahrenheit','The Seventh One','Toto XX']
won_globes = ['Jaws','Star Wars IV', 'E.T.']
toto_album = ['Fahrenheit','The Seventh One', 'Toto XX']

def alphabetical_order(x):
    order_movies = sorted(x)
    return order_movies
print(alphabetical_order(list_movies))

def won_golden_globe(movie):
    movie = movie.lower()
    for i in range (len(won_globes)):
       won_globes[i] = won_globes[i].lower()
    return movie in won_globes
print(won_golden_globe('Superman'))

def remove_toto_albums(x):
    for a in toto_album:
        if a in x:
            x.remove(a)
    return x
print(remove_toto_albums(list_movies))
print(list_movies)