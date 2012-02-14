# -*- coding:utf-8 -*-
'''
计算波速
Created on 2012-2-14

@author: WLQ
'''

import numpy as np

class Wave(object):
    def __init__(self,rho=0,E=0,v=0):
        self.E=E
        self.v=v
        self.lambd=v*E/(1+v)/(1-2*v)
        self.G=E/2/(1+v)
        self.rho=rho
        
    def __repr__(self):
        return '''E = %6.2f, v = %6.2f, lambda = %6.2f
G = %6.2f, Rho = %6.2f, P/R = %6.2f
V_s = %6.2f, V_p = %6.2f, V_r = %6.2f'''%(self.E,self.v,self.lambd,self.G,self.rho,self.PRRatio(),self.ShearWave(),
self.DilatationalWave(),self.RayleighWave())
        
    def setLame(self,lambd=0,G=0):
        self.lambd=lambd
        self.G=self.G
        self.E=self.G*(3*self.lambd+2*self.G)/(self.G+self.lambd)
        self.v=self.lambd/(self.lambd+self.G)/2
    
    def setEv(self,E=0,v=0):
        self.E=E
        self.v=v
        self.lambd=v*E/(1+v)/(1-2*v)
        self.G=E/2/(1+v)
        
    def setRho(self,rho=0):
        self.rho=rho
        
    def ShearWave(self):
        return np.sqrt(self.G/self.rho)
    
    def DilatationalWave(self):
        return np.sqrt((self.lambd+2*self.G)/self.rho)
        
    def RayleighWave(self):
        return (self.v*1.12+0.87)/(1+self.v)*self.ShearWave()
    
    def PRRatio(self):
        return  np.sqrt(2*(1-self.v)/(1-2*self.v)) 
          

            
        