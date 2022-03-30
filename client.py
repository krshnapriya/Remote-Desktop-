import pyautogui as pg
import socket



client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
client_socket.connect(("192.188.56.1","9302")) 

message = 'done'
while True:
    try:
        while message.lower().strip() != 'bye':
            client_socket.send(message.encode())  
            data = client_socket.recv(1024).decode()  
            if data == 'click':
                pg.click(x, y)
            elif data == 'del':
                pg.typewrite(['backspace'])
            elif data.startswith('cde:'):
                pg.write(data.replace('cde:', ''))
            elif data=='rclick':
                pg.click(button='right')
            elif data=='dclick':
                pg.click(clicks=2)
            elif data=='nl':
                pg.typewrite(['enter'])
            else:
                x = int(data.split(' ')[0])
                y = int(data.split(' ')[1])
                pg.moveTo(x, y)
            message = 'done' 

        client_socket.close()  
    except:
        pass
