"""
Práctica: Modelado y control del sistema cardiovascular mediante el modelo Windkessel

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Javier Vazquez Gomez
Número de control: 23212242
Correo institucional: l23212242@tectijuana.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx

"""
import numpy as np
import math as m
import control as ctrl
import matplotlib.pyplot as plt
from scipy import signal
from pathlib import Path
import pandas as pd

# Datos generales de la simulación
u = np.array(pd.read_excel(r'C:\Users\Admin\Pictures\Paul\PAUL GITHUB 3\signal.xlsx', header=None))
u = np.reshape(u,-1)
x0,t0,tend,dt,w,h = 0,0,15,1E-3,10,5
N = round((tend-t0)/dt) + 1
t = np.linspace(t0,tend,N)
u = np.interp(t,np.linspace(t0,tend,len(u)),u)
signals = ["Normotenso","Hipotenso","Hipertenso",]
# Componentes del circuito RLC
def sis(C, nombre):
    R, L, Z = 1,0.001,0.01
    num = [L*R, R*Z]
    den = [L*R*C*Z,L*(Z+R),R*Z]
    sys = ctrl.tf(num, den)
    print(f"Función de transferencia {nombre}: {sys}\n")
    # Polos del sistema    
    L = np.roots(den)
    print(f"Polos del sistema: {L[0]:.3e}, {L[1]:.3e}\n")
    return sys

sysN = sis(1.5, "Normotenso")
sysL = sis(3.5, "Hipotenso")
sysH = sis(1.0, "Hipertenso")

def PID(sys,kP,kI,kD,nombrePID):
    Cr = 1E-6
    Re = 1/(Cr*kI)
    Rr = kP*Re
    Ce = kD/Rr
    numPID = [Re*Rr*Ce*Cr,Re*Ce+Rr*Cr,1]
    denPID = [Re*Cr,0]
    PID = ctrl.tf(numPID,denPID)
    print(f"Función de transferencia del controlador {nombrePID}: {PID}\n")
    # Sistema de control en lazo cerrado     
    sysPID = ctrl.feedback(ctrl.series(PID,sys),1,sign = -1)
    print(f"Función de transferencia en lazo cerrado {nombrePID}: {sysPID}\n")
    return sysPID

sysPIDL = PID(sysL,464.5531,1141740.5289,0.0062681,"Hipotenso")
sysPIDH = PID(sysH,130.974,317572.5368,0.0017466,"Hipertenso")

#Colores 
clr1 = np.array([(0, 53, 58)])/255
clr2 = np.array([(138, 43, 226)])/255
clr3 = np.array([(0, 206, 209)])/255

# Funciones del sistema en lazo abierto y lazo cerrado
def openloop(t,ft,u):
  _,La = ctrl.forced_response(ft,t,u,x0)
  return La
def closedloop(t,ftPID,PpN):
  _,Lc = ctrl.forced_response(ftPID,t,PpN,x0)
  return Lc

#Respuestas: Simulaciones numéricas
for i in range(0,3):
    PpN = openloop(t,sysN,u)
    PpL = openloop(t,sysL,PpN)
    PpH = openloop(t,sysH,PpN)
    PIDL = closedloop(t,sysPIDL,PpN)
    PIDH = closedloop(t,sysPIDH,PpN)
    fg = plt.figure(i+1)
    fg.set_size_inches(w,h)
    plt.rcParams['font.size'] = 11
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = ['Times New Roman']
    plt.plot(t,PpN,'-',linewidth=1.5,color=clr1,label='PpN(t):Normotenso')
    if i == 0:
        plt.plot(t,PpL,'--',linewidth=1.5,color=clr2,label='PpL(t):Hipotenso')
        plt.plot(t,PpH,':',linewidth=1.5,color=clr3,label='PpH(t):Hipertenso')
    elif i == 1:
        plt.plot(t,PpL,':',linewidth=1.5,color=clr2,label='PpL(t):Hipotenso')
        plt.plot(t,PIDL,'--',linewidth=1.5,color=clr3,label='PIDL(t):Hipotenso')
    elif i == 2:
        plt.plot(t,PpH,':',linewidth=1.5,color=clr2,label='PpH(t):Hipertenso')
        plt.plot(t,PIDH,'--',linewidth=1.5,color=clr3,label='PIDH(t):Hipertenso')    
    plt.xlim(-0.2,15.1); plt.xticks(np.arange(0,16,1))
    plt.ylim(-0.8,1.6); plt.yticks(np.arange(-0.6,1.6,0.2))
    plt.xlabel('t [s]')
    plt.ylabel('V(t) [V]')
    plt.legend(bbox_to_anchor=(0.5,-0.25),loc='center',ncol=3,frameon=False)
    plt.show()
    fg.savefig(Path(__file__).resolve().parent / (signals[i]+'_python2.pdf'),bbox_inches='tight')
    plt.show()