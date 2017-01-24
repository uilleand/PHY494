# Heaviside step function
def heaviside(x):
   """Heaviside step function"""

   theta = None
   if x < 0:
      theta = 0.
   elif x == 0:
      theta = 0.5
   else:
      theta = 1.

   return theta

xlist = []

h = 0.5
xmin, xmax = -4, 4
x = xmin
while x <= xmax:
    xlist.append(x)
    x + h
    print(xlist)
    theta = heaviside(x)

print("Theta(" + str(x) + ") = " + str(theta))
