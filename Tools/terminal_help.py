def ginp(text):
    value = input(text)
    return value

def gint(text):
    value = int(input(text))
    return value

def gf(text):
    value = float(input(text))
    return value

def get_ABC():
    A = gint('value of A: ')
    B = gint('value of B: ')
    C = gint('value of C: ')
    return A,B,C

def get_ABCD(text1,text2,text3,text4):
    A = gint(text1)
    B = gint(text2)
    C = gint(text3)
    D = gint(text4)
    return A,B,C,D

def get_ABCD(text1,text2,text3):
    A = gint(text1)
    B = gint(text2)
    C = gint(text3)
    return A,B,C

def getf_ABC():
    A = gf('value of A: ')
    B = gf('value of B: ')
    C = gf('value of C: ')
    return A,B,C

def get_AB():
    A = gint('value of A: ')
    B = gint('value of B: ')
    return A,B

def get_AB(text1,text2):
    A = gint(text1)
    B = gint(text2)
    return A,B
