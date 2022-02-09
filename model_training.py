from tensorflow_examples.lite.model_maker.core.task.model_spec.image_spec import efficientnet_lite4_spec
from tflite_model_maker import image_classifier
from tflite_model_maker.image_classifier import DataLoader

path = r"C:\Users\User\PycharmProjects\ScoreFace\faces-fiq"
data = DataLoader.from_folder(path)
train_data, rest_data = data.split(0.8)
validation_data, test_data = rest_data.split(0.5)
model = image_classifier.create(train_data, validation_data=validation_data, model_spec=efficientnet_lite4_spec)
loss, accuracy = model.evaluate(test_data)
model.export(export_dir='.')