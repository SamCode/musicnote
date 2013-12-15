import collections

ACC_PREF = -1

class Interval(object):
    """A distance between two notes."""

    def __init__(self, steps):
        if 0 <= steps:
            self.val = steps
        else:
            raise ValueError()

class Note(object):
    """A musical pitch.

    Class variables:
        NOTES
        NOTES2
        ACCS
        MAX_ACC_VAL - the maximum number of flats or sharps allowed for a note

    Instance variables:
        base - an int from 0 to 11
        octave - an int from 0 to 10
        acc - an int
        acc_sign - an int either -1, 0, or 1
    """

    NOTES = "C D EF G A B"
    NOTES2 = "CDEFGAB"
    ACCS = "b #"
    # ACCS = u"b\u266E#"
    MAX_ACC_VAL = 2

    def __init__(self, base, acc=0, octave=3):

        assert Note.NOTES[base] in Note.NOTES2
        assert -Note.MAX_ACC_VAL <= acc < Note.MAX_ACC_VAL
        assert 0 <= octave <= 10

        self.base = base
        self.acc = acc
        self.octave = octave

    def __str__(self):
        note_str = []
        note_str.append(Note.NOTES[self.base])
        for _ in xrange(self._acc_abs):
            note_str.append(Note.ACCS[self.acc_sign + 1])
        return ''.join(note_str)

    @property
    def val(self):
        return self.base + self.acc

    @property
    def acc(self):
        return self._acc_val

    @acc.setter
    def acc(self, value):
        self._acc_val = value
        self._acc_abs = abs(value)
        if self._acc_val:
            self.acc_sign = self._acc_val / self._acc_abs
        else:
            self.acc_sign = 0

    def equals(self, other): # sign=False
        """Test for equality between Note instances."""

        assert isinstance(other, Note)

        # if not sign: Bb = A#
        return (
            self.val == other.val and
            self.octave == other.octave)

    def clone(self):
        return Note(self.base, self.acc, self.octave)

    def jump(self, steps, acc_pref=None): # clone=False, scale=None
        new_val = self.val + steps
        new_octave = self.octave + new_val / 12
        new_val = new_val % 12
        new_acc = 0
        if Note.NOTES[new_val] == ' ':
            # Use the accidental symbol that was previously used,
            # or a flat if one didn't exist.
            new_acc = self.acc_sign or acc_pref or ACC_PREF

        self.octave = new_octave
        self.acc = new_acc
        self.base = new_val - self.acc

    def sub(self, other):
        """Returns the interval between two notes."""

class NoteGroup(object):
    """A set of notes."""

    def __init__(notes):
        self._notes = notes

    def __len__(self):
        return len(self._notes)

    def __getitem__(self, key):
        return self._notes[key]

    def __setitem__(self, key, value):
        self._notes[key] = value

    def __delitem__(self, key):
        del self._notes[key]

    def __iter__(self):
        return iter(self._notes)

    def __contains__(self, note):
        return note in self._notes

    def clone(self):
        raise NotImplementedError

    def jump(self, interval):
        for note in notes:
            note.jump(interval)

class Chord(NoteGroup):
    """A set of three or more notes."""

class Triad(Chord):
    """A set of three notes."""

class Scale(NoteGroup):
    """A musical scale.

    Instance variables:
        notes - a list of Note objects; first 8 notes of the scale
    """

    STEPS = (2, 2, 1, 2, 2, 2, 1) # heptatonic
    MAJOR = 0 # ionian
    MINOR = 5 # natural minor

    # type=None, chromatic, harmonic, melodic, jazz, pentatonic
    def __init__(self, tonic, type=0, acc_pref=None):
        """
        Arguments:
            tonic - a Note object
            type - an int"""

        self._notes = [tonic]
        scale = collections.deque(Scale.STEPS, 7)
        scale.rotate(type)
        
        note = tonic
        for steps in scale:
            note = note.clone()
            note.jump(steps, acc_pref = tonic.acc_sign or acc_pref or ACC_PREF)
            self._notes.append(note)

    def __getitem__(self, key):
        if key < 7:
            return self._notes.__getitem__(key)
        else:
            raise ValueError()

    # def diatonic(self):

if __name__ == "__main__":
    pass