class ProxyConnectionLost(Exception):
    def __init__(self, *args: object) -> (None):
        super().__init__(self.__class__.__name__,*args)
