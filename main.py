from sympy import *
def absdf(df):
    return sqrt((df[0]**2)+df[1]**2)
x1=symbols('x1')
x2=symbols('x2')
print("Function:")
f=eval(input())
print("X01:")
x01=input()
print("X02:")
x02=input()
Xk=Matrix([[x01],[x02]])
print("eps:")
eps=float(input())
t=0.001
df=Matrix([[diff(f,x1)],[diff(f,x2)]])
dfsubs=df.subs([(x1,Xk[0]),(x2,Xk[1])])
df=Matrix([[diff(f,x1)],[diff(f,x2)]])
while absdf(dfsubs)>eps:
    Xk=Xk-t*df.subs([(x1,Xk[0]),(x2,Xk[1])])
    dfsubs = df.subs([(x1, Xk[0]), (x2, Xk[1])])


print("xmin=",round(float(Xk[0]),2),round(float(Xk[1]),2))

