import os
import sys
path = os.path.join(os.path.abspath('../../'))
sys.path.append(path)
import math
import random
import pandas as pd
from settings import *
from School.Tests.tests import connect_to_db

conn, cur = connect_to_db('../Tests/tests.sqlite')

def get_lrs(cur):
    try:
        sql = '''SELECT subject, date, type FROM Tests'''
        result = cur.execute(sql)
    except Exception:
        return ''
    return result

class PlanCreator():
    def __init__(self, lrs : list, num_subjects=2) -> None:
        self.EPSILON = 200
        self.lrs = lrs
        self.num_subjects = num_subjects
        if type(lrs) != 'list':
            self.lrs = list(lrs)
        self.priority_list = self.priority_set()
    
    def priority_set(self):
        priority_list = {'math': 90, 'physics':80, 'chemistry': 70, 'biology':60, 'ai': 50, 'history':40, 'civics':30, 'geography':20, 'economics':10, "english":5, 'hindi':3, 'telugu': 2}
        for subject, priority_score in priority_list.items():
            for lr_instance in self.lrs:
                if subject.upper() in lr_instance:
                    priority_list[subject] += 30
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
        return plan
    
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
def create_plans():
    for i in range(1000):
        choices = creator.make_plan()
        yield choices
choices = create_plans()
df = pd.DataFrame(choices, columns=['sub_1', 'sub_2', "sub_3", "sub_4", "sub_5"])
df.to_csv('train.csv')