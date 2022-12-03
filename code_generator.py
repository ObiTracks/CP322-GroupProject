sign_mappings = {
    0 : """
for i in range(5):
    print("Hello World")
""",
    1 : """
i = 0
while i < 5:
    print("The Sun is Shining")
    i += 1""",
    2 : """
if (i == 0):
    print("The World is at Balance")
""",
    3 : """
elif (i == 1):  
    print("The World is out of Balance")
""",
    4 : """
else:
    print("The World is Back in Balance")
""",
    5 : """
def some_function():
    x = ("Hello World")
    return x

print(some_function())""",
}


def get_sign_mapping(sign: str):
    x = sign_mappings[sign]
    print(x)
    return x


def write_code_to_file(code: str):
    try:
        with open('output.py', 'w+') as f:
            f.write(code)
            print('Code written to output.py')
    except Exception as e:
        print("Failed to write code to file: Error {}".format(e))

    return


def main(sign_codes):
    # Get whichever ASL sign has being displayed on the screen - will be a number from 0-7
    code_output = ""
    for sign_code in sign_codes:
        sign = get_sign_mapping(sign_code)
        code_output += sign

    write_code_to_file(code_output)


# Testing the code
sign_codes = [0, 1, 2, 3, 4, 5, ]
main(sign_codes)
