while True:
    expression = input("Input expression (or 'exit' to exit: ")
    if expression == 'exit':
        break
    try:
        result = eval(expression)
        print(result)
    except SyntaxError:
        print("Error: invalid syntax")
    except NameError:
        print("Error: invalid variable or function name")
    except ZeroDivisionError:
        print("Error: division by zero")
    except Exception as e:
        print("Error: {}".format(e))