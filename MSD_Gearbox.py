import itertools
import numpy as np
from pandas import array

def factorial(z):
    given = z
    factors = []
    i = 2
    while i<= z+1:
        # if i ==1:
        #     continue
        if z % i == 0:
            factors.append(i)
            z= z/i
            continue
        i += 1

    fac = dict()
    for i in factors:
        fac[i] = fac.get(i, 0) +1
    ans = ""
    for k,v in fac.items():
        ans += f"{k}^{v} "

    return f"factors of {given} = {ans}", fac, factors

z = 12
print(factorial(z)[0],end="\n\n")

# P1(x1)P2(x2)P3(x3)....Pn(xn)
facts_dict = factorial(z)[1]
fact_lst = factorial(z)[2]

n = 0
for i in facts_dict:
    n += facts_dict[i]


res = list(itertools.permutations(fact_lst))

# res = []
# [res.append(x) for x in test_list if x not in res]
# # print(res)
st_formula = []
X= []

for i in res:
    x1 = 1
    if len(i)==2:
        x2 = i[0]
        X.append(list(itertools.permutations([x1,x2])))
    elif len(i)==3:
        x2 = i[0]
        x3 = i[0]*i[1]
        X.append(list(itertools.permutations([x1,x2,x3])))
    elif len(i)==4:
        x2 = i[0]
        x3 = i[0]*i[1]
        x4 = i[0]*i[1]*i[2]
        X.append(list(itertools.permutations([x1,x2,x3,x4])))
    else:
        print("Too much data to handle")
    
    for p,xs in zip(i,X):
        for x in xs:
            st_formula.append(" ".join(f"{p}({ele})" for ele in x))
    X.clear()


print("Total Structural Formulae are: ")
for i in range(len(st_formula)):
    print(f"{i+1})-> ", st_formula[i])



unique = []
[unique.append(x) for x in st_formula if x not in unique]

print('\n')
print("Total UNIQUE Structural Formulae are: ")
for i in range(len(unique)):
    print(f"{i+1})-> ", unique[i])
