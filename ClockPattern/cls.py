import time
import schedule
import clsModule as cm

def main():

    cm.clsModule()
    
if __name__=="__main__":
	schedule.every(1).seconds.do(main)
  
while True:
    schedule.run_pending()
