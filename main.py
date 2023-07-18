def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except SyntaxError:
        return "Error: invalid syntax"
    except NameError:
        return "Error: invalid variable or function name"
    except ZeroDivisionError:
        return "Error: division by zero"
    except Exception as e:
        return "Error: {}". format(e)


def main():
    while True:
        expression = input("Input expression (or 'exit' to exit: ")
        if expression == 'exit':
            break
        result = evaluate_expression(expression)
        print(result)


if __name__ == "__name__":
    main()
