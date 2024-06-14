# # variables are something that holds the value
#
# a = 5
# a = str(a)
# b = 'hello'  #quotes
# print(a, b)
# print(type(a))  #tpe is afunction,predefined
# #dynamic typing
# a, b, c = 5, 6, 7  #multiple assignment
# #a,b,c=5# is not possible
# print(a, b, c)
# #collection-any list or tuple
# a = ["fruits", "mango", "orange"]
# b, c, d = a  #unpacking
# print(a, "\n", b, c, d)
# a = """My
# Name
# is
# """
#
#
# #triple single/double --to print multiline strings
#
# #gloabl --outside function accessed by anyone
#
#
# def add():
#     a = 2
#     print(a, "\n")
#
#
# print(a)  #gloabl
# add()  #local
# #text-str,char
# a = "hi"
# #numeric-int,float,complex
# a = 4 + 1j
#
# #0 , 0.0 -- int doesnt have capa
#
# #sequential- list,tuple,range
# #set type-set and frozenset
# #boolean - true or false
# #binary- bit,bytes..
# #None type- null
# #type casting
# #strings-immutable,char array
# #modifying,concatenating
# a = "abc"
# print(a[2])
# print(len(a))  # return int -- length of the string
#
# a = "My name is abc"
# print("is" in a)  # bool type returned
# print(a.find('is'))
# print(a[:2])
# print(a[0:2])
# #negative indexing
# print(a[-9:-1])
# a = "abc"
# b = "CSD"
# print(a.upper())
# print(b.lower())
# a = "   abc,gdh"
# print(a.strip(" "))  #removing from whitespace - starting or ending
# print(a.split(","))
# a = "abc"
# b = "cdf"
# print(a + b)
# print(f'a={a}')  #formating
# #Escaping characters
# a = "My name is \"ABX\""  #backward slash--escaping charcater \" \n \t \r \b \f \'..and others
# print(a)
# a=5
# print(bool(a)) #true
# a=[]
# print(bool(a))
# #operator
# #arithematic- add/subtract/multiply/divide/exponent/modulus
# #assignment operator- = +=,-=,*=,/=
# #>=,<=,==,!=,>,<.---..Relationship
# #logical- or,and,not,xor
# #bitwise &,|,>>,<<
# #list operation
# #list doesn not support changing  order
# #print duplicte
# a = ["fruits", "mango", "orange"]
# print(a[0])
# #positive and negative
# a[0]="Chickoo"
# print(a)
#
# #slicing can be used... [3:5]
# #append or insert
# a.append("Heel")
# a.insert(2,"hello")
# print(a)
# b=["a","b","c"]
# print(a.pop())
#
# print(a.extend(b))
# print(b.extend(a))
# print(a+b)
# for i in a:
#     print(i)
# # print(a.clear())

x=[1,2,3,3,2,1,6,72,1,2]
a=x.sort()
print(a)
print(x.sort(reverse=True))
y=['acs','a','dcd','dg']
print(y.sort())