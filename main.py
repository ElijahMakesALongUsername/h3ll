a=0
lines = []
import os
import time
curr_line = 1
last_line = 0
dev_copy = True

def h3ll_compile(what_to_compile):
    print("Code:")
    for x in what_to_compile:
        time.sleep(0.10)
        if x != "compile" or x != "save" or x != "load":
            print(x)
    time.sleep(2.0)

p = open('persistent', 'r')

def save_code():
    c_name = input("name: ")
    with open(c_name + '.h3ll', 'w') as c:
        c.write(lines)
    with open('persistent', 'w') as s:
        s.write("last_written=" + c_name + ".h3ll")
    os.startfile("main.py")

def load_code():
    pass


while (a == 0):
    line = input( str(curr_line) + "| ")
    lines.append(line)

    # lines
    if line == "close" or line == "quit":
        quit()
    elif line == "compile":
        lines.remove(line)
        h3ll_compile(lines)
    elif dev_copy and line == "dev.lines":
        lines.remove(line)
        print(str(lines))
    elif line == "clear":
        os.startfile("main.py")
        quit()
    elif line == "save":
        save_code()
        lines.remove(line)
    elif line == "load":
        lines.remove(line)
        
    curr_line += 1
    if curr_line != 1:
        last_line = curr_line - 1