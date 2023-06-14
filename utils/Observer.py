'''
 # @ coding: utf-8
 # @ language: python
 # @ project: PyQtFlightTest
 # @ author: bcynuaa
 # @ date: 2023-06-14 21:17:16
 # @ license: Mozilla Public License 2.0
 # @ description: the file contains watchdog to monitor the data files used in the program
 '''

import time
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

kSleep_Time: float = 0.1

# TODO: this is a temporary solution, need to be improved

def callbackNone(event_src_path) -> None:
    pass

class ModifiedHandler(FileSystemEventHandler):
    
    def __init__(self, callback=callbackNone) -> None:
        super().__init__()
        self.callback = callback
        pass
    
    def on_modified(self, event) -> None:
        self.callback(event.src_path)
        pass
    
    pass

class WatchDog:
    
    def __init__(self, eyesore_path: str, sleep_time: float = kSleep_Time, callback=callbackNone) -> None:
        self.eyesore_path: str = eyesore_path
        self.sleep_time: float = sleep_time
        self.modified_handler: ModifiedHandler = ModifiedHandler(callback)
        self.observer: Observer = Observer()
        self.observer.schedule(self.modified_handler, self.eyesore_path, recursive=True)
        self.working: bool = False
        pass
    
    def setSleepTime(self, sleep_time: float) -> None:
        self.sleep_time = sleep_time
        pass
    
    def wakeUp(self) -> None:
        self.working = True
        self.observer.start()
        try:
            while self.working == True:
                time.sleep(self.sleep_time)
                pass
            pass
        except KeyboardInterrupt:
            self.observer.stop()
            pass
        self.observer.join()
        pass
    
    def sleep(self) -> None:
        self.working = False
        self.observer.stop()
        self.observer.join()
        pass
    
    pass

print("utils: Observer.py is imported")