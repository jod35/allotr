import re

python_processing = ["Python To Pseudocode convertor"]
by_hand = []
python_variables = []


def code_indent(linestart):
    spaces = 0
    linecheck = python_processing[linestart]
    for i in linecheck:
        if i == " ":
            spaces += 1
        else:
            break
    return spaces


def ending_insert(linestart, endstatement):
    current_line = linestart + 1
    spaces = code_indent(linestart)
    start_spaces = spaces
    try:
        while (
            code_indent(current_line) > spaces
            or "else" in python_processing[current_line]
        ):
            current_line += 1
            if (
                len(python_processing) == current_line
            ):  # Handles situations where the indent runs to end of file
                break
    except:
        byhandadd = "line " + str(i) + " Hit an error. Please check"
        by_hand.append(byhandadd)
    z = (" " * start_spaces) + endstatement
    python_processing.insert(current_line, z)


MyPython = open("MyPythonFile")
for line in MyPython:
    line = line.strip("\n")
    python_processing.append(line)

# = processing to arrow
for i in range(len(python_processing)):
    if "=" in python_processing[i]:
        if "==" in python_processing[i]:
            python_processing[i] = python_processing[i].replace("==", "=")
        elif " = " in python_processing[i]:
            python_processing[i] = python_processing[i].replace(
                " = ", "<-"
            )  # Can't use Unicode arrows on windows.
        elif re.search("[a-z]=[a-z]", python_processing[i]):
            python_processing[i] = python_processing[i].replace(
                "=", "<-"
            )  # Can't use Unicode arrows on windows.


# if statements

i = 0
while i < len(python_processing):  # Need to use while, because list gets bigger!
    if "else:" in python_processing[i]:
        python_processing[i] = python_processing[i].replace("else:", "ELSE")

    if "elif" in python_processing[i]:
        python_processing[i] = (
            python_processing[i] + "  //You will need to change this to CASE OF"
        )
    elif "if " in python_processing[i]:
        python_processing[i] = python_processing[i].replace("if", "IF")
        python_processing[i] = python_processing[i].replace(":", "")
        ending_insert(i, "ENDIF")
        x = code_indent(i + 1)
        z = " " * x + "THEN"
        python_processing.insert(i + 1, z)
    i += 1

# for loops

i = 0
while i < len(python_processing):  # Need to use while, because list gets bigger!
    if "for " in python_processing[i]:
        python_processing[i] = python_processing[i].replace("for", "FOR")
        if "range" in python_processing[i]:
            if re.search("[0-9]{1},[0-9]{1,3}", python_processing[i]):
                python_processing[i] = python_processing[i].replace("in range(", " <- ")
                python_processing[i] = python_processing[i].replace(",", " TO ")
                python_processing[i] = python_processing[i].replace("):", "")
                ending_insert(i, "NEXT")
            elif re.search("[0-9]{1}", python_processing[i]):
                python_processing[i] = python_processing[i].replace(
                    "in range(", "0 TO "
                )
                python_processing[i] = python_processing[i].replace("):", "")
                ending_insert(i, "NEXT")
        else:
            python_processing[i] = (
                python_processing[i] + "  //Pseudocode can't handle this"
            )

    i += 1

# Possible repeat loops

for i in range(len(python_processing)):
    if "break" in python_processing[i]:
        python_processing[i] = (
            python_processing[i] + "  //This might be better as a repeat loop"
        )


# While loops
i = 0
while i < len(python_processing):  # Need to use while, because list gets bigger!
    if "while " in python_processing[i]:
        python_processing[i] = python_processing[i].replace("while", "WHILE")
        python_processing[i] = python_processing[i].replace(":", " DO")
        ending_insert(i, "ENDWHILE")

    i += 1


# input statements
i = 0
while i < len(python_processing):  # Need to use while, because list gets bigger!
    if "input" in python_processing[i]:
        var_builder = ""
        for j in python_processing[i]:
            if j != "<-":
                if j != " ":
                    var_builder += j
            else:
                break

        if "int" in python_processing[i]:
            declare = "DECLARE " + var_builder + " : INTEGER"
        elif "float" in python_processing[i]:
            declare = "DECLARE " + var_builder + " : REAL"
        else:
            declare = "DECLARE " + var_builder + " : STRING"

        python_variables.append(declare)
        var_builder = "INPUT " + var_builder
        python_processing[i] = var_builder
    i += 1
for i in python_variables:
    python_processing.insert(1, i)

# Possible arrays
for i in range(len(python_processing)):
    if "=[" in python_processing[i]:
        # DECLARE StudentNames : ARRAY[1:30] OF STRING
        python_processing[i] = python_processing[i] + "  //Possible array."

# Print to output
for i in range(len(python_processing)):
    if "print" in python_processing[i]:
        python_processing[i] = python_processing[i].replace("print(", "OUTPUT ")
        python_processing[i] = python_processing[i].replace(")", "")

# functions / procedures
i = 0
while i < len(python_processing):  # Need to use while, because list gets bigger!
    if "def " in python_processing[i]:
        if "():" in python_processing[i]:
            python_processing[i] = python_processing[i].replace("def", "PROCEDURE ")
            python_processing[i] = python_processing[i].replace("()", "")
            ending_insert(i, "ENDPROCEDURE")
        else:
            python_processing[i] = python_processing[i].replace("def", "FUNCTION ")
            ending_insert(i, "ENDFUNCTION")
            x = code_indent(i + 1)
            z = " " * x + "RETURNS // What gets sent back?"
            python_processing.insert(i + 1, z)

    i += 1

# Changes comments # to //
for i in range(len(python_processing)):
    if "#" in python_processing[i]:
        python_processing[i] = python_processing[i].replace("#", "//")


x = 0
numbers = input("Would you like line numbers? Y/N")
if numbers.upper() == "Y":
    for i in python_processing:
        print(x, i)
        x += 1
else:
    for i in python_processing:
        print(i)

for i in by_hand:
    print(i)
