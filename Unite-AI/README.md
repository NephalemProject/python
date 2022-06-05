## About
This project was intended to test machine learning on the recently released mobile MOBA game Pokemon Unite by recording a human playing and then attempting to learn when to perform what action.

## Setup
- You can start data collection by running CreateData.py
- Pressing B will start the screen / key grab. These will be stored in lists until the episode is done.
- Once the episode ( Round ) ends pressing h will stop the screen / key grab process and all data will be moved to a numpy array.
- Then I used a script in util folder called CreateImages.py to put then onto a disk drive in folders corresponding to their actions.

## Train
- Use the file called training.py
- Point it at your image directory
- I trained my AI using Google Colab

## Run Agents
- Fully random agent is RandomAgent.py, i.e. chooses random actions.
- Trained Agent is TrainedAgent.py
- You will have to load in the pkl created from training.

## Early Showcase
Here is a very early demo of the model after approximately 3 games of training:
https://youtu.be/9ngkaWZ5yWg
