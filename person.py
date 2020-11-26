# Create a class called Person which defines the generic data and functionality of a human.
# A class is a collection of attributes and functions. Different languages use different terminology for these things, but the bacic concepts are the same.
# Give your Person class should have the following attributes:
# name
# age
# gender
# interests. This is a list or array of strings
# Give your Person class a hello function:

class Person:
    def __init__(self, name, age, gender, interests):
        self.name = name
        self.age = age
        self.gender = gender
        self.interests = interests

    def hello(self):
        size = len(self.interests)
        intro = "Hello my name is " + self.name 
        years = " and I am " + str(self.age) + " years old."
        likes = " My interests are "
        end = " and " + self.interests[size - 1] + "."
        for item in range(0, size):
            if item == size - 1:
                break
            likes += self.interests[item]
            if item < size - 2:
                likes += ', '
        result = intro + years + likes + end
        return result

person = Person("Lelana Matobela", 27, "female", ['yoga', 'reading', 'coding', 'netball', 'hockey'])
greeting = person.hello()
print(greeting)