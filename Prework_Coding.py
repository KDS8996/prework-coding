def hello_name(user_name):
    print("hello_" + user_name.title() + "!")
hello_name("USERNAME")


def first_odds():
    odd_num = [i for i in range(1, 100) if i % 2 == 1]
    return odd_num
print(first_odds())

def max_num_in_list(a_list):
    max_ = a_list[0]
    for ele in a_list:
        if (ele > max_):
            max_ = ele
    return max_

my_list  = [1, 2, 3, 4, 5]
result = max_num_in_list(my_list)
print(result)

def is_leap_year(a_year):
      if (a_year % 400 == 0):
            return True
      elif (a_year % 4 == 0) and (a_year % 100 != 0):
            return True
      else:
            return False
print(is_leap_year(2000))  
print(is_leap_year(2001))  

def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+ 1))
    
list1 = [3, 4, 5, 6, 7]
print(is_consecutive(list1))