try:
    num = input("Enter number")
    print("user entered {}".format(num))
except:
    print("Wrong user input".format(num))
finally:
    print("User attempted input")