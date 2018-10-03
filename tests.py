import unittest
from sequencefolder import (
    _DimensionAccessor as DimensionAccessor, SequenceFolder
)


class TestDimensionAccessorGet(unittest.TestCase):
    def test_2d_square(self):
        da = DimensionAccessor('ABCDEFGHIJKLMNOPQRSTUVWXY', (5, 5), [])
        self.assertEqual(da[0][0], 'A')
        self.assertEqual(da[1][1], 'G')
        self.assertEqual(da[4][2], 'W')
        self.assertEqual(da[4][4], 'Y')

    def test_2d(self):
        da = DimensionAccessor('ABCDEFGHIJKLMNOPQRSTUVWX', (3, 8), [])
        self.assertEqual(da[0][5], 'F')
        self.assertEqual(da[1][0], 'I')
        self.assertEqual(da[2][7], 'X')

    def test_3d_square(self):
        da = DimensionAccessor('ABCDEFGHIJKLMNOPQRSTUVWXYZ0', (3, 3, 3), [])
        self.assertEqual(da[0][0][0], 'A')
        self.assertEqual(da[1][1][1], 'N')
        self.assertEqual(da[0][2][1], 'H')
        self.assertEqual(da[2][2][2], '0')

    def test_3d(self):
        da = DimensionAccessor('ABCDEFGHIJKLMNOPQRSTUVWX', (2, 2, 6), [])
        self.assertEqual(da[0][0][5], 'F')
        self.assertEqual(da[0][1][2], 'I')
        self.assertEqual(da[1][1][5], 'X')
        self.assertEqual(da[1][0][0], 'M')
        self.assertEqual(da[0][0][4], 'E')


class TestDimensionAccessorSet(unittest.TestCase):
    # All positions were determined with random.org

    def test_2d(self):
        da = DimensionAccessor([42 for i in range(4 * 2)], (4, 2), [])
        da[0][1] = 9
        da[2][1] = 9
        da[0][0] = 9
        self.assertEqual(da[0][1], 9)
        self.assertEqual(da[2][1], 9)
        self.assertEqual(da[0][0], 9)

    def test_3d(self):
        da = DimensionAccessor([42 for i in range(9 * 6 * 7)], (9, 6, 7), [])
        da[4][2][0] = 9
        da[6][4][3] = 9
        da[7][0][4] = 9
        da[4][1][4] = 9
        da[1][5][4] = 9
        self.assertEqual(da[4][2][0], 9)
        self.assertEqual(da[6][4][3], 9)
        self.assertEqual(da[7][0][4], 9)
        self.assertEqual(da[4][1][4], 9)
        self.assertEqual(da[1][5][4], 9)


class TestSequenceFolder(unittest.TestCase):
    def test(self):
        sf = SequenceFolder([42 for i in range(4 * 2)], (4, 2))
        sf[0][1] = 9
        sf[2][1] = 9
        sf[0][0] = 9
        self.assertEqual(sf[0][1], 9)
        self.assertEqual(sf[2][1], 9)
        self.assertEqual(sf[0][0], 9)


if __name__ == '__main__':
    unittest.main()
