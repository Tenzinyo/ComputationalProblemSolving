import numpy as np
aggregate_shots_made=[]
for i in range(0,1000):
  shots_made=[]
  random = np.random.random()
  if (random<=.7):
    shots_made.append(1)
  else:
    shots_made.append(0)

if(sum(shots_made)>=70):
  aggregate_shots_made.append(1)
else:
  aggregate_shots_made.append(0)


print(np.average(aggregate_shots_made))
    
  
