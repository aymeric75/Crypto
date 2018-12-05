


 
def pgcd_rec(a,b):
    """pgcd(a,b): calcul du 'Plus Grand Commun Diviseur' entre les 2 nombres entiers a et b"""
    if b==0:
        return a
    else:
        r=a%b
        return pgcd_rec(b,r)


 
def pgcd(a,b):
    """pgcd(a,b): calcul du 'Plus Grand Commun Diviseur' entre les 2 nombres entiers a et b"""
    while b!=0:
        r=a%b
        a,b=b,r
    return a
 


def pgcdn(*n):
    """Calcul du 'Plus Grand Commun Diviseur' de n valeurs entières (Euclide)"""
    p = pgcd(n[0], n[1])
    for x in n[2:]:
        p = pgcd(p, x)
    return p


def pgcde(a, b):
    """ pgcd étendu avec les 2 coefficients de bézout u et v
        Entrée : a, b entiers
        Sorties : r = pgcd(a,b) et u, v entiers tels que a*u + b*v = r
    """
    r, u, v = a, 1, 0
    rp, up, vp = b, 0, 1
    while rp != 0:
        q = r//rp
        rs, us, vs = r, u, v
        r, u, v = rp, up, vp
        rp, up, vp = (rs - q*rp), (us - q*up), (vs - q*vp)
    return (r, u, v)

def ppcm(a,b):
    """ppcm(a,b): calcul du 'Plus Petit Commun Multiple' entre 2 nombres entiers a et b"""
    if (a==0) or (b==0):
        return 0
    else:
        return (a*b)//pgcd(a,b)



def ppcm(*n):
    """Calcul du 'Plus Petit Commun Multiple' de n (>=2) valeurs entières (Euclide)"""
    def _pgcd(a,b):
        while b: a, b = b, a%b
        return a
    p = abs(n[0]*n[1])//_pgcd(n[0], n[1])
    for x in n[2:]:
        p = abs(p*x)//_pgcd(p, x)
    return p


if __name__ == "__main__":

    print(pgcdn(2,3,4))