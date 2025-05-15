import unittest
import os
from src.overlay import add_overlay

class TestOverlayFunction(unittest.TestCase):
    def test_output_created(self):
        output_path = "output/test_result.png"
        add_overlay(
            base_path="overlays/base.jpg",
            overlay_path="overlays/icon.png",
            output_path=output_path,
            position=(10, 10),
            size=(100, 100),
            opacity=200
        )
        self.assertTrue(os.path.exists(output_path))

if __name__ == "__main__":
    unittest.main()

