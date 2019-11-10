import numpy as np
import pandas as pd
import matplotlib as mpl
from matplotlib import pyplot as plt
import pylab
import seaborn as sns

np.warnings.filterwarnings('ignore')
planets = pd.read_csv("planets.csv", sep=',', comment='#')
old_names = ['loc_rowid','pl_hostname','pl_name','pl_discmethod','pl_pnum','pl_orbper','pl_orbsmax','pl_bmassj','st_dist','gaia_dist','st_teff','st_mass','pl_facility','rowupdate']
new_names = ['id', 'Hostname', 'planet_name', 'discovery_method', 'No_of_planets', 'orbital_period', 'orbit_semimajor_axis', 'planet_mass', 'star_dist', 'gaia_dist',
             'star_temp', 'star_mass', 'disc_facility','date_d']
planets.rename(columns=dict(zip(old_names, new_names)), inplace=True)
df = pd.DataFrame(planets)


#print("Features = ",planets.columns[3])
df.insert(0,'new',100)
print(df[['star_mass','discovery_method','star_temp']].head(10))
print(df.loc[1],df.loc[2])
sns.set()

pylab.suptitle("Scatter plots for exoplanet features", fontsize="xx-large")
plt.axis([-0.5, 8000,-0.5, 1500])
sns.scatterplot(x="star_dist", y="orbital_period",
                     hue="discovery_method", size="planet_mass",
                     palette="dark", sizes=(10, 200),
                     data=planets)
plt.show()

pylab.suptitle("Scatter plots for exoplanet features", fontsize="xx-large")
plt.axis([-0.5, 8000,1500, 3000])
sns.scatterplot(x="star_dist", y="orbital_period",
                     hue="discovery_method", size="planet_mass",
                     palette="dark", sizes=(10, 200),
                     data=planets)
plt.show()

pylab.suptitle("Scatter plots for exoplanet features", fontsize="xx-large")
plt.axis([-0.5, 8000,3000, 8000])
sns.scatterplot(x="star_dist", y="orbital_period",
                     hue="discovery_method", size="planet_mass",
                     palette="dark", sizes=(10, 200),
                     data=planets)
plt.show()
sns.set(style="ticks")

g=sns.relplot(x="star_dist", y="star_temp", hue="No_of_planets", size="star_mass",
            sizes=(40, 400), alpha=.5, palette="BuPu_r",
            height=6, data=planets)
g.set(ylim=(0,8000))
plt.title("Star data analysis")
plt.show()
g=sns.relplot(x="star_dist", y="star_temp", hue="No_of_planets", size="star_mass",
            sizes=(40, 400), alpha=.5, palette="BuPu_r",
            height=6, data=planets)
g.set(ylim=(8000,50000))
plt.title("Star data analysis")
plt.show()
sns.set()

#plt.xlim(0,5000)
#plt.ylim(0,1000)
g=sns.lmplot(x="star_mass", y="star_temp",hue="No_of_planets",
               truncate=True, height=5, data=planets)
g.set(ylim=(0,15000))
plt.title("Regression Analysis")
plt.show()
sns.set()
plt.title("Swarm plot for categorical analysis")
plt.xticks(rotation=90)
sns.swarmplot(x='discovery_method', y='planet_mass', data=planets, hue='No_of_planets', split=True)
plt.show()
# Use more informative axis labels than are provided by default
sns.set(style="ticks")

# Initialize the figure with a logarithmic x axis
f, ax = plt.subplots(figsize=(7, 6))
ax.set_xscale("log")



sns.boxplot(x="star_mass", y="discovery_method", data=planets,
            whis="range", palette="vlag")


sns.swarmplot(x="star_mass", y="discovery_method", data=planets,
              size=2, color=".3", linewidth=0)


ax.xaxis.grid(True)
ax.set(ylabel="")
sns.despine(trim=True, left=True)
plt.show()

#ax.set_xscale("linear")
#sns.boxplot(x="No_of_planets", y="star_mass", data=planets,
 #           whis="range", palette="husl")

# Add in points to show each observation
#sns.swarmplot(x="No_of_planets", y="star_mass", data=planets,
#             size=2, color=".3", linewidth=0)

# Tweak the visual presentation
#ax.xaxis.grid(True)
#ax.set(ylabel="")
#sns.despine(trim=True, left=True)
#plt.show()





