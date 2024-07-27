class Database:
    __names = [
        {"name": "John", "year": 1915, "gender": "M", "count": 47577},
        {"name": "John", "year": 1916, "gender": "M", "count": 50046},
        {"name": "John", "year": 1917, "gender": "M", "count": 51851},
        {"name": "John", "year": 1918, "gender": "M", "count": 56599},
        {"name": "John", "year": 1919, "gender": "M", "count": 53532},
    ]

    def showNames(cls):
        return cls.__names
    