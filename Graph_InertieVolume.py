# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 16:33:25 2019

@author: yannael
"""

import matplotlib.pyplot as plt
import numpy as np


#0_Cylindre y #1_Cylindre x/z 
#2_Cylindre_Creux y #3_Clindre_Creux x/z 
#4_Double_Cone y #5_Double_Cone x/z
#6_Toupie y  #7_Toupie x/z
#8_cube
#9_double_Pyramide y  #10_double pyramide x/z
#11_sablier y  #12_sablier x/z
#13_altère x   #14_altère y/z
#15_cylindre feuille  y    #16_cylindre feuille  x/z
#17_feuille cylindre  y    #18_feuille cylindre x/z
#19_croix + y     #20_croix + x/z
#21_croix x y     #22_croix x x/z
#23_croix creuse y  #24_croix creuse x/z
#25_sphère
#26_sphère creuse
#27_sphère feuille
#28_ballon rugby pointu  y
#29_beigner  y   #30_beigner  x/z
#31_beigner plat  y  #32_beigner plat  x/z
#33_croix 3D 
#34_Etoile
#35_Etoile noyau
#36_double bole  y   #37_double bole  x/z
#38_double assiette  y #39_double assiette x/z
#40_beigner plein  y  #41_beigner plein  x/z
#42_volant continu y #43_volant continu x/z
#44_volant discontinu y #45_volant discontinu x/z
#46_volant_isocontraint y #47_volant_isocontraint x/z

liste=['Cylindre y','Cylindre x/z','Cylindre_Creux y','Clindre_Creux x/z','Double_Cone y','Double_Cone x/z','Toupie y','Toupie x/z','cube','double_Pyramide y','double pyramide x/z',
       'sablier y','sablier x/z','altère x','altère y/z','cylindre feuille y','cylindre feuille x/z','feuille cylindre  y','feuille cylindre x/z','croix + y','croix + x/z','croix x y','croix x x/z','croix creuse y',
       'croix creuse x/z','sphère','sphère creuse','sphère feuille','ballon rugby pointu  y','beigner  y','beigner  x/z','beigner plat y','beigner plat x/z','croix 3D','Etoile','Etoile noyau','double bole y',
       'double bole  x/z','double assiette y','double assiette x/z','beigner plein y','beigner plein x/z','volant continu y','volant continu x/z','volant discontinu y','volant discontinu x/z','volant_isocontraint y','volant_isocontraint x/z']

#V=[785,785,784,784,787,787,785,785,785,784,784,780,780,785,785,787,787,786,786,788,788,786,786,788,788,786,790,786,792,790,790,788,788,783,787,789,789,789,790,790,788,788,787,787,790,790]
#V=(46)*[785]
V=np.zeros(48)
for i in range(0,48,3):
    V[i]=784
    V[i+1]=785
    V[i+2]=786

#V[45]=785  
#print(V)  
#print('taille:',len(V))

V_B=[785,1571,1287,2071,787,2730,785,3591,1235,1233,1848,785,2323,785,4047,3928,5857233,786161,4194952,2906,10701,1491,17157,4650,7464,786,2386,180365,792,790,7238,788,8300,2702,2180,1402,789,4189,790,12482,788,6581,1232,6657,1571,8083,785,11742]

I=[76.58,89.34,174.19,138.07,138.25,84.46,181,117,87.09,108.2,81.5,66.1,267.44,64.03,805.22,69067,34533,61307,30973,1361,686,1117,561,1794,898,80,250,5016,61,634,323,652,329,354,333,178,360,185,817,410,488,247,600,309,678,349,308,157]

#print('taille liste:',len(liste))
#print('taille V:',len(V))
#print('taille V_B:',len(V_B))
#print('taille I:',len(I))

v1,v2,i1,i2=770,788,1000,1000000
x2=[v1,v2,v2,v1,v1]
y2=[i1,i1,i2,i2,i1]

plt.figure(2)
plt.scatter(V,I,marker = 'o')
plt.plot(x2,y2,'red')
plt.xlabel('Volume mm3')
plt.ylabel('Inertie g.mm²')
plt.title("Graphique 1")
plt.yscale('log')
plt.axis([780,790,10,100000])
plt.grid(True)
#plt.legend()
#plt.show

vb1,vb2,ib1,ib2=700,20000,170,7000
x1=[vb1,vb2,vb2,vb1,vb1]
y1=[ib1,ib1,ib2,ib2,ib1]


plt.figure(1)
plt.scatter(V_B,I,marker = 'o')
plt.plot(x1,y1,'red')

plt.yscale('log')
plt.xscale('log')
plt.xlabel('Volume Balayé mm3')
plt.ylabel('Inertie g.mm²')
plt.title("Graphique 2")
#plt.axis([-5,5,-20,20])
plt.grid(True)
plt.legend()
plt.show

def recherche_zoneVB(VB,I,L,v1,v2,i1,i2):
    N=len(VB)
    Mem=[]
    for i in range(0,N):
        if  v1<=VB[i]<=v2 and i1<=I[i]<=i2:
            Mem.append(L[i])
    n=len(Mem)
    return Mem,n
            
def recherche_zoneV(V,I,L,v1,v2,i1,i2):
    N=len(V)
    Mem=[]
    for i in range(0,N):
        if  v1<=V[i]<=v2 and i1<=I[i]<=i2:
            Mem.append(L[i])
    n=len(Mem)
    return Mem,n

y1,n1=recherche_zoneVB(V_B,I,liste,vb1,vb2,ib1,ib2)
print('il y a',n1,'volants dans la zone recherchée(volume balayé):::',y1)

y2,n2=recherche_zoneV(V,I,liste,v1,v2,i1,i2)
#print('il y a',n2,'volants dans la zone recherchée(volume instantané):::',y2)
