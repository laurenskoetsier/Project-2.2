import control as ct 
import numpy as np 

p_bar = 700
d_bar = 0.02
p_cyl = 7870
d_cyl = 0.01 
r = 0.1
l = 0.6 
m_p = p_bar*0.6*0.02*0.02
m_c = p_cyl*0.01*np.pi*0.1**2
    
g = 9.81





I = ((p_bar*(d_bar**4)*l)/12) + (p_bar*(d_bar**2)*l**3)/3
I_cyl = (np.pi*p_cyl*d_cyl*r**4)/2



matrix_A = np.array([[0,1,0,0],[0,0,((m_p*g*l/2 + m_c*g*l)/(I + m_c*l**2)),0],[0,0,0,1],[0,0,((m_p*g*l/2 + m_c*g*l)/(I + m_c*l**2)),0]])
matrix_B = np.array([[0],[1/I_cyl],[0],[-1/(I + m_c*l**2)]])

print('eigenwaardes of A are:')
print(np.linalg.eigvals(matrix_A))

list_poles = [-9.5, -10.5, -11.5, -12.5]

matrix_K = ct.place(matrix_A,matrix_B,list_poles)
print(' ')
print('Gain matrix K is:')
print(matrix_K)
print(' ')
print('eigenvalues of (A-BK) are:')
print(np.linalg.eigvals((matrix_A-matrix_B @ matrix_K)))


