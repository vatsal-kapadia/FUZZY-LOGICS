import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt 
x_qual = np.arange(0, 120, 1) 
x_serv = np.arange(0, 120, 1) 
x_tip = np.arange(0, 100, 1) 
# Generate fuzzy membership functions 
qual_lo = fuzz.trimf(x_qual, [0, 30, 50]) 
qual_md = fuzz.trimf(x_qual, [40, 60, 80]) 
qual_hi = fuzz.trimf(x_qual, [70, 90, 120]) 
serv_lo = fuzz.trimf(x_serv, [0, 20, 55])
serv_md = fuzz.trimf(x_serv, [40, 68, 90]) 
serv_hi = fuzz.trimf(x_serv, [65, 100, 120]) 
tip_lo = fuzz.trimf(x_tip, [0, 25, 50]) 
tip_md = fuzz.trimf(x_tip, [30, 50, 75]) 
tip_hi = fuzz.trimf(x_tip, [60, 80, 100]) 

# Visualize these universes and membership functions 
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9)) 
ax0.plot(x_qual, qual_lo, 'b', linewidth=1.5, label='cold') 
ax0.plot(x_qual, qual_md, 'g', linewidth=1.5, label='warm') 
ax0.plot(x_qual, qual_hi, 'r', linewidth=1.5, label='hot') 
ax0.set_title('TEMP') 
ax0.legend() 
ax1.plot(x_serv, serv_lo, 'b', linewidth=1.5, label='Poor') 
ax1.plot(x_serv, serv_md, 'g', linewidth=1.5, label='Acceptable') 
ax1.plot(x_serv, serv_hi, 'r', linewidth=1.5, label='Amazing') 
ax1.set_title('Weather') 
ax1.legend() 
ax2.plot(x_tip, tip_lo, 'b', linewidth=1.5, label='SLOW') 
ax2.plot(x_tip, tip_md, 'g', linewidth=1.5, label='MODERATE') 
ax2.plot(x_tip, tip_hi, 'r', linewidth=1.5, label='FAST') 
ax2.set_title('Speed') 
ax2.legend() 
# Turn off top/right axes 
for ax in (ax0, ax1, ax2): 
 ax.spines['top'].set_visible(False) 
 ax.spines['right'].set_visible(False) 
 ax.get_xaxis().tick_bottom() 
 ax.get_yaxis().tick_left() 

