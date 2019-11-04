#!/usr/local/bin/python3

'''
Generators: a technique of returning a value and saving the function status, every function
call the result will be a continuation of the previous status, the function resumes rather 
than restarts.
@author: Jorgeley, Ivan Freeza
'''


from pympler import summary, muppy
import psutil
import resource
import os
import sys
import random
import time

def getMemory():
    process = psutil.Process(os.getpid())
    mem = process.memory_info()[0]
    return mem

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

#common way of returning a bulk list/dictionaire
def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

#generator: rather than returning the whole list it returns item by item
def people_generator(num_people):
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
	#this returns the item and save the current state, so next loop starts from 2nd item and so on...
        yield person

print('PID: ', os.getpid())
time.sleep(2)
print ('Memory (Before): {}'.format(getMemory()))
t1 = time.process_time()

#comment the following call and uncomment the next one to see the difference
#people = people_generator(1000000)

#comment the following call and uncomment the previous one to see the difference
people = people_list(1000000)
for i in people:
	print(id(i))
t2 = time.process_time()

print( 'Memory (After) : {}'.format(getMemory()))
print ('Took {} Seconds'.format(t2-t1))
time.sleep(5)
