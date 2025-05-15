import unittest
import os
from src.overlay import process_batch_images

class TestBatchOverlay(unittest.TestCase):
    def test_batch_overlay_output_count(self):
        base_dir = "overlays/base_images"
        icon_dir = "overlays/icons"
        output_dir = "output"

        # Clean output folder
        for f in os.listdir(output_dir):
            os.remove(os.path.join(output_dir, f))

        # Run the batch process
        process_batch_images(base_dir, icon_dir, output_dir)

        # Assert: output should match base images count
        base_images = [f for f in os.listdir(base_dir) if f.endswith(('.jpg', '.png'))]
        output_images = [f for f in os.listdir(output_dir) if f.endswith(('.jpg', '.png'))]
        self.assertEqual(len(base_images), len(output_images))

if __name__ == "__main__":
    unittest.main()

