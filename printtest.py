#use output formats

name="johnBakerTest"
age=25
salary= 10000.25

#Approach 1
print("APPROACH one is here")
print(name, age, salary)

#print(name, int(age), float(salary))

#Approach 2
print("APPROACH two is here")
print("name:", name)
print("age is:", age)
print("salary is:", salary)

#Approach 3
print("APPROACH 3 - using percentage)")
print("name:%s age:%d salary:%f" %(name, age, salary))

#Approach 4
print("APPROACH 4 - using curly brackets")
print("name:{} age:{} salary{}". format(name, age, salary))

#Approach 5
print("APPROACH 5 - passing index with brackets")
print("name:{0} age:{1} salary{2}". format(name, age, salary))
