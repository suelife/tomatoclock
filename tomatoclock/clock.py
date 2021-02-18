import time
import datetime
from tomatoclock.util.all_util import is_integer_num
from tomatoclock.util.all_util import exit_program


class Timer():
    def __init__(self) -> None:
        self._hour = 0
        self._minute = 1
        self._second = 0
        self._beforeSymbol = "-"
        self._afterSymbol = "="
        self._progressbarLen = 10
        
    def countdown(self):
        target_time = datetime.datetime.strptime(f"{self._minute}:{self._second}", "%M:%S")
        total_second = (target_time-datetime.datetime(1900,1,1,0,0,0)).total_seconds()
        start_time = time.perf_counter()
        while True:
            now = time.perf_counter()
            current_time = int(now - start_time)
            remaining_time = total_second - current_time
            if remaining_time < 0:
                print("")
                break
            
            remaining_min = int(remaining_time / 60)
            remaining_sec = int(remaining_time % 60)
            format_time = datetime.datetime.strptime(f"{remaining_min}:{remaining_sec}", "%M:%S").strftime("%M:%S")
            self._progressbar(current_time, total_second, format_time)
            time.sleep(1)
            
    def set_second(self, second:int):
        if is_integer_num(second):
            self._second = second
        else:
            exit_program("Second only could be an integer.")
    
    def set_minute(self, minute:int):
        if is_integer_num(minute):
            self._minute = minute
        else:
            exit_program("Minute only could be an integer.")
    
    def set_progressbar_len(self, length:int):
        if is_integer_num(length):
            self._minute = length
        else:
            exit_program("Progressbar Len only could be an integer.")
    
    def set_before_symbol(self, symbol:str):
        self._beforeSymbol = str(symbol)
        
    def set_after_symbol(self, symbol:str):
        self._afterSymbol = str(symbol)
    
    def _progressbar(self, current_time, total_second, format_time):
        percentage = current_time/total_second
        past_len = int(percentage * self._progressbarLen)
        remaining_len = self._progressbarLen-past_len
        print(f"{self._afterSymbol*past_len}{self._beforeSymbol*remaining_len} [{percentage:.0%}] ⏰ {format_time}", end='\r')
            
        
if __name__ == "__main__":
    import sys
    from pathlib import Path
    sys.path.append(Path(__file__).parent)

    
    c = Timer()
    c.set_second(30)
    c.set_minute(0)
    c.countdown()
