class Caretaker:
    def __init__(self):
        self._history = []

    def save(self, memento):
        self._history.append(memento)

    def undo(self):
        if not self._history:
            return None
        return self._history.pop()