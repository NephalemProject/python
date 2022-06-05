import cv2
import numpy as np

data = np.load("D:/Nephalem/Documents/uniteTrainingData/training_data.npy", allow_pickle=True)
targets = np.load("D:/Nephalem/Documents/uniteTrainingData/target_data.npy", allow_pickle=True)

print(f'Image Data Shape: {data.shape}')
print(f'targets Shape: {targets.shape}')

# Lets see how many of each type of move we have.
unique_elements, counts = np.unique(targets, return_counts=True)
print(np.asarray((unique_elements, counts)))

# Store both data and targets in a list.
# We may want to shuffle down the road.

holder_list = []
for i, image in enumerate(data):
    holder_list.append([data[i], targets[i]])

count_up = 0
count_left = 0
count_right = 0
count_down = 0
count_move01 = 0
count_move02 = 0
count_attack = 0

for data in holder_list:
    #print(data[1])
    if data[1] == 'W':
        count_up += 1
        cv2.imwrite(f"D:/Nephalem/Documents/uniteTrainingData/createImages/Up/H2-u{count_up}.png", data[0])
    elif data[1] == 'A':
        count_left += 1
        cv2.imwrite(f"D:/Nephalem/Documents/uniteTrainingData/createImages/Left/H2-l{count_left}.png", data[0])
    elif data[1] == 'D':
        count_right += 1
        cv2.imwrite(f"D:/Nephalem/Documents/uniteTrainingData/createImages/Right/H2-r{count_right}.png", data[0])
    elif data[1] == 'S':
        count_down += 1
        cv2.imwrite(f"D:/Nephalem/Documents/uniteTrainingData/createImages/Down/H2-d{count_down}.png", data[0])
    elif data[1] == 'E':
        count_attack += 1
        cv2.imwrite(f"D:/Nephalem/Documents/uniteTrainingData/createImages/Attack/H2-a{count_attack}.png", data[0])
    elif data[1] == 'Q':
        count_move01 += 1
        cv2.imwrite(f"D:/Nephalem/Documents/uniteTrainingData/createImages/Move01/H2-m{count_move01}.png", data[0])
    elif data[1] == 'F':
        count_move01 += 1
        cv2.imwrite(f"D:/Nephalem/Documents/uniteTrainingData/createImages/Move02/H2-mm{count_move02}.png", data[0])
