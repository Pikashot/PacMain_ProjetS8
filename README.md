# Pacmain : Project S8
Github for the project PacMain.  
Code adapted from https://github.com/kinivi/hand-gesture-recognition-mediapipe by Kazuhito Takahashi (https://twitter.com/KzhtTkhs).

# Requirements
Can be found in requirements.txt

# Directory
<pre>
.
│   .gitignore
│   app.py
│   LICENSE
│   README.md
│   requirements.txt
│
├───model
│   │   RF_classification.ipynb
│   │   trained_RF
│   │   trained_RF_exercise_0
│   │   trained_RF_exercise_5
│   │   trained_RF_exercise_8
│   │   trained_RF_exercise_9
│   │
│   ├───data
│   │       cleandata.csv
│   │       donnees_reelles.csv
│   │       données25200.csv
│   │       exo_0.csv
│   │       exo_5.csv
│   │       exo_8.csv
│   │       exo_9.csv
│   │
│   └───labels
│           labels.csv
│           labels_exercise_0.csv
│           labels_exercise_5.csv
│           labels_exercise_8.csV
│           labels_exercise_9.csv 
│
└───utils
    │   cvfpscalc.py
    │   data_Augmentation_BROUILLON.ipynb
    │   data_Augmentation_CLIMAX.ipynb
    │   key_code_index.txt
    │   read_keyboard_keys.py
    │   select_rows.py
    │   __init__.py
</pre>

### app.py
This is a sample program for inference. Lauch the running app.py. For the moment, this app is dedicated to the recongnition onf ONLY RIGHT HAND signs. The results for the left hand can not be guaranteed. <br>

There are currently 5 recognition modes available. These modes correspond to the reeducation mouvements 0, 5, 8 and 9. The default mode is -1 and corresponds to the recognition of all of the available hand signs (16 in total).

In addition, this app can be used to collect the landmark coordinates in order to create or enlarge a training dataset. To do so, lauch the app by running app.py and enter mode data collection by pressing "k". Remark: To use the data collection feature properly, your keyboard must be configured in QWERTY. If you press any key from "0" to "9" or "a" to "y", the landmarks of the current hand sign position will be captured and added to "model/model/données_reelles.csv" with the key as an index. A key code index is available in utils/key_code_index.txt.<br>

### model/RF_classification.ipynb
Contains a notebook explaining how the model was designed, including its validation, training and testing. It can also be used to train the model with new or selected data.

### utils/data_Augmentation_CLIMAX.ipynb
Contains a notebook explaining the data augmentation techniques used for generating artificial training data from real data.


# Demo
Here's how to run a demo using your webcam.
```bash
python app.py
```
