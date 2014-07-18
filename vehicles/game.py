class Vehicle(object):
    hit = False
    initials = "Hw"

    def receive_callback(self):
        self.hit = True

    def return_self(self):
        return self


class Cell(object):
    _callbacks = []

    def add_callback(self, callback):
        self._callbacks.append(callback)

    def add_return_callback(self, callback):
        self._return_callback = callback

    def hit(self):
        for callback in self._callbacks:
            callback()

    def get_vehicle(self):
        return self._return_callback
