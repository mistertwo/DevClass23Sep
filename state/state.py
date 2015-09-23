class run:
    def __init__(self):
        self.valid_states = {
            "primer" : primer,
            "runner" : runner,
            "stopper" : stopper
            }
        self.current_state = "primer"
        print("I've alive!!! To use me, use the runme function. Lost? Put 'help' in as an argument.")
        return

    def runme(self, data):
        things_done = self.valid_states[self.current_state]()
        results = things_done.run(self, data)
        return results

    def changeup(self, data):
        if type(data) != str:
            print("incorrect data type")
            return
        
        if data in self.valid_states.keys():
            self.current_state = str(data)
            return

class primer:
    def run(self, caller, data):
        if type(data) == int:
            return "we're not running yet. give me the 'start' command."

        if data == "start":
            caller.changeup("runner") 
            return "starting up!"
        
        if data == "help":
            return "you can 'start' things up."        

        else:
            return "what do?"

class runner:
    def run(self, caller, data):
        if type(data) == int:
            return str("chosen run speed:" + str(data))

        if data == "start":
            return "already started"

        if data == "stop":
            caller.changeup("stopper")
            return "stopping!"
    
        if data == "help":
            return "tell me how fast you want to run with an integer. you can also 'stop' things." 

        else:
            return "what do?"

class stopper:
    def run(self, caller, data):
        if type(data) == int:
            return str("motor is currently stopped.")

        if data == "reset":
            caller.changeup("primer")
            return "priming for a restart!"

        if data == "help":
            return "I'm stopped right now. Perhaps you'd like to 'reset' things?"        
 
        else:
            return "what do?"


