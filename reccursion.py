student = {'name': 'Tom',
        'age': None,
        'subject': {001: 'php',
                    002: None },
        'marks': {'theory': {'java' : 67, 'c++' : 49, 'html' : None}}
           }
def reccursion(r):
    for k,v in r.items():
        if isinstance(v,dict):
            reccursion(v)
        elif v==None:
            del r[k]
    return r

value = reccursion(student)
print value

