var1 = "Guru99!"
var2 = "Software Testing"
print("var1[0]:", var1[0])
print("var2[1:5]:", var2[1:5])

x = "Hello World!"
print(x[:6])
print(x[0:6] + "Guru99")

oldstring = 'I like Guru99'
newstring = oldstring.replace('like', 'love')
print(newstring)

string = "python at guru99"
print(string.upper())

print(":".join("Python"))
wordz = "guru99 career guru99"
print(wordz.split(' '))

x = "Guru99"
x = x.replace("Guru99", "Python")
print(x)
tup1 = ('Robert', 'Carlos', '1965', 'Terminator 1995', 'Actor', 'Florida');
tup2 = (1, 2, 3, 4, 5, 6, 7);
print(tup1[0])
print(tup2[1:4])

x = ("Guru99", 20, "Education")  # tuple packing
(company, emp, profile) = x  # tuple unpacking
print(company)
print(emp)
print(profile)

a = {'x':100, 'y':200}
b = a.items()
print (b)

x = ("a", "b","c", "d", "e")
print (x[2:4])

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
studentX=Boys.copy()
studentY=Girls.copy()
print(studentX)
print(studentY)

