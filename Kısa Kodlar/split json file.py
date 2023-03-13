import json

with open('/content/tb_newdataset/tb_newdataset/_annotations.coco.json', 'r') as f:
    dataset_dict = json.load(f)


def split_dataset(dataset_dict, train_ratio=0.8):
    train_dict = {}
    val_dict = {}
    images = dataset_dict['images']
    annotations = dataset_dict['annotations']
    categories = dataset_dict['categories']

    train_images = images[:int(train_ratio * len(images))]
    val_images = images[int(train_ratio * len(images)):]

    train_dict['images'] = train_images
    val_dict['images'] = val_images

    train_annotations = []
    val_annotations = []
    for annotation in annotations:
        if annotation['image_id'] in [x['id'] for x in train_images]:
            train_annotations.append(annotation)
        else:
            val_annotations.append(annotation)

    train_dict['annotations'] = train_annotations
    val_dict['annotations'] = val_annotations

    train_dict['categories'] = categories
    val_dict['categories'] = categories

    return train_dict, val_dict


train_dict, val_dict = split_dataset(dataset_dict, train_ratio=0.8)

with open('train.json', 'w') as f:
    json.dump(train_dict, f)

with open('val.json', 'w') as f:
    json.dump(val_dict, f)
import json

train_file = "/content/tb_newdataset/train.json"
val_file = "/content/tb_newdataset/val.json"

with open(train_file) as f:
    train_data = json.load(f)

with open(val_file) as f:
    val_data = json.load(f)

num_train_images = len(train_data["images"])
num_train_annotations = len(train_data["annotations"])
num_val_images = len(val_data["images"])
num_val_annotations = len(val_data["annotations"])

print("Number of training images:", num_train_images)
print("Number of training annotations:", num_train_annotations)
print("Number of validation images:", num_val_images)
print("Number of validation annotations:", num_val_annotations)