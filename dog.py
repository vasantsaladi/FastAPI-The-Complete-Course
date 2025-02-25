class Dog:
    def __init__(self, name: str = "", age: int = 0):
        # Private attributes using name mangling with __
        self.__name = name
        self.__age = age
        self.__energy_level = 100  # Additional private attribute
    
    # Getter method for name
    @property
    def name(self) -> str:
        return self.__name
    
    # Setter method for name
    @name.setter
    def name(self, value: str) -> None:
        if not value.strip():
            raise ValueError("Name cannot be empty")
        self.__name = value.strip()
    
    # Getter method for age
    @property
    def age(self) -> int:
        return self.__age
    

    super()