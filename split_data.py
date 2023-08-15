import os
import random
import shutil

# Set the paths for the input data
image_folder = # đường dẫn đến file image cần chia
label_folder = # đường dẫn đến file label cần chia

# Set the paths for the output data
output_folder = " "

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Create the train and test folders within the output folder
train_folder = os.path.join(output_folder, "train")
test_folder = os.path.join(output_folder, "test")
os.makedirs(train_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)

# Create the image and label folders within the train and test folders
train_image_folder = os.path.join(train_folder, "images")
train_label_folder = os.path.join(train_folder, "labels")
os.makedirs(train_image_folder, exist_ok=True)
os.makedirs(train_label_folder, exist_ok=True)

test_image_folder = os.path.join(test_folder, "images")
test_label_folder = os.path.join(test_folder, "labels")
os.makedirs(test_image_folder, exist_ok=True)
os.makedirs(test_label_folder, exist_ok=True)

# Get the list of files in the image folder
image_files = os.listdir(image_folder)

# Shuffle the file list randomly
random.shuffle(image_files)

# Calculate the split index for the train-test split
split_index = int(0.5 * len(image_files)) ## tỉ lệ phần trăm khi chia file, như ở đây là 50 50

# Split the file list into train and test sets
train_files = image_files[:split_index]
test_files = image_files[split_index:]

# Copy image files to the train folder
for file in train_files:
    # Check for variations in file extensions
    base_filename, ext = os.path.splitext(file)
    ext = ext.lower()

    if ext in [".jpg", ".jpeg"]:
        image_src = os.path.join(image_folder, file)
        image_dst = os.path.join(train_image_folder, file)
        shutil.copy(image_src, image_dst)

        # Assuming label files have the same name as image files
        label_src = os.path.join(label_folder, base_filename + ".txt")
        label_dst = os.path.join(train_label_folder, base_filename + ".txt")
        shutil.copy(label_src, label_dst)

# Copy image files to the test folder
for file in test_files:
    # Check for variations in file extensions
    base_filename, ext = os.path.splitext(file)
    ext = ext.lower()

    if ext in [".jpg", ".jpeg",".JPG"]:
        image_src = os.path.join(image_folder, file)
        image_dst = os.path.join(test_image_folder, file)
        shutil.copy(image_src, image_dst)

        # Assuming label files have the same name as image files
        label_src = os.path.join(label_folder, base_filename + ".txt")
        label_dst = os.path.join(test_label_folder, base_filename + ".txt")
        shutil.copy(label_src, label_dst)

# Print the summary
print(f"Train set: {len(train_files)} images")
print(f"Test set: {len(test_files)} images")