from uart_parse import UARTParser


class SpeedConfig():
    def __init__(self, uart_parser: UARTParser) -> None:
        self.speed = 0
        self.mode = "normal"
        self.count_down = 0  # 单位为秒

        self.uart_parser = uart_parser

    def update_uart_parser(self, uart_parser: UARTParser):
        self.uart_parser = uart_parser

    def send(self):
        speed_data = f"S {self.speed}\n"
        mode_data = f"M {self.mode}\n"
        count_down = f"C {self.count_down}\n"
        data = speed_data+mode_data+count_down
        self.uart_parser.send_data(data)
