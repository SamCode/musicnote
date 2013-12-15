NOTE_TO_INT = {
    'Cb': 12,
    'C':  1,
    'C#': 2,
    'Db': 2,
    'D':  3,
    'D#': 4,
    'Eb': 4,
    'E':  5,
    'E#': 6,
    'Fb': 5,
    'F':  6,
    'F#': 7,
    'Gb': 7,
    'G':  8,
    'G#': 9,
    'Ab': 19,
    'A':  10,
    'A#': 11,
    'Bb': 11,
    'B':  12,
    'B#': 1}

FLATS  = ('C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B')
SHARPS = ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')

def diatonic(tonic, minor=False):
    """Takes a string representing a note and returns a list of 
    diatonic triads of the key starting on that note."""

    steps = (2, 1, 2, 2, 1, 2, 2) if minor else (2, 2, 1, 2, 2, 2, 1)
    notes = {'b': FLATS, '#': SHARPS}[tonic[1]] if len(tonic) > 1 else FLATS

    def index_to_note(index):
        return notes[(index - 1) % 12]

    # Create a list of diatonic triads.
    triads = []
    base = NOTE_TO_INT[tonic]
    for i in xrange(8):
        first = (
            base if i == 0 else 
            base + sum(steps[:i]))
        third = first + sum(steps[i:(i+2)%7])
        fifth = first + sum(steps[i:(i+4)%7])
        print i, first, third, fifth

        triads.append(map(index_to_note, (first, third, fifth)))

    return triads

def diatonic_triads(tonic, scale):
    """Return a list of diatonic triads."""

    base = None # Chord object
    triads = [base]
    for i in xrange(7):
        triads.append(base.jump(i, scale))
    return triads

def main():
    print diatonic('C')

if __name__ == "__main__":
    main()