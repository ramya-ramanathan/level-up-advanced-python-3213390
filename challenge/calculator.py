class Calculator:
    def __init__(self,*args) -> None:
        self._types = []
        self._types += args
        self.error = None

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type in self._types:
            self.error = exc_type
            return True
        return False
    