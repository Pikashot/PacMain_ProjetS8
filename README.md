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
    │   data_Augmentation_CLIMAX.ipynb
    │   key_code_index.txt
    │   read_keyboard_keys.py
    │   select_rows.py
    │   __init__.py
</pre>

# Demo
Here's how to run a demo using your webcam.
```bash
python app.py
```
