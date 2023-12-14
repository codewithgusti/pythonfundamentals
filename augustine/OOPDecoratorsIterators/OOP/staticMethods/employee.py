
class Employee(object):
    def __init__(self, name,salary,project_name):
        self.name = name
        self.salary =salary
        self.project_name = project_name
    
    @staticmethod
    def gather_requirements(project_name):
        if project_name == 1:
            requirements = ['task_1']
        else:
            requirements = ['task_1', 'task_2' , 'task_3']
        return requirements
    
    def work(self):
        requirements = self.gather_requirements(self.project_name)
        for task in requirements:
            print('completed ', task)
            
    
emp = Employee('Augustine',1200,'ABC Project')
emp.work()