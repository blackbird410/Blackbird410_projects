class Person:
    ledger  = []

    def __init__(self, lastName="", firstName="", age=0, gender="Male", occupation="", address="") -> None:
        assert gender == "Male" or gender == "Female", f"{gender} is an incorrect gender."

        self.lastName = lastName
        self.firstName = firstName
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.address = address

        Person.ledger.append(self)

    def __repr__(self) -> str:
        return f"Person( Name        : {self.lastName}\n"\
               f"        First Name  : {self.firstName}\n"\
               f"        Age         : {self.age}\n"\
               f"        Gender      : {self.gender}\n"\
               f"        Occupation  : {self.occupation}\n"\
               f"        Address     : {self.address}\n"\
                ")"


        