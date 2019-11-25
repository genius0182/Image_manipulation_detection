import os


if __name__ == '__main__':
    target_path = './data/DIY_dataset/VOC2007/ImageSets/Main/trainval.txt'
    src_path = './data/DIY_dataset/VOC2007/JPEGImages/'
    for root, dirs, files in os.walk(src_path):
        for file in files:
            with open(target_path, 'a') as f:
                f.write('\n'+os.path.splitext(file)[0])
                f.close()
