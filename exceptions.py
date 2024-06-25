def divide():

    try:
        op1=(float(input("digit the fist numeric value: ")))
        op2=(float(input("digit the second numeric value: ")))
        print("the division is: " + str(op1/op2))
    except ValueError:
        print("the value is not acceptable")
    except ZeroDivisionError:
        print("zero division not allow")
    finally:
        print("operation finished")

divide()