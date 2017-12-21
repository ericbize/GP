import time
import datetime
import sendd

def cycle1():
    var = 1
    while var==1 :
      x = run1()
      time.sleep(x)


def run1():
    now = datetime.datetime.now()
    hours = now.hour

    if hours > 8 and hours < 16:
      try:
       sendd.startt()
       return 54000
      except:
       return 60

    else:
       return 60

if __name__ == '__main__':
  cycle1()
