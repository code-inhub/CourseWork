class TechWorld:
    
    def __init__(self, name, skills, exp, feedback):
        self._name = name 
        self._skills = skills
        self._exp = exp
        self._feedback = feedback
        
    def check_eligibility(self):
        if (self._exp>3 and self._feedback>=4.5) or (self._exp<=3 and self._feedback>=4):
            print("Eligible, experience and feedback matches")
            return True
        else:
            print("Not eligible, experience and feedback doesn't match")
            return False
        
    def allocate_course(self, tech):
        if tech in self._skills:
            print("Course skill present")
            return True
        else:
            print("Skill not present")
            return False
        
    def final_decision(self,tech):
        if (self.check_eligibility()==True) and (self.allocate_course(tech)==True):
            print("Congratulations, allocation done!")
        else:
            print("Sorry, can't be allocated")
            
n = input("Enter name: ")
s = int(input("Enter number of skills: "))
skills = []
for i in range(s):
    print("Enter skill ", i+1, ": ")
    skill = input()
    skills.append(skill)
e = float(input("Enter experience (in years): "))
f = float(input("Enter feedback rating (0 to 5): "))
appl = input("Enter technology for application: ")

obj = TechWorld(n, skills, e, f)
obj.final_decision(appl)