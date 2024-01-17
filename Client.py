import socket
import pyautogui


def tab_changer():
    pyautogui.hotkey('Alt', 'Tab')


serverIp = "Your private ip"
serverPort = 2222
bufferSize = 1024
UDPServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPServer.bind((serverIp, serverPort))
print("Server is started....")
while True:
    data, address = UDPServer.recvfrom(bufferSize)
    dataDecode = data.decode("utf-8")
    if dataDecode == "Changed":
        tab_changer()
    print(dataDecode)
