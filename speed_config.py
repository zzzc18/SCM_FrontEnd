from uart_parse import UARTParser
import logging


class SpeedConfig():
    def __init__(self, uart_parser: UARTParser) -> None:
        self.speed = 0
        self.mode = "normal"
        self.count_down = 0  # 单位为秒

        self.uart_parser = uart_parser

    def update_uart_parser(self, uart_parser: UARTParser):
        self.uart_parser = uart_parser

    def send(self):
        speed_data = f"S{self.speed:03d}"
        mode_data = f"M{self.mode:03d}"
        count_down = f"C{self.count_down:03d}"
        data = speed_data+mode_data+count_down
        self.uart_parser.send_data(data)
        logging.warning(
            f"[风扇转速设定] 转速：{self.speed}% 工作模式：{self.mode} 倒计时设定：{self.count_down}秒")
