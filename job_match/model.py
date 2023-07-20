import tensorflow as tf
import tensorflow_hub as hub
import tarfile

# def load_model():
#     module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
#     model = hub.load(module_url)
#     print ("module %s loaded" % module_url)
#     return model

def extract_model():
    with tarfile.open("/universal-sentence-encoder_4.tar.gz", "r") as tf:
        print("Opened tarfile")
        tf.extractall(path="./extraction_dir")
        print("All files extracted")

def load_model():
    model_dir = "./extraction_dir/"
    try:
        # Try to load the model from a saved file
        model =  hub.load(model_dir)
        print("Model loaded from file")
    except (OSError, IOError):
        # print("Something went wrong!")
        # If the saved model file doesn't exist, download and save the model
        module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
        model = hub.load(module_url)
        model.save(model_dir)
        print("Model downloaded and saved")

    return model

def embed(model, input):
    text_list = [input]
    embedding = model(text_list)
    return embedding
