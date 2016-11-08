import unittest, random
import ps2


# test suite for the class RectangularRoom
class TestRectangularRoom(unittest.TestCase):
    def setUp(self):
        self.room = ps2.RectangularRoom(4, 3)
        random.seed(0)

    def test_width_height_boundaries(self):
        with self.assertRaises(ValueError) as context:
            ps2.RectangularRoom(-6, 6)
        self.assertTrue('width/height should be > 0 !' in str(context.exception))

    def test_room_size(self):
        self.assertEqual(self.room.height, 3)
        self.assertEqual(self.room.width, 4)

    def test_clean_tile_at_position(self):
        position = ps2.Position(2.3, 1.7)
        self.room.cleanTileAtPosition(position)
        self.assertTrue(self.room.tiles[2][1])

    def test_all_tiles_are_claned(self):
        room = ps2.RectangularRoom(4, 6)
        for x in range(4):
            for y in range(6):
                self.assertFalse(room.isTileCleaned(x, y))
        self.assertEqual(room.getNumCleanedTiles(), 0)

    def test_specific_tile_is_cleaned(self):
        position = ps2.Position(3.3, 2.7)
        self.room.cleanTileAtPosition(position)
        self.assertTrue(self.room.isTileCleaned(3, 2))
        self.assertFalse(self.room.isTileCleaned(2, 1))

    def test_number_of_tiles(self):
        self.assertEqual(self.room.getNumTiles(), 4*3)

    def test_number_cleaned_tiles(self):
        position = ps2.Position(3.3, 2.7)
        self.room.cleanTileAtPosition(position)
        position = ps2.Position(2.3, 1.7)
        self.room.cleanTileAtPosition(position)
        self.assertEqual(self.room.getNumCleanedTiles(), 2)

    def test_get_random_position(self):
        for n in range(100):
            position = self.room.getRandomPosition()
            self.assertTrue(self.room.isPositionInRoom(position))

if __name__ == '__main__':
    unittest.main()