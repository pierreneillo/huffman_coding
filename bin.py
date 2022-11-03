#Tracé grâce à la méthode d'Euler de la solution de l'équation différentielle
from matplotlib.pyplot import *
from numpy import *

#On tracera la courbe avec 1 ms comme unité de temps
E = 5
tau = 1 #tau vaut donc 1

def f(t,yt):
    return (E-yt)/tau#Relation donnée par l'équation différentielle

for nbIntervalles in [5,10,15,20]:
    Tf = 5# On choisit 5 comme tf (99.3% de charge)
    pas = Tf/nbIntervalles

    Texp = linspace(0,Tf,nbIntervalles+1)
    Y = [0] #Le premier élément vaut 0 car le condensateur est déchargé au début

    for i in range(1,nbIntervalles+1):
        Y.append(Y[-1]+pas*f(pas*i,Y[-1]))

    plot(Texp,Y,'blue')



    #Courbe "exacte"
    T = linspace(0,Tf,101)
    U = E*(1-exp(-T/tau))
    plot(T,U,'red')
    xlabel("Temps (ms)")
    ylabel("Tension au bornes de C (V)")
    title("Méthode d'Euler avec %d portions"%nbIntervalles)
    show()

    savefig("euler"+str(nbIntervalles)+".png",
    dpi='figure',
    facecolor='w',
    edgecolor='w',
    orientation='portrait',
    format=None,
    transparent=False,
    pad_inches=0.1)
    clf()
    
    
    
