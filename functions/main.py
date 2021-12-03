# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line
def greet(x):
    name=x
    sentence= f'Hello, {name}!'
    return sentence

begroeting=greet('Pleuni')
print(begroeting)
def add(a,b,c):
    som= a+b+c
    return som
totaal= add(7,4,2)
print(totaal)

def positive(h):
    pos= h>0
    return pos
waar= positive(10)
print(waar)

def negative(g):
    neg= g<0
    return neg
niet_waar= negative(10)
print(niet_waar)