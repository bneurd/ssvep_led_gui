import network
from machine import idle


def wireless_connection():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    nets = wlan.scan()
    for net in nets:
        if net[0] == b'nome_da_rede':
            print('Network found!')
            wlan.connect(net[0], 'senha_da_rede')
            while not wlan.isconnected():
                idle()
            print('WLAN successfully connected!')
            print('IP Address: {}'.format(wlan.ifconfig()[0]))
            break


if __name__ == "__main__":
    wireless_connection()
