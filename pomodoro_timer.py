import time

def countdown(minutes):
    seconds = minutes * 60

    while seconds > 0  :
        mins = seconds // 60
        sec = seconds % 60
        print(f"{mins:02d}:{sec:02d}",end="\r")
        time.sleep(1)
        
        seconds -= 1
    
    print("00:00")

def pomodoro(session):
     completed_session = 0
     if session > 0 :
        for x in range(session):
                print(f"SESSION {x+1}" )
                countdown(work_session)
                completed_session +=1
                if completed_session % 4 == 0 :
                    print("LONG BREAK")
                    countdown(long_break)
                else: 
                    print("SHORT BREAK")
                    countdown(short_break)
     
if __name__ == "__main__": 
    work_session= 2
    long_work_session = 50
    short_break = 1
    long_break = 15
   
    session = int (input(f"how many sessions will you like to do: ")) 
    pomodoro(session)
   
                