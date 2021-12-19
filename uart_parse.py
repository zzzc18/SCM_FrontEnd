from re import T
import serial  # 导入模块
import time
import serial.tools.list_ports


def get_uart_default_settings():
    return "COM1", 9600, 8, 'N', 1


def get_port_list():
    _port_list = list(serial.tools.list_ports.comports())
    port_list = []
    for port in _port_list:
        port_list.append(str(port)[:4])
    return port_list


class UARTParser():
    def __init__(self, port, baudrate, bytesize, parity, stopbits) -> None:
        self.port = port
        self.baudrate = baudrate
        self.bytesize = bytesize
        self.parity = parity
        self.stopbits = stopbits

        # Read Cache
        self.speed = 0
        self.temperature = 20
        self.reconnect()

    def reconnect(self):
        try:
            self.serial = serial.Serial(port=self.port, baudrate=self.baudrate, bytesize=self.bytesize,
                                        parity=self.parity, stopbits=self.stopbits, timeout=None)
        except Exception as e:
            print("---串口连接异常---", e)

    def set_to_default(self):
        self.port = "COM1"
        self.baudrate = 9600
        self.bytesize = 8
        self.parity = 'N'
        self.stopbits = 1

    def get_settings(self):
        return self.port, self.baudrate, self.bytesize, self.parity, self.stopbits

    def get_data(self):
        try:
            data = self.serial.read_all()
        except Exception as e:
            print("---读取数据异常---", e)
        data = str(data, encoding="utf-8")
        if data == "":
            return
        lines = data.split("\r\n")
        for line in lines:
            if line == "":
                continue
            command, value = line.split(" ")
            if command == "T":
                self.temperature = int(value)
            elif command == "S":
                self.speed = int(value)
            else:
                print("Command not found")
            # print(f"command: {command}")
            # print(f"value: {value}")

    def send_data(self, data):
        try:
            length = self.serial.write(bytes(data, encoding="utf8"))
            print(length)
        except Exception as e:
            print("---发送数据异常---", e)


if __name__ == "__main__":
    print(get_port_list())
    parser = UARTParser(*get_uart_default_settings())
    while True:
        # print(parser.get_data())
        parser.get_data()
        parser.send_data("Test\n")
        time.sleep(2)
