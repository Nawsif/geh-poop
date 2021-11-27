import requests
import threading
import webbrowser

webbrowser.open_new_tab("https://discord.gg/ZYx5Udp2pf")
print("JOIN THE DISCORD FOR MORE! https://discord.gg/ZYx5Udp2pf")
threadsnum = input("Enter threads amount: ")
startid = int(input("Enter start id: "))

def groupchecker(ishiscool):
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}
    global startid
    rangereq = 9000000 - int(startid)
    for x in range(int(rangereq)):
        r = requests.get("https://groups.roblox.com/v1//groups/" + str(startid), headers=headers)
        if "owner" in r.json():
            if "isLocked" in r.json():
                if r.json()["owner"] == None and r.json()["publicEntryAllowed"] == True and r.json()["isLocked"] == False:
                    validtxt = "[VALID] Group ID: " + str(startid)
                    print(str(validtxt))
                    open("valid.txt", "a+").write(f"Group name: {r.json()['name']} | https://www.roblox.com/groups/{startid} | Members: {r.json()['memberCount']}\n")
                else:
                    invalidtxt = "[INVALID] Group ID: " + str(startid)
                    print(str(invalidtxt))
                startid = startid + 1
            elif "isLocked" not in r.json():
                if r.json()["owner"] == None and r.json()["publicEntryAllowed"] == True:
                    validtxt = "[VALID] Group ID: " + str(startid)
                    print(str(validtxt))
                    open("valid.txt", "a+").write(f"Group name: {r.json()['name']} | https://www.roblox.com/groups/{startid} | Members: {r.json()['memberCount']}\n")
                else:
                    invalidtxt = "[INVALID] Group ID: " + str(startid)
                    print(str(invalidtxt))
                startid = startid + 1
    
threads = list()
for index in range(int(threadsnum)):
    x = threading.Thread(target=groupchecker, args=(index,))
    threads.append(x)
    x.start()