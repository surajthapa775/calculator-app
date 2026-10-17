from calc_func import do_addition, do_subtraction
from multiply import do_multiply
def main():
    print("Hello calculator")
    print("""
            \nSelect the  function from the given option
            1. Add
            2. Subtract
            3. Mul
            """)

    user_input= input("Select the function\n")

    a= int(input("Value of A\n"))
    b= int(input("Value of B\n"))

    if user_input== "1":
        result= do_addition(a,b)
    elif user_input=="2":
        result= do_subtraction(a,b)
    elif user_input=="3":
        result= do_multiply(a,b)

    print(result)

if __name__=="__main__":
    main() 