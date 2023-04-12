import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
mtcars = pd.read_csv('c:/Users/student/Documents/mtcars.csv')

colors1 =['darkturquoise','deepskyblue','dodgerblue']
mtcars.groupby(['cyl']).mpg.mean().plot.bar(stacked=True, ylabel='potrosnja',xlabel='cilindri',color=colors1,rot=0)
plt.show()
boxplot = mtcars.boxplot(by='cyl',column=['wt'])
plt.show()
colors2=['gold','orangered']
mtcars.groupby(['am']).mpg.mean().plot.bar(stacked=True, ylabel='potrosnja',xlabel='cilindri',color=colors2,rot=0)
plt.show()


automatic = mtcars[mtcars.am == 0]
manual = mtcars[mtcars.am == 1]
a = automatic[['hp','qsec']].to_numpy()
m = manual[['hp','qsec']].to_numpy()

fig = plt.figure()
ax2 = fig.add_axes([0.1,0.1,0.8,0.8])
axa_hp = ax2.scatter(a[:,1],a[:,0], color = 'blue')
axm_hp = ax2.scatter(m[:,1],m[:,0], color = 'green')
ax2.legend(labels = ['Automatski','Rucni'])
ax2.set_title("Ubrzanje s obzirom na konjsku snagu")

plt.show()


