import json
import xmltodict

def read_File(filename,line):
    file = open(filename,"r")
    for i in range(int(line)):
        print(file.readline().split("\n")[0])
    print("...")

def xml_to_json(filename):
    inString = open(filename).read()
    if filename.split(".")[1] == "xml":
        outString = json.dumps(xmltodict.parse(inString),indent=4)
        outputFile = filename.split(".")[0]+".json"
    elif filename.split(".")[1] == "json":
        outString = json.dumps(xmltodict.unparse(inString), indent=4)
        outputFile = filename.split(".")[0] + ".xml"

    output = open(outputFile,"w")
    output.write(outString)
    output.close()
    print(outputFile)

def analyze_input(information):
    lst = information.split(" ")
    try:
        if lst[0] == 'head':
            read_File(lst[3],lst[2])
        elif lst[0] == 'weather':
            xml_to_json(lst[1])
        elif lst[0] == "exit":
            return True
    except:
        print('invalid comand "'+information+'"')

if __name__ == '__main__':
    running = True
    while running:
        if analyze_input(input(">")):
            running = False

