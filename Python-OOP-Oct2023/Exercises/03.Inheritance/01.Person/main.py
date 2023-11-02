from project.person import Person
from project.child import Child

person = Person("Peter", 25)
child = Child("Peter Junior", 5)
print(person.name)
print(person.age)
print(child.__class__.__bases__[0].__name__)  # base class name
assert child.__class__.__bases__[0].__name__ == 'Person'
print(child.__class__.__name__)  # object's class name

print(child.__class__)
# <class '__main__.Child'>

print(child.__class__.__bases__[0])
# <class '__main__.Person'>
