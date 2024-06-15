class A: 
    def __init__(self,name,surname,categorry,marriedstatus):
        self.name=name
        self.surname=surname
        self.categorry=categorry
        self.marriedstatus=marriedstatus
                 
    def show(self):
        print('my name is=',self.name)
        print('my surnamne is=',self.surname)
        print('my csṭegory is=',self.categorry)
        print('my married status is=',self.marriedstatus)
obj=A('siddharth','badkur','obc','null')
obs=A('arun','patel','obc','null')
obj.show()
obs.show()
print(obj.name)
print(obs.name)
