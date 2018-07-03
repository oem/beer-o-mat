import turicreate as tc
import os

current_dir = os.path.dirname(__file__)
model = tc.load_model(os.path.join(
    current_dir, '../model/v1.model'))

images = tc.load_images(os.path.join(current_dir, '../data/test'))
images['predictions'] = model.predict(images)
images.print_rows(num_rows=10)
