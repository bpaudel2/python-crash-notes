class Presenters():
    def __init__(self, name):
        #Constructor 
        self.name = name #Field 
    
    def say_hello(self):
        #method 
        print('Hello, '+ self.name)


presenter = Presenters('Chris')
presenter.name = 'Christopher'
presenter.say_hello()
