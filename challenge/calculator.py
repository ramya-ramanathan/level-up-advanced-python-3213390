class Calculator:
    def __init__(self,error_t1, error_t2, error_t3, error_t4) -> None:
        self._types = []
        self._types.append(error_t1)
        self._types.append(error_t2)
        self._types.append(error_t3)
        self._types.append(error_t4)
        self.error = None

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type in self._types:
            self.error = exc_type
            return True
        return False
    