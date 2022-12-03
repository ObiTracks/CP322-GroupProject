sign_mappings = {
    0: """
for i in range(5):
    print("Hello World")
""",
    1: """
i = 0
while i < 5:
    print("The Sun is Shining")
    i += 1""",
    2: """
if (i == 0):
    print("The World is at Balance")
""",
    3: """
elif (i == 1):  
    print("The World is out of Balance")
""",
    4: """
else:
    print("The World is Back in Balance")
""",
    5: """
def some_function():
    x = ("Hello World")
    return x

print(some_function())""",
}


def get_sign_mapping(sign: str):
    x = sign_mappings[sign]
    print(x)
    return x


def write_code_to_file(code: str, file_name: str = "output.py"):
    try:
        with open(file_name, 'a') as f:
            f.write(code)
            print('Code written to output.py')
        f.close()
    except Exception as e:
        print("Failed to write code to file: Error {}".format(e))

    return


def main(sign, output_filename):
    # Get whichever ASL sign has being displayed on the screen - will be a number from 0-7
    sign = get_sign_mapping(sign)
    write_code_to_file(sign, output_filename)



#Output file to write code to
output_filename = 'output.py'

# Erasing the contents of the output file before running the code
open(output_filename, 'w').close()

# Testing the code with dummy array of sign codes
sign_codes = [0, 1, 2, 3, 4, 5, ]
code_output = ""
for sign_code in sign_codes:
    main(sign_code, output_filename)