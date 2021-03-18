#!/bin/bash

echo '*** UPLOADING FILES...'

scp -P 780 col-typification.zip root@200.145.54.25:/home/lcoletta
#scp -P 780 col-object-detection/run_experiments.py root@200.145.54.25:/home/lcoletta/col-object-detection/run_experiments.py
#scp -P 780 col-object-detection/exp1_training_vgg_unet.py root@200.145.54.25:/home/lcoletta/col-object-detection/exp1_training_vgg_unet.py

echo 'Done!!!'

