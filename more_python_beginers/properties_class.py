class Presenter():
    def __init__(self, name):
        #Constructor
        self.name = name #calling property
    
    @property
    def name(self):
        print('In the getter')
        return self.__name

    @name.setter
    def name(self, value):
        print('In setter')
        # cool validation here 
        self.__name = value


presenter = Presenter('Chris')
presenter.name = 'Christopher'
    
