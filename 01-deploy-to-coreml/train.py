import turicreate as tc
import os

current_dir = os.path.dirname(__file__)
data = tc.SFrame(os.path.join(current_dir, '../data/processed/beers.sframe'))

train, test = data.random_split(0.8)

model = tc.image_classifier.create(train, target='label')

# evaluate on test data
predictions = model.predict(test)
metrics = model.evaluate(test)
print(metrics)

# persist the model
model.export_coreml(os.path.join(
    current_dir, '../model/BeerClassifier.mlmodel'))
