# HID2020 Gaitset
## 1 datasets
put the train dataset into __dataset/train__  
put the test probe dataset into __dataset/test_probe__  
put the test gallery dataset into __dataset/test_gallery__  
## 2 pretreatment
pretreat the dataset by cut image to size 64X64  
```
# train dataset
python pretreatment.py --input_path dataset/train --output_path dataset/train_pre
# probe dataset
python pretreatment.py --input_path dataset/test_probe --output_path dataset/test_probe_pre
# gallery dataset
python pretreatment.py --input_path dataset/test_gallery --output_path dataset/test_gallery_pre
```
## 3 train model
you can check and modify the basic information in config.py 
```
python train.py
```
the model will save at __work/checkpoint/__
## 4 test and generate submission.csv
move the best model into __work/weights/__ and then
```
python test.py
```
the submission.csv will save at __work/submission.csv__
