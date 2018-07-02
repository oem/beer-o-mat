import turicreate as tc
import re
import os


def path_as_label(path):
    label = re.search('(?<=raw/)(.+)?/.+$', path).group(1)
    label = label.replace('_', ' ')
    return label.title()


img_path = os.path.join(os.path.dirname(__file__), '../data/raw')
data = tc.image_analysis.load_images(img_path, with_path=True)
data['label'] = data['path'].apply(path_as_label)
data.print_rows(num_rows=50)
data.save(os.path.join(os.path.dirname(__file__),
                       '../data/processed/beers.sframe'))
