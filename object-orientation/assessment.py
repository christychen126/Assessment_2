"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
    1. Abstraction: It hides details from users, but user can still use it without 
        knowing how it works. 
    2. Encapsulation: 
        Objects in the same class will have similar properties, and methods are close 
        to the data(objects) that they can be called on.
    3. Polymorphism: For children classes that inherit from same parent class, 
        there are some commons in the children classes. They can have same attributes 
        or can call same methods which are defined in their parent class. 

2. What is a class?
    A class can group functions(methods) and attributes which can be applied to 
    some objects (intances) together.  

3. What is an instance attribute?
    It's a variable in a class and is specific to each instance.

4. What is a method?
    It is a functions that is defined in a class, and can only apply to instances 
    belong to the class. It has to call "self" as it's first argument.


5. What is an instance in object orientation?
    It is an object that is initiated in a class. It has it's own data, and can call
    methods from the class that it is initiated in. 

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   A class attribue is a variable definded at class level, while an instance attribute 
   is defined at instance level and will vary when differnt instances are initiated.
   Instances in the same class will have same class attributes, but differnt instance
   attributes.
   For example, "is drinkable" can be a class attribute for a class of "Coffee", 
   but each instance of "Coffee" can have differnt types, names, origins, tastes 
   which are instance attributes. 


"""


# Parts 2 through 5:
# Create your classes and class methods


class Student(object):

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        user_input = raw_input(self.question)
        if user_input == self.correct_answer:
            return True
        else:
            return False


class Exam(object):

    def __init__(self, name):
        self.name = name       
        self.questions = []
        
    def add_question(self, question, correct_answer):
        my_question = Question(question, correct_answer)
        self.questions.append(my_question)

    def administer(self):
        score = 0
        for question in self.questions:
            if question.ask_and_evaluate():
                score += 1
        return score

def take_test(exam, student):
    student.score = exam.administer()


def example():
    exam = Exam('Fluffy')
    exam.add_question("Are you a dog?", "Yes I am!")
    exam.add_question("Are you hungry?", "Kind of.")
    student = Student("Agnes", "Potter", "The closet")
    take_test(exam, student)



class Quiz(Exam):
    



