# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 10:05:14 2019

@author: yannael
"""

import matplotlib.pyplot as plt



#Cylindre y #Cylindre x/z #Cylindre_Creux y
#Clindre_Creux x/z  #Double_Cone y #Double_Cone x/z
C_cy=[0.42,0.80,0.83,0.84,0.91,0.94,0.98]

C_ba=[0.54,1.21,1.83,1.92,2.11,2.49,2.52]


V_cy=[813,1221,1467,1515,1598,1632,1686]

V_ba=[274,1100,1251,1375,1451,1557,1566]

ms=[1.6,1.65,1.7,1.75,1.8,1.85,1.9]



plt.figure(1)
plt.plot(ms,C_cy,'-r',linewidth=1.5,label="Cylindre")
plt.plot(ms,C_ba,'-b',linewidth=1.5,label="Barre")
plt.xlabel('signal en ms')
plt.ylabel('Consommation en A')
plt.title("Comparaison consommation 2 pièces ( Inertie et poids égaux )")
#plt.axis([1.6,1.9,0,3])
plt.grid(True)
plt.legend()
plt.show


plt.figure(2)
plt.plot(ms,V_cy,'-r',linewidth=1.5,label="Cylindre")
plt.plot(ms,V_ba,'-b',linewidth=1.5,label="Barre")
plt.xlabel('signal en ms')
plt.ylabel('vitesse de rotation en tr/min')
plt.title("Comparaison vitesse 2 pièces ( Inertie et poids égaux )")
#plt.axis([,5,-20,20])
plt.grid(True)
plt.legend()
plt.show

plt.figure(3)
plt.plot(C_cy,V_cy,'-r',linewidth=1.5,label="Cylindre")
plt.plot(C_ba,V_ba,'-b',linewidth=1.5,label="Barre")
plt.xlabel('Consommation en A')
plt.ylabel('vitesse de rotation en tr/min')
plt.title("Comparaison consommation/vitesse 2 pièces ( Inertie et poids égaux )")
#plt.axis([,5,-20,20])
plt.grid(True)
plt.legend()
plt.show
