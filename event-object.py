import threading
import time

def helper_function(event_obj, timeout,i):
  print("Thread started, for the event to set")
 
  flag = event_obj.wait(timeout)
  if flag:
    print("Event was set to true() earlier, moving ahead with the thread")
  else:
    print("Timeout occurred, event internal flag still false. Executing thread without waiting for event")
    print("Value to be printed=", i)
    
if __name__ == '__main__':
  event_obj = threading.Event()
#   event_obj2 = threading.Event()
  
  thread1 = threading.Thread(target=helper_function, args=(event_obj,10,27))
  thread1.start()

  time.sleep(5)
  
  event_obj.set()
#   event_obj2.set()
  print("Event is set to true. Now threads can be released.")
  print()
