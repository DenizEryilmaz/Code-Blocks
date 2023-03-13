import os
import random
from glob import glob
from shutil import copyfile

# Define the paths to your original data
data_path = '/content/dataset/dataset'
tb_path = os.path.join(data_path, 'tb')
normal_path = os.path.join(data_path, 'normal')

# Define the paths to your new train and test data
train_path = os.path.join(data_path, 'train')
test_path = os.path.join(data_path, 'test')

# Define the percentage of data you want to use for training
train_percent = 0.8

# Create the train and test directories if they don't exist
os.makedirs(train_path, exist_ok=True)
os.makedirs(test_path, exist_ok=True)

# Iterate through the tb and normal folders
for class_path in [tb_path, normal_path]:
    # Get all image paths for the current class
    image_paths = glob(os.path.join(class_path, '*.png'))

    # Shuffle the image paths
    random.shuffle(image_paths)

    # Split the image paths into train and test sets
    num_train = int(len(image_paths) * train_percent)
    train_image_paths = image_paths[:num_train]
    test_image_paths = image_paths[num_train:]

    # Copy the train images to the train directory
    for image_path in train_image_paths:
        class_name = os.path.basename(os.path.dirname(image_path))
        file_name = os.path.basename(image_path)
        new_path = os.path.join(train_path, class_name, file_name)
        os.makedirs(os.path.join(train_path, class_name), exist_ok=True)
        copyfile(image_path, new_path)

    # Copy the test images to the test directory
    for image_path in test_image_paths:
        class_name = os.path.basename(os.path.dirname(image_path))
        file_name = os.path.basename(image_path)
        new_path = os.path.join(test_path, class_name, file_name)
        os.makedirs(os.path.join(test_path, class_name), exist_ok=True)
        copyfile(image_path, new_path)
