#-*- coding:utf-8 -*-
import cv2
from pascal_voc_writer import Writer
import random
import glob, os

background_images_files = glob.glob("./00_background/*.jpg")
icon_images_files = glob.glob("./01_icon/*.PNG")


IMG_H = 480
IMG_W = 640
ICON_H = 60
ICON_W = 60

i = 1

# trainval
path_w = '../ImageSets/Main/trainval.txt'

for k in range(100):
    for bgimg in background_images_files:
        # make output file name
        zero_i = "{0:06d}".format(i)
        new_img_name = "../JPEGImages/"+zero_i+".jpg"
        print(bgimg + "→" + new_img_name)
        i += 1
        with open(path_w, mode='a') as f:
            f.write(zero_i+"\n")


        # VOC annotation format
        writer = Writer(bgimg, IMG_W, IMG_H)

        # read background image
        base_img = cv2.imread(bgimg)
        base_img =cv2.resize(base_img,(IMG_W,IMG_H))
        large_img = base_img

        for iconimg in icon_images_files:

            icon_img = cv2.imread(iconimg)
            num_icon = random.randrange(3) + 1

            icon_name_temp = os.path.basename(iconimg)
            icon_name, ext = os.path.splitext(icon_name_temp)

            for j in range(num_icon):

                x_offset = random.randrange(100, 540, 1)  # 100-540
                y_offset = random.randrange(100, 380, 1)  # 100-380
                scale = random.uniform(0.6, 1.2)  # 0.3 - 1.0

                icon_img = cv2.resize(icon_img, (int(ICON_W * scale), int(ICON_H * scale)))

                # synthetic iamge creation
                small_img = icon_img
                large_img[y_offset:y_offset + small_img.shape[0], x_offset:x_offset + small_img.shape[1]] = small_img

                # annotation
                writer.addObject(icon_name, x_offset, y_offset, (x_offset + small_img.shape[1]), (y_offset + small_img.shape[0]))


        new_anot_name = "../Annotations/"+zero_i+".xml"
        writer.save(new_anot_name)
        cv2.imwrite(new_img_name, large_img)

'''
        # for debug
        cv2.imshow("input", large_img)
        cv2.waitKey(3000)


cv2.waitKey(1)
cv2.destroyAllWindows()
cv2.waitKey(1)
'''