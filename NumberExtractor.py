import numpy as np
import cv2
import matplotlib.pyplot as plt
import numpy as np
from keras.models import model_from_json
from keras import backend as K
K.set_image_data_format('channels_last')  

json_file = open('models/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("models/model.h5")
print("Loaded saved model from disk.")
 
def identify_number(image):
    image_resize = cv2.resize(image, (28,28))    
    image_resize_2 = image_resize.reshape(1,28,28,1)    
    loaded_model_pred = loaded_model.predict(image_resize_2, verbose=0)
    loaded_model_pred_classes = np.argmax(loaded_model_pred, axis=1)
    return loaded_model_pred_classes[0]

def extract_number(sudoku):
    sudoku = cv2.resize(sudoku, (450,450))
    grid = np.zeros([9,9])
    for i in range(9):
        for j in range(9):
            image = sudoku[i*50:(i+1)*50,j*50:(j+1)*50]
            if image.sum() > 25000:
                grid[i][j] = identify_number(image)
            else:
                grid[i][j] = 0
    return grid.astype(int)




