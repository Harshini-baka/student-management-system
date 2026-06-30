class Student:
    def __init__(self,name,roll_no,dept,mark):
        self.name=name
        self.roll_no=roll_no
        self.dept=dept
        self.mark=mark
    
    def __str__(self):
        return f"{self.name}-{self.roll_no}"
    
    def display_details(self):
        print("\n====STUDENT DETAILS====")
        print(f"Name      : {self.name}")
        print(f"Roll no   : {self.roll_no}")
        print(f"Department: {self.dept}")
        print(f"Mark      : {self.mark}")
        print(f"Grade     : {self.calculate_grade()}")
    
    def calculate_grade(self):
        if self.mark>=90:
            return "A"
        elif self.mark>=80:
            return "B"
        elif self.mark>=70:
            return "C"
        elif self.mark>=50:
            return "D"
        else:
            return "F"
    
    def to_dict(self):
     return {
        "name": self.name,
        "roll no": self.roll_no,
        "dept": self.dept,
        "mark": self.mark
     }
    
    @classmethod
    def from_dict(cls,data):
        return cls(
            data["name"],
            data["roll no"],
            data["dept"],
            data["mark"]

        )
    
    def update_name(self,new_name):
        self.name = new_name
    def update_dept(self, new_dept):
        self.dept = new_dept
    def update_mark(self,new_mark):
        self.mark = new_mark

    @classmethod
    def from_row(cls,row):
        return cls(
            row[1],
            row[2],
            row[3],
            row[4]
        )
