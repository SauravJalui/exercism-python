# # from datetime import timedelta as t

# # def add_gigasecond(now):
# # 	return now + t(seconds = 10 ** 9)
    
# import datetime

# ONE_GIGASECOND = 1000000000


# def add_gigasecond(d):
#     return d + datetime.timedelta(0, ONE_GIGASECOND)

# my_dict = {'a': 'jill', 'b': 'tom', 'c': 'tim'}
# for key in my_dict.keys():
#     print(key)


# Examples of iteration with for loops.

# my_list = [0, 1, 2, 3, 4, 5]

# # Print each value in my_list. Note you can use the "in" keyword to iterate over a list.
# for item in my_list:
#     print('The value of item is: '+ str(item))

# # Print each index and value pair.
# for i, value in enumerate(my_list):
#     print('The index value is: ' + str(i) + '. The value at i is: ' + str(value))   

#     # Print each number from 0 to 9 using a while loop.
# i = 0
# while(i < 10):
#     print(i)
#     i += 1


# # Print each key and dictionary value. Note that you can use the "in" keyword 
# # to iterate over dictionary keys.
# my_dict = {'a': 'jill', 'b': 'tom', 'c': 'tim'}
# for key in my_dict:
#     print(key + ', ' + my_dict[key])


# # Example function 1: return the sum of two numbers.
# def sum(a, b):
#     return a+b

# # Example function 2: return the size of list, and modify the list to now be sorted.
# def list_sort(my_list):
#     my_list.sort()
#     return len(my_list),  my_list


# def smallest_positive(in_list):
# 	in_list.sort()
# 	print(in_list[0])
# 	return print(" sorted list = ", in_list )

# print(smallest_positive([4, -6, 7, 2, -4, 10]))

# def myFunc(e):
#   return len(e)

# cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

# cars.sort(key=myFunc)

# print(cars)

# def smallest_positive(in_list):
# 	a = sorted(in_list)
# 	return a[0]

# print(smallest_positive([4, -6, 7, 2, -4, 10]))

# print(smallest_positive([4, -6, 7, 2, -4, 10]))
# # Correct output: 2

# print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# # Correct output: 0.2


# def smallest_positive(in_list):
#     # TODO: Define a control structure that finds the smallest positive
#     # number in in_list and returns the correct smallest number.
#     smallest_pos = None
#     for num in in_list:
#         if num > 0:
#             # Note: we use a logical "or" in this solution to form 
#             # the conditional statement, although this was
#             # not introduced above. 
#             if smallest_pos == None or num < smallest_pos:
#                 smallest_pos = num
#     return smallest_pos

# # Test cases

# print(smallest_positive([4, -6, 7, 2, -4, 10]))
# # Correct output: 2

# print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# # Correct output: 0.2

# def smallest_positive(in_list):
#     # TODO: Define a control structure that finds the smallest positive
#     # number in in_list and returns the correct smallest number.
#     min = 999999999999999999999999999
#     for num in in_list:
#         if num < min and num > 0.0:
#             min = num
    
#     if len(in_list) > 1:
#         return min
#     else:
#         return None


# # Test cases

# print(smallest_positive([4, -6, 7, 2, -4, 10]))
# # Correct output: 2

# print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# # Correct output: 0.2

# def smallest_positive(in_list):
#     # TODO: Define a control structure that finds the smallest positive
#     # number in in_list and returns the correct smallest number.
#     smallest_pos = None
#     for num in in_list:
#         if num > 0:
#             # Note: we use a logical "or" in this solution to form 
#             # the conditional statement, although this was
#             # not introduced above. 
#             if smallest_pos == None or num < smallest_pos:
#                 smallest_pos = num
#     return smallest_pos

# # Test cases

# print(smallest_positive([4, -6, 7, 2, -4, 10]))
# # Correct output: 2

# print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# # Correct output: 0.2

# This exercise uses a data structure that stores Udacity course information.
# The data structure format is:

#    { <semester>: { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }


# courses = {
#     'spring2020': { 'cs101': {'name': 'Building a Search Engine',
#                            'teacher': 'Dave',
#                            'assistant': 'Peter C.'},
#                  'cs373': {'name': 'Programming a Robotic Car',
#                            'teacher': 'Sebastian',
#                            'assistant': 'Andy'}},
#     'fall2020': { 'cs101': {'name': 'Building a Search Engine',
#                            'teacher': 'Dave',
#                            'assistant': 'Sarah'},
#                  'cs212': {'name': 'The Design of Computer Programs',
#                            'teacher': 'Peter N.',
#                            'assistant': 'Andy',
#                            'prereq': 'cs101'},
#                  'cs253': {'name': 'Web Application Engineering - Building a Blog',
#                            'teacher': 'Steve',
#                            'prereq': 'cs101'},
#                  'cs262': {'name': 'Programming Languages - Building a Web Browser',
#                            'teacher': 'Wes',
#                            'assistant': 'Peter C.',
#                            'prereq': 'cs101'},
#                  'cs373': {'name': 'Programming a Robotic Car',
#                            'teacher': 'Sebastian'},
#                  'cs387': {'name': 'Applied Cryptography',
#                            'teacher': 'Dave'}},
#     'spring2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
#                            'teacher': 'Dorina'},
#                         'cs003': {'name': 'Programming a Robotic Robotics Teacher',
#                            'teacher': 'Jasper'},
#                      }
#     }

# # In this exercise, you will need to complete the function 
# # when_offered(courses, course). This function accepts a "courses" 
# # data structure and a "course" string. 
# # The function should return a list of strings representing the semesters 
# # when the input course is offered. See the two test cases below for examples 
# # of correct results.


# def when_offered(courses, course):
#     # TODO: Fill out the function here.
#     semesters = []
#     for semester in courses:
#         if course in courses[semester]:
#             semesters.append(semester)
#     # TODO: Return list of semesters here.
#     return semesters



# print(when_offered(courses, 'cs101'))
# # Correct result: 
# # ['fall2020', 'spring2020']

# print(when_offered(courses, 'bio893'))
# # Correct result: 
# # []

def prod(a,b):
    # TODO change output to the product of a and b
    return a*b

def fact_gen():
    i = 1
    n = i
    while True:
        output = prod(n, i)
        yield output
        i += 1
        n = output

# Test block
my_gen = fact_gen()
num = 5
for i in range(num):
    print(next(my_gen))

# Correct result when num = 5:
# 1
# 2
# 6
# 24
# 120