import queue

class Sink:
    
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.queue = queue.Queue()
        
    def get_coordinates(self):
        return self.coordinates
    
    def exchange_message(self, message):
        self.queue.put(message)
    
    def deliver_message(self):
        return self.queue.get()
    
    def print_sink(self):
        print(self.coordinates)
        print(self.queue.qsize())
