import math

x1, y1, z1=map(float,input('Первая точка плоскости: ').split())
x2, y2, z2=map(float,input('Вторая точка плоскости: ').split())
x3, y3, z3=map(float,input('Третья точка плоскости: ').split())
x4, y4, z4=map(float,input('Точка, до которой ищем расстояние: ').split())

d=x2-x1
f=x3-x1
g=y2-y1
k=y3-y1
l=z2-z1
m=z3-z1
a=g*m-(k*l)
b=(d*m-(l*f))*(-1)
c=(d*k-(f*g))
D=(a*x1*(-1))+(b*(y1*(-1)))+(c*(z1*(-1)))

H=math.fabs(a*x4+b*y4+c*z4+D)/(((a**2)+(b**2)+(c**2))**(1/2))

print('Расстояние от точки до плоскости: ', H)
