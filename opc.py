import sys
import time
import msvcrt
import ticket
from opcua import Client
sys.path.insert(0, "..")


client = Client("opc.tcp://DESKTOP-EA768IN:53530/OPCUA/SimulationServer")
client.connect()
root = client.get_root_node()




def getcounter():
    myvar = root.get_child(["0:Objects", "5:Simulation", "5:Counter1"])
#    mystring = str(myvar.get_browse_name())
#    test = mystring.split(":")[1]
#    print(test.split(")")[0] + " Value: " + str(myvar.get_value()))
#    print(myvar.nodeid.Identifier)
    return {'Name': myvar.nodeid.Identifier, 'Value': myvar.get_value()}
    client.disconnect()


def getexpression():
    myvar = root.get_child(["0:Objects", "5:Simulation", "5:Expression1"])
    return {'Name': myvar.nodeid.Identifier, 'Value': myvar.get_value()}
    client.disconnect()


def getrandom():
    myvar = root.get_child(["0:Objects", "5:Simulation", "5:Random1"])
    return {'Name': myvar.nodeid.Identifier, 'Value': myvar.get_value()}
    client.disconnect()

def test():
    while True:
        counter = root.get_child(["0:Objects", "5:Simulation", "5:Counter1"])
        print(counter.nodeid.Identifier + " " + str(counter.get_value()))
        expression = root.get_child(["0:Objects", "5:Simulation", "5:Expression1"])
        print(expression.nodeid.Identifier + " " + str(expression.get_value()))
        random = root.get_child(["0:Objects", "5:Simulation", "5:Random1"])
        print(random.nodeid.Identifier + " " + str(random.get_value()))
        time.sleep(1)
        if msvcrt.kbhit():
            break


def toticket():
    while True:
        counter = root.get_child(["0:Objects", "5:Simulation", "5:Counter1"])
        print(counter.nodeid.Identifier + " " + str(counter.get_value()))

        expression = root.get_child(["0:Objects", "5:Simulation", "5:Expression1"])
        print(expression.nodeid.Identifier + " " + str(expression.get_value()))

        random = root.get_child(["0:Objects", "5:Simulation", "5:Random1"])
        print(random.nodeid.Identifier + " " + str(random.get_value()))

        ticket.send(counter.get_value(),expression.get_value(),random.get_value())
       # print(counter.nodeid.Identifier + " " + str(counter.get_value()))
       # expression = root.get_child(["0:Objects", "5:Simulation", "5:Expression1"])
       # print(expression.nodeid.Identifier + " " + str(expression.get_value()))
       # random = root.get_child(["0:Objects", "5:Simulation", "5:Random1"])
       # print(random.nodeid.Identifier + " " + str(random.get_value()))
        time.sleep(0.5)
        if msvcrt.kbhit():
            break



