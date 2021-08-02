# Assigning values to variables in multiple lines
Age = 20
Sal = 30000
# Assigning values to multiple variables in the same line
Niha, Chandu, Nikki = 26, 24, 24
# Assigning same value to multiple variables in the same line
Developer = Tester = Devops = 50000
# Assigning both Integer and String values to multiple variables in the same line
Salary, Job_Description = 350000, "Junior Software Developer"
# Passing values as Tuples and printing them
print("Age: %s \nSal: %s" % (Age, Sal))
print("Ages of Niha, Chandu, Nikki are %s, %s, %s respectively" % (Niha, Chandu, Nikki))
print("The salary of %s is %s" %(Job_Description, Salary))
# Passing values as Dictionary and printing them
print("Salaries of the jobs are as follows:\nDeveloper: %(a)s\nTester: %(b)s\nDevops: %(c)s" % {'a': Developer,
                                                                                                'b': Tester,
                                                                                                'c': Devops})

