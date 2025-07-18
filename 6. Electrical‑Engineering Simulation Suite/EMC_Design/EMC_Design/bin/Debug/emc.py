

f = open("C:\\Users\\xxtra\\OneDrive\\Desktop\\kodlar\\lab\\EMC_Design\\EMC_Design\\bin\\Debug\\emc.txt", "r")
varab=f.readlines()[0].split(",")
for u in range(0,len(varab)):
    varab[u]=float(varab[u])

p,fe,nrpm,pi,it,rs,ns,s,pstator,pgap,protor =varab

#P_stator
c=3*(it**2)*rs

#P_gap
d=pi-pstator

#Ns
a=120/p*fe

#Slip
b=(a-nrpm)/a

#P_rotor
e=b*d

varab[6:] = a,b,c,d,e
otp=""
iter=0
for u in varab:
    if iter==10:
        otp+=str(u)
    else:
        otp+=str(u)+","
    iter+=1
with open("C:\\Users\\xxtra\\OneDrive\\Desktop\\kodlar\\lab\\EMC_Design\\EMC_Design\\bin\\Debug\\emc.txt", 'w') as f:
    f.write(otp)