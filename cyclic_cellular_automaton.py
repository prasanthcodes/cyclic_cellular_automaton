import numpy as np
import matplotlib.pyplot as plt
import time

width=100
height=100
n_states=15
n_iteration=500
S1=np.random.random(width*height)*n_states
S2=np.random.random(width*height)*n_states
S1=S1.astype(np.uint8)
S2=S2.astype(np.uint8)
# plt.figure()
# plt.imshow(np.reshape(S2,[height,width]))
plt.ion()
fig1, ax1 = plt.subplots()
axim1=ax1.imshow(np.reshape(S2,[height,width]))
for n_frame in range(n_iteration):
    for i in range(height):
        for j in range(width):
            cur=S1[i*width+j]
            target=(cur+1)%n_states
            next=cur
            for k in range(-1,2,1):
                for l in range(-1,2,1):
                    if ((k==0)&(l==0)):
                        continue
                    pos=(i+k)*width+(j+l)
                    if ((pos)>0)&(pos<width*height):
                        if S1[pos]==target:
                            next=target
            S2[i*width+j]=next
    tmp=S1
    S1=S2
    S2=tmp
    IM=np.reshape(S2,[height,width])
    axim1.set_data(IM)
    fig1.canvas.flush_events()
    time.sleep(0.0001)
