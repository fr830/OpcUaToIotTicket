import time
import opc

opc.getexpression()


def getattributes():
    global counter1
    global expression1
    global random1
    counter1 = opc.getcounter()
    expression1 = opc.getexpression()
    random1 = opc.getexpression()
   # print(counter1)
   # print(expression1)
   # print(random1)


print("____")
print("/ __ \ ")
print("| |  | |_ __   ___   _   _  __ _ ")
print("| |  | | '_ \ / __| | | | |/ _` |")
print("| |__| | |_) | (__  | |_| | (_| |")
print("\____/| .__/ \___|  \__,_|\__,_|")
print("      | |")
print("      |_|     _____         _   _  _ _  _           _")
print("             |_   _|__ _ _ (_) | || (_)(_)_ _  _ _ (_)_ _  ___ _ _")
print("               | |/ _ \ ' \| | | __ / _` | ' \| ' \| | ' \/ -_) ' \ ")
print("               |_|\___/_||_|_| |_||_\__,_|_||_|_||_|_|_||_\___|_||_|")
print("--------------------------------------------------------------------")
print("----             1. Read OPCUA live Data                       -----")
print("----             2. Write to Wapice IOT Ticket                 -----")
print("--------------------------------------------------------------------")

var = input("Choose option: ")
if var == "1":
    opc.test()
elif var == "2":
    opc.toticket()


time.sleep(5)
