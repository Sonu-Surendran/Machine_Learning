from fastapi import FastAPI
import tensorflow as tf
from PIL import Image
from tensorflow import keras
from fastapi import File, UploadFile
import uvicorn

from tensorflow.keras.applications.xception import preprocess_input

import numpy as np

model = keras.models.load_model("xception_v5_15_0.800.h5", compile=False)

app = FastAPI()

classes = ['blazer',
 'blouse',
 'body',
 'dress',
 'hat',
 'hoodie',
 'longsleeve',
 'other',
 'outwear',
 'pants',
 'polo',
 'shirt',
 'shoes',
 'shorts',
 'skirt',
 't-shirt',
 'top',
 'undershirt']

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = Image.open(file.file).convert("RGB")

    image = image.resize((299, 299))

    img_arr = np.array(image)
    img_arr = np.expand_dims(img_arr, axis=0)

    pro_img = preprocess_input(img_arr)

    pred = model.predict(pro_img)

    prob = tf.nn.softmax(pred)[0]
    pred_ind = np.argmax(prob)
    predicted_class = classes[pred_ind]

    return predicted_class


if __name__ == "__main__":
    uvicorn.run("backend:app", host="127.0.0.1", port=8000, reload=True)

