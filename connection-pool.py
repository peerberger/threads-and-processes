import threading


class Connection:
    def open():
        pass

    def close():
        pass

class ConnectionPool:
    def __init__(self):
        self._connections = [Connection() for _ in range(10)]
        self.lock = threading.Lock()

    def get_connection(self):
        s
