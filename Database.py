class Database:
    # This is a class called Database, it's attribute __names stores a list of dictionaries
    # the dictionaries contain dummy data of most popular names by year 
    # between the years 1915 and 1919
    __names = [
        {"name": "John", "year": 1915, "gender": "M", "count": 47577},
        {"name": "John", "year": 1916, "gender": "M", "count": 50046},
        {"name": "John", "year": 1917, "gender": "M", "count": 51851},
        {"name": "John", "year": 1918, "gender": "M", "count": 56599},
        {"name": "John", "year": 1919, "gender": "M", "count": 53532},
    ]

    @classmethod
    def showNames(cls):
        # This is a class method that returns the attribute __names 
        # (a list of dictionaries) from the class Database
        return cls.__names
    