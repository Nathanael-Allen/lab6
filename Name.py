from Database import Database

class Name:
    # A class called Name with private attributes and getter and setter methods
    __name = ""
    __year = int
    __gender = ""
    __count = int
    
    # Sets the name attribute
    def setName(self, name):
        self.__name = name
    
    # Returns the name attribute
    def getName(self):
        return self.__name
    
    # Sets the year attribute
    def setYear(self, year):
        self.__year = year
    
    # Returns the year attribute
    def getYear(self):
        return self.__year
    
    # sets the gender attribute 
    def setGender(self, gender):
        self.__gender = gender
    
    # returns the gender attribute 
    def getGender(self):
        return self.__gender
    
    # Sets the count attribute
    def setCount(self, count):
        self.__count = count
    
    # returns the count attribute
    def getCount(self):
        return self.__count
    
    
    def showNames():
        # calls the showNames class method of the Database class, this returns a list of
        # dictionaries. the method then loops through the list and creates a Name object
        # it then sets the name, year,gender, and count attributes using the setter methods
        # of the Name class. It appends this object to a list called data and once the
        # loop is complete it returns the data list.
        # The data list is a list of Name objects.
        names = Database.showNames()
        data = []
        for i in range(0, len(names)):
            newName = Name()
            newName.setName(names[i]["name"])
            newName.setYear(names[i]["year"])
            newName.setGender(names[i]["gender"])
            newName.setCount(names[i]["count"])
            data.append(newName)
        return data