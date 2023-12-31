import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

# class HemileiaVastatrix:
#     def __init__(self,filename):
#         self.filename =filename

#     def predictioncoffeeleafrust(self):
#         # load model
#         model = load_model(os.path.join("artifacts","training", "model.h5"))

#         imagename = self.filename
#         test_image = image.load_img(imagename, target_size = (224,224))
#         test_image = image.img_to_array(test_image)
#         test_image = np.expand_dims(test_image, axis = 0)
#         result = np.argmax(model.predict(test_image), axis=1)
#         print(result)

#         if result[0] == 1:
#             prediction = 'healthy'
#             return [{ "image" : prediction}]
#         else:
#             prediction = 'unhealthy'
#             return [{ "image" : prediction}]
class HemileiaVastatrix:
    def __init__(self, filename):
        self.filename = filename

    def predictioncoffeeleafrust(self):
        # Load model
        model = load_model(os.path.join("artifacts", "training", "model.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = model.predict(test_image)

        # Assuming the classes are 0 for healthy and 1 for unhealthy
        class_labels = ["healthy", "unhealthy"]
        predicted_class = class_labels[np.argmax(result)]

        return [{"image": predicted_class, "probabilities": result.tolist()}]
