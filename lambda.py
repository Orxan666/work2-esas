physics={
    'F': lambda m,a: m*a,
    'a': lambda v1,v2, t1, t2: (v2-v1)/(t2-t1),
    'Rz': lambda *args: sum(args) ,
    'S': lambda a,t: a*t**2/2,
    'Ep': lambda m,g,h: m*g*h,
    'v': lambda s1,s2, t1,t2: (s2-s1)/(t2-t1),
    'W': lambda F,s: F*s,
    'T': lambda f: 1/f,
    'Ek': lambda m,v: m*v**2/2,
    'p': lambda F,s: F/s,
    'Vsr': lambda s,t: s/t,
    'Ew': lambda W,Q: W+Q,
    'ro': lambda m,v: m/v,
    'U': lambda W,q: W/q,
    'I': lambda q,t: q/t,
    'W2': lambda U,I,t: U*I*t

}
print(physics.get('F')(5,4))





















# def test(a,b):
#     c=a+b
#     return c

# print(test(2,3))


# def increment(*args):
#     return sum(args)


# print(increment(2,3,4))


# age=int(input("Yasinizi daxil edin: "))

# result=lambda x: print("Siz siqaret ala bilersiniz") if x>18  else print("Ala bilmersiniz") 

# result(age)