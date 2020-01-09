from boltiot import Bolt
import config,json,time
mybolt=Bolt(config.api,config.id)
passed = 0
def update_ir_value():
  global threshold
  response = mybolt.digitalWrite('1','LOW')
  response = mybolt.analogRead('A0')
  data = json.loads(response)
  threshold = int(data['value'])
  threshold += 30
  print(threshold)
def check_ir_status() :
 global passed
 if(time.time()-passed > 60):
  passed = time.time()
  response=mybolt.analogRead('A0')
  data = json.loads(response)
  value = int(data['value'])
  print(value)
  if (value > threshold) :
   response = mybolt.digitalWrite('1','HIGH')

