import os
path = os.path.join(os.path.join(os.path.dirname(__file__), os.pardir), os.pardir)
import sys
import math
import random
sys.path.append(path)
from settings import *
from School.Tests.tests import connect_to_db

conn, cur = connect_to_db('../Tests/tests.sqlite')

def get_lrs(cur):
    sql = '''SELECT subject, date, type FROM Tests'''
    result = cur.execute(sql)
    return result

class PlanCreator():
    def __init__(self, lrs : list, num_subjects=2) -> None:
        self.EPSILON = 200
        self.lrs = lrs
        self.num_subjects = num_subjects
        if type(lrs) != 'list':
            self.lrs = list(lrs)
            # self.lrs = list(map(lambda x: list(x), lrs))
        self.priority_list = self.priority_set()
    
    def priority_set(self):
        priority_list = {'math': 0.85, 'physics':0.80, 'chemistry': 0.75, 'biology':0.70, 'ai': 0.65, 'history':0.60, 'civics':0.55, 'geography':0.50, 'economics':0.45, "english":0.40, 'hindi':0.35, 'telugu': 0.20}
        for subject, priority_score in priority_list.items():
            for lr_instance in self.lrs:
                if subject.upper() in lr_instance:
                    priority_list[subject] += 1
        print(priority_list)
        return priority_list

    def get_num_instances(self):
        subjects = ['math','ai',  "biology", "chemistry", "hindi", "physics", "history", "geography", "civics", "telugu", "english"]
        num_instances = {}
        for subject in subjects:
            multiplier = self.priority_list[f'{subject}']
            instances = math.ceil(multiplier * self.EPSILON)
            num_instances[f'{subject}'] = instances      
        return num_instances
    
    def make_plan(self):
        instances = self.get_num_instances()
        self.chosen_list = []
        for key, val in instances.items():
            for i in range(0, val+1):
                self.chosen_list.append(key)
        final_choices = []
        for i in range(0, self.num_subjects):
            choice =random.choice(self.chosen_list)
            final_choices.append(choice)
        plan = self.review_plan(final_choices)
        return final_choices
    
    def review_plan(self, plan):
        try:
            remove = []
            for index, subject in enumerate(plan):
                if plan.count(subject) > 2:
                    remove.append(index)
            for sub in plan:
                remove_choice = random.choice(remove)
                plan[remove_choice] = random.choice(self.chosen_list)
        except IndexError:
            pass
        return plan

        
        
        
lrs = get_lrs(cur)

creator = PlanCreator(lrs, 5)
choices = creator.make_plan()
print(choices)