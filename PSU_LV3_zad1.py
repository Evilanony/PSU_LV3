import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
mtcars = pd.read_csv('c:/Users/student/Documents/mtcars.csv')

#prvi
print("\n",mtcars.sort_values('mpg', ascending=True).tail(5))
print("\n--------------------------------------------------")
#drugi
print("\n",mtcars[mtcars.cyl == 8].sort_values('cyl', ascending=True).head(3))
print("\n--------------------------------------------------")
#treci
cyl_cars = mtcars[mtcars.cyl == 6]
print("\n",cyl_cars['mpg'].mean())
print("\n--------------------------------------------------")
#cetvrti
mass_cars=mtcars[(mtcars.wt>=2) & (mtcars.wt<=2.2) & (mtcars.cyl==4)]
print("\n",mass_cars['mpg'].mean())
print("\n--------------------------------------------------")
#peti
automatic_cars=mtcars[mtcars.am==1]
print("\n",automatic_cars['am'].count())
print("\n--------------------------------------------------")
nonautomatic_cars=mtcars[mtcars.am==0]
print("\n",nonautomatic_cars['am'].count())
print("\n--------------------------------------------------")
#sesti
automatic_cars_hp=mtcars[(mtcars.am==1) & (mtcars.hp>100)]
print("\n",automatic_cars_hp['hp'].count())
print("\n--------------------------------------------------")
#sedmi
mtcars['kg'] = mtcars.wt * 1000 * 0.45359237
print("\n",mtcars.kg)
print("\n--------------------------------------------------")
print(mtcars)

