# Decorators

# Decorators are the function build to perform some task

# It can add extra features in existing function without doing any changes inside that existing function.

# @ is used to denote that one


def greet(fx):
    def good():
        print("Good Morning")
        fx()
        print("Thanks for Choosing Python") # After calling the decorators 
    return good
@greet  # Calling decorators using greet # inhance the funtion 
def hello():
    print("Hello World!")
hello()