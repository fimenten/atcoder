import socket

def main():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect(("192.168.3.20", 50002))

    while(1):
        data = soc.recv(1024)
        print("Server>", data.decode("utf-8"))      # サーバー側の書き込みを表示
        data = input("Client>") # 入力待機
        soc.send(data.encode("utf-8"))              # ソケットに入力したデータを送信

        if data == "q":             # qが押されたら終了
            soc.close()
            break

main()