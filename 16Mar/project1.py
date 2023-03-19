class student:
    def _init_(self):
        self.__student_id=None
        self.__marks=None
        self.__age=None
    def set_details(self,sid,sm,sa):
        self.__student_id=sid
        self.__marks=sm
        self.__age=sa
    def validate_marks(self):
        if 100>=self.__marks>=0:
            return True
        else:
            return False
    def validate_age(self):
        if self.__age>20:
            return True
        else:
            return False
    def check_qualification(self):
        if self.validate_marks() and self.validate_age():
            if self.__marks>=65:
                return True
        else:
            return True
    def choose_course(self):
        if self.check_qualification():
            self.fees=None
            self.course=int(input("\nyou are eligible for admission,\ninput 1001 to choose course 1001 (default fees 25575.0)\ninput 1002 to choose course 1002 (default fees 15500.0)\nyour choice: "))
            if self.course==1001 and self.__marks>85:
                self.fees =25575.0- 0.25*25575.0
            elif self.course==1001 and self.__marks<=85:
                self.fees =25575.0
            elif self.course==1002 and self.__marks>85:
                self.fees =15500.0- 0.25*15500.0
            elif self.course==1002 and self.__marks<=85:
                self.fees =15500.0
            print(f"\nyou have joined course {self.course} and your fees is {self.fees}")
            

s1=student()
s1.set_details(int(input("enter id: ")),int(input("enter marks: ")),int(input("enter age: ")))
s1.choose_course()