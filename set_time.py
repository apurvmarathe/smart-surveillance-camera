import time
wait = 300
elapsed=0
start_hour= 16
start_min= 0
end_hour= 19
end_min= 40
def check_time():
 global wait,elapsed,current,start_hour,start_min
 current=time.localtime()
 hour=current.tm_hour
 if(hour==0):
   start_hour=0
   start_min=0
 min=current.tm_min
 if((time.time()-elapsed)>=wait)and(hour>=start_hour and min>start_min):
   if(hour==end_hour and min>=end_min): 
      return False
   else:
      elapsed=time.time()
      return True
 else:
   return False
