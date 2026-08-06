
def add(a,b):
    return a + b

def sub(a,b):
    return a - b


def mul(a,b):
    return a * b


def div(a,b):
    return a / b


def mod(a,b):
    return a % b


function_list = ["add", "sub", "mul", "div", "mods"]

if __name__=="__main__":
    print("Testing and function: ")
    add_result = add(3,5)
    print("addition result: ", add_result)

    print("Testing sub function: ")
    sub_result = sub(3,5)
    print("subtraction result: ", sub_result)

    print("Testing mul function: ")
    mul_result = mul(3,5)
    print("multiplication result: ", mul_result)

    print("Testing div function: ")
    div_result = div(3,5)
    print("division result: ", div_result)

    print("Testing mod function: ")
    mod_result = mod(3,5)
    print("modulus result: ", mod_result)




def is_palindrome(text: str) -> bool:
    """Check if a word is a palindrome."""
    return text == text[::-1]