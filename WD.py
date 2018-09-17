# This is a test.

print("hello")

print("yo ho ho")

def roxprint(x):
    print(x)

roxprint('hello')
roxprint('foo' + 'bar' + 'bletch' + 'spam')

def addition(x, y):
   print(x + y)

addition(44, 45)

def mult3(x, y, z): #function
    return x * y * z


rda = mult3(3, 4, 5)
print("rda = ", rda)

s = 'sophie'
print(s[2:5]) #array slice

s.capitalize()
print(s.capitalize())

print(s.upper())

ip = '10.0.1.99'
print(ip.split('.'))
print(ip.split('.')[3])