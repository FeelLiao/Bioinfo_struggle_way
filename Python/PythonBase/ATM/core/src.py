from lib.common import logger
def login():
    print("login panel")
    logger("exlon just logged in ")
def register():
    print("register panel")
    logger("exlon just registered ")
def withdraw():
    print("withdraw panel")
    logger("exlon just withdraw $1000 ")
def transfer():
    print("transfer panel")
    logger("exlon just transferred $1000000")
func_dict={
    "0":["login", login],
    "1":["register", register],
    "2":["withdraw", withdraw],
    "3":["transfer", transfer],
    "4":["exit",exit]
}
def run():
    while True:
        for k in func_dict:
            print(k,func_dict[k][0])
        choice=input("please input the number to control")
        if choice in func_dict:
            func_dict[choice][1]()
        else:
            print("input invalid")

