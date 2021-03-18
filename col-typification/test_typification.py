import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
import numpy as np

from keras_segmentation.models.unet import vgg_unet
from keras_segmentation.metrics import get_iou

#model = vgg_unet(n_classes=10,  input_height=768, input_width=960)
#model = vgg_unet(n_classes=10,  input_height=384, input_width=480)
model = vgg_unet(n_classes=6,  input_height=192, input_width=256)

#https://www.tensorflow.org/tutorials/keras/save_and_load
latest = tf.train.latest_checkpoint('saved_models/vgg_unet/')
model.load_weights(latest)

#### Using Intersection over Union (IoU) measure for each class
#### Average IoU is equal to TP/(FN + TP + FP)

test_number = 144

test_img = "data/dataset_tipificacao_v1/images_test/" + str(test_number) + ".png"
test_gt = "data/dataset_tipificacao_v1/annotations_test/" + str(test_number) + ".png"
num_classes = 4

out = model.predict_segmentation(
    inp=test_img,
    out_fname="/results/out.png"
)

gt = cv2.imread(test_gt, 0)
gt = cv2.resize(gt, (480, 384))

fig = plt.figure()
fig.suptitle('Ground of Truth (Annotated Classes)', fontsize=16)
plt.imshow(gt)
fig = plt.figure()
fig.suptitle('Predicted Classes', fontsize=16)
plt.imshow(out)

### https://fairyonice.github.io/Learn-about-Fully-Convolutional-Networks-for-semantic-segmentation.html
iou = get_iou(gt, out, num_classes)
mean_iou = sum(iou)/num_classes

print("IoU per class:", np.round(iou, 4))
print("Mean IoU:", round(mean_iou, 4))


