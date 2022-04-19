class Tormoz:
    def __init__(self, is_abs: bool = False):
        self._is_abs = is_abs

    @property
    def is_abs(self):
        return self._is_abs

    def __str__(self):
        str_is_abs = 'is abs' if self.is_abs else ''
        return f"tormoz: {str_is_abs}"
