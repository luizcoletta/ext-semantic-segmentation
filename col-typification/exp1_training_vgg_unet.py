from keras_segmentation.models.unet import vgg_unet

### Training

### real image size: 960x720 (ratio -> 4:3), but 720/32 is inexact!
### type size 1: 960x704, both division by 32 is exact
### type size 2: 960x736, both division by 32 is exact

#model = vgg_unet(n_classes=10, input_width=960, input_height=768)
#model = vgg_unet(n_classes=10, input_width=480, input_height=384)
model = vgg_unet(n_classes=6, input_width=192, input_height=160)

model.train(
    train_images = "data/dataset_tipificacao_v1/images_train/",
    train_annotations = "data/dataset_tipificacao_v1/annotations_train/",
    checkpoints_path = "saved_models/vgg_unet/vgg_unet_1", epochs=20)