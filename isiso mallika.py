def isIso(x,y):
    if len(x) !=len(y):
        return false
    for i in range(len(x)):
        count=0
        if x.count(x[i]) != y.count(y[i]):
           return False
    return True
print(isIso("fool","poor"))
print(isIso("too","bar"))
print(isIso("faol","poor"))
print(isIso("toto","yaya"))
