class Track:
    def __init__(self, notes=None, velocity=127, instrument=None):
        self.notes = notes
        self.velocity = velocity
        self.activate = True
        self.instrument = instrument      # 0 = guitarra , 1 = violín, 2 = piano, 3 = lo que quieran agregar
        self.signal_out = []
        self.change = False      # Si esta en True es pq en el update se modificaron las notas/velocidad/instrument

    def update(self, velocity, activate, instrument):
        if self.velocity != velocity or self.instrument != instrument:
            self.velocity = velocity
            self.instrument = instrument
            self.activate = activate
            self.signal_out = []
            self.change = True
        else:
            self.activate = activate
            self.change = False
