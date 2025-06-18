# type() is built in funtion that tells you data type of a variable or a value

a=10
print(type(a))   # int data type

b=10.5
print(type(b))   # float data type 

c=2+3j
print(type(c))   # complex data type involves char values + int values

str="gfg"
print(type(str))   # String is sequence of char

J=[10,20,30]
print(type(J))   # data stored in square braces is called *List

t=(20,40,30)
print(type(t))   # also similar like list but diff is you can't modify once you created a tuple
                 #these are immutable   - tuple stored in simple braces

s={10,30,40}    # set is collection of items , where all items are distinct and set is like mathematical set
print(type(s))

d={10:"gfg",20:"ide"}
print(type(d))  # dictionaries are used to do mappings, this is a collection of key value pairs
                # item:prices , rollno:name


