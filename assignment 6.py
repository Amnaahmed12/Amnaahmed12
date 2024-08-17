def sum_of_elements(list):
   return sum(list)

#Example  usage list:

numbers=[1,2,3,6,4]
result=sum_of_elements(numbers)
print("sum of elements:",result)

def  smallest_number(numbers):
   return min(numbers)

#Example  usage tuple:
numbers=(5,7,4,2)
smallest=smallest_number(numbers)
print(smallest)

def square_set(numbers):
   return{n**2 for n in numbers}

#Example usage set:
numbers={1,2,9,6}
squared_numbers=square_set(numbers)
print(squared_numbers)

def get_keys(dicionary):
   return list(dicionary.keys())

#Example usage dicionary.keys
dict={"name":"ahmed","age":17,"sity":"karach"}
keys=get_keys(dict)
print(keys)