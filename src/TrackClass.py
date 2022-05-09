class Track:
    def __init__(self, notes=None, velocity=1, instrument=None):
        self.notes = notes
        self.velocity = velocity
        self.activate = True
        self.instrument = instrument      # 0=guitarra , 1= violin, 2= piano, 3= lo que quieran agregar
        self.signal_out = []
        self.change = True      # Si esta en True es pq en el update se modificaron las notas/velocidad/instrument

    def update(self, newtrack):
        if self.notes != newtrack.notes or self.velocity != newtrack.velocity or self.signal_out != newtrack.intrument:
            self.notes = newtrack.notes
            self.velocity = newtrack.velocity
            self.signal_out = newtrack.intrument
            self.activate = newtrack.activate
            self.signal_out = []
            self.change = 1
        else:
            self.activate = newtrack.activate
            self.change = 0


