import tensorflow as tf
import tensorflow_hub as hub

# def load_model():
#     module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
#     model = hub.load(module_url)
#     print ("module %s loaded" % module_url)
#     return model

import tensorflow as tf
import tensorflow_hub as hub

def load_model():
    model_filename = 'universal_sentence_encoder'
    try:
        # Try to load the model from a saved file
        model = tf.keras.models.load_model(model_filename)
        print("Model loaded from file")
    except (OSError, IOError):
        # If the saved model file doesn't exist, download and save the model
        module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
        model = hub.load(module_url)
        model.save(model_filename)
        print("Model downloaded and saved")

    return model

def embed(input):
    model = load_model()
    return model(input)
