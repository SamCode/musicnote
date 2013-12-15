import unittest

from musicnote.base import Note, Scale

class TestNoteMethods(unittest.TestCase):

    def setUp(self):
        self.note = Note(
            base = Note.NOTES.find('A'),
            acc = (Note.ACCS.find('b') - 1) * 2)

    def test_init(self):
        self.assertEqual(self.note.acc, -2)
        self.assertEqual(self.note.octave, 3)
        self.assertEqual(self.note.base, Note.NOTES.find('A'))

    def test_str(self):
        self.assertEquals(str(self.note), "Abb")

    def test_clone(self):
        # also tests equals
        self.assertTrue(self.note.equals(self.note.clone()))

    def test_jump(self):
        # Abb.jump(3) == Bb
        self.note.jump(3)
        note = Note(
            base = Note.NOTES.find('B'),
            acc = Note.ACCS.find('b') - 1)
        self.assertTrue(self.note.equals(note))

class TestScaleMethods(unittest.TestCase):

    def setUp(self):
        self.scale = Scale(
            tonic = Note(
                base = Note.NOTES.find('C')))

    def test_init(self):
        scale = "CDEFGAB"
        for i in xrange(7):
            self.assertEqual(str(self.scale[i]), scale[i])

    def test_diatonic(self):
        pass

if __name__ == '__main__':
    unittest.main()