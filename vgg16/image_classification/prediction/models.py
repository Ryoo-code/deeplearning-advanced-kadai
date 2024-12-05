from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.models import save_model
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions

import numpy as np
import tensorflow as tf
#モデルを初期化（必要に応じてweights='imagenet'など変更）
model = VGG16(weights='imagenet')
# モデルを保存
save_model(model, 'vgg16.h5')

#画像判定関数
def classify_image(image):
    image = preprocess_input(image) #前処理
    prediction = model.predict(image)#推論
    return decode_predictions(prediction,top=5) #上位3件を返す