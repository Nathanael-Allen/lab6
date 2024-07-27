from Database import Database

class Name:
    __name = ""
    __year = int
    __gender = ""
    __count = int
    

    def setName(self, name):
        self.__name = name
    

    def getName(self):
        return self.__name
    

    def setYear(self, year):
        self.__year = year
    

    def getYear(self):
        return self.__year
    

    def setGender(self, gender):
        self.__gender = gender
    

    def getGender(self):
        return self.__gender
    

    def setCount(self, count):
        self.__count = count
    

    def getCount(self):
        return self.__count
    
    def showNames():
        names = Database().showNames()
        data = []
        for i in range(0, len(names)):
            newName = Name()
            newName.setName(names[i]["name"])
            newName.setYear(names[i]["year"])
            newName.setGender(names[i]["gender"])
            newName.setCount(names[i]["count"])
            data.append(newName)
        return data