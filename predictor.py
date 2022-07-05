import cv2
import numpy as np
from keras.models import load_model


# to predict captcha
def predict(filepath):
    img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)

    if img is not None:  # image found at file path
        img = img / 255.0  # Scale image
    else:
        print("Not detected")
        return False

    # np.newaxis=1
    res = np.array(model.predict(img[np.newaxis, :, :, np.newaxis]))
    # added this bcoz x_train 243*25*65*1

    # returns array of size 1*5*14
    result = np.reshape(res, (5, 14))  # reshape the array
    k_ind = []
    # probs = []
    for i in result:
        k_ind.append(np.argmax(i))  # adds index of the char found in captcha

    capt = ""  # string to store predicted captcha
    for k in k_ind:
        capt += character[k]  # finds the char corresponding to the index

    if not capt:
        return False
    else:
        # Removing the ? from the end to get mathematical equation
        cleaned_captcha_characters = capt.split("=")[0]

        # Replacing ? from operator because * is too much noisy and model,
        # is predicting ? for * operator most of the time
        cleaned_captcha_characters = cleaned_captcha_characters.replace(
            "?",
            "*",
        )

        # Solve the Mathematical Equation to get the result
        resp = eval(cleaned_captcha_characters)

        return {
            "captcha_characters": cleaned_captcha_characters,
            "result": resp,
        }


if __name__ == "__main__":
    character = "012345679+-*=?"
    model = load_model("Captcha_Model")

    image_to_predict = "Image\\training_raw\\3+5=j.jpg"

    response = predict(image_to_predict)
    print(response)
