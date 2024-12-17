# -*- coding: utf-8 -*-

import wis_2_2_utilities as util
import wis_2_2_systems as systems
#import random
import numpy as np

#set timestep
timestep = 2e-3

#parameters aanpassen totdat binnen 3 sec gebalanseerd is
class PID_controller():
  def __init__(self, target=0):
    self.integral1=0
    self.integral2=0
    self.K_P1= 28 #nfout in karpositie
    self.K_I1= 0          # opgetelde fout in karpositie    
    self.K_D1= 420  # snelheid van foutverandering in karpostie
    
    self.K_P2= 700 # fout in stoktoek
    self.K_I2= 0.0                   # optgetelde fout stokhoek
    self.K_D2= 150  # snelheid van foutverandering in stokhoek
    
    
  def feedBack(self, observe):
    self.integral1+=observe[0]
    self.integral2+=observe[2]
    u=self.K_P1*observe[0]+\
      self.K_I1*self.integral1+\
      self.K_D1*observe[1]+\
      self.K_P2*observe[2]+\
      self.K_I2*self.integral2+\
      self.K_D2*observe[3]
    return u
  
class pp_controller():
  def __init__(self, target=0):
    self.matrix_gain=np.array([[0, 0, 0, 0]])
    
  def feedBack(self, observe):
    u= -self.matrix_gain @ observe
    return u  
  
#class controller():
  #def __init__(self, target=0):
    pass
    
  #def feedBack(self, observe):
    u=0
    return u

class controller():
    def __init__(self, target=0):
        self.matrix_gain=np.array([[  -10.57934484,    -3.88746252, -1452.57721256,  -326.28929788]])
    def feedBack(self, observe): 
        u= -self.matrix_gain @ observe 
        return u

def main():
  model=systems.flywheel_inverted_pendulum()
  control = controller()
  simulation = util.simulation(model=model,timestep=timestep)
  simulation.setCost()
 # simulation.max_duration = 600 #seconde
  simulation.GIF_toggle = True #set to false to avoid frame and GIF creation

  while simulation.vis.Run():
      if simulation.time<simulation.max_duration:
        simulation.step()
        print(simulation.cost_input)
        u = control.feedBack(simulation.observe())
        simulation.control(u)
        simulation.log()
        #simulation.refreshTime()
      else:
        print('Ending visualisation...')
        simulation.vis.GetDevice().closeDevice()
        
  simulation.writeData()

if __name__ == "__main__":
  main()
  
