from decorator import decorator, uppercase_decorator, split_string

@decorator
def function():
    print("Dentro da função")
    
function()

@split_string
@uppercase_decorator
def text():
    return "Hello World"

print(text())

@split_string
@uppercase_decorator
def example():
    return "Aprendendo Python e criando decorators"
print(example())