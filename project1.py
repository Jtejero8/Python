name = input()
print(f'hello {name}')


x = 10 

if x > 0:
    print('is positive')
elif x < 0:
    print('in negative')
else:
    print('is zero')

names = ["alice", "bob", "George"]

for i in range(5):
    print(i)

ages = {"alice": 22, "bob": 27}
 

def square(x):
    return x * x


for i in range(10):
    print("{} square is {}".format(i, square(i)))

class Point:
    def _init_(self, x, y):
        self.x = x
        self.y = y

# p = Point( 3, 5)
# print(p.x)
# print(p.y)

# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return "Hello, World!"


