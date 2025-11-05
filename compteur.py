class Compteur:
    def __init__(self, value=0):
        self.value = value

    def __iadd__(self, other):
        """operator +="""
        self.value += other
        return self

    def __isub__(self, other):
        """operator -="""
        self.value -= other
        return self

    def __repr__(self):
        return f"Compteur({self.value})"
