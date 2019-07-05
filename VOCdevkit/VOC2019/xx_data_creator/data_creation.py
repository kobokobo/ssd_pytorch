#-*- coding:utf-8 -*-

from pascal_voc_writer import Writer
import random
import glob, os
import cv2
background_images_files = glob.glob("./00_background/*.jpg")

IMG_H = 480
IMG_W = 640

i = 1

# trainval
path_w = '../ImageSets/Main/trainval.txt'

for k in range(100):
    for bgimg in background_images_files:
        
        # make output file name
        zero_i = "{0:06d}".format(i)
        new_img_name = "../JPEGImages/"+zero_i+".jpg"
        print(bgimg + "→" + new_img_name)
        
        with open(path_w, mode='a') as f:
            f.write(zero_i+"\n")

        # VOC annotation format
        writer = Writer(bgimg, IMG_W, IMG_H)
        #print(bgimg)
        # read background image        
        base_img = cv2.imread(bgimg)
        base_img =cv2.resize(base_img,(IMG_W,IMG_H))
        
        if '000001.jpg' in bgimg:
            writer.addObject('zoom', 7, 92, 53, 144)
            writer.addObject('search', 5, 156, 51, 204)
            writer.addObject('orientation_n', 5, 216, 52, 266)
            writer.addObject('voice', 6, 281, 52, 328)
            writer.addObject('more_options', 7, 338, 50, 387)
            writer.addObject('detour_menu',556,180,636,470)
            writer.addObject('phone_bar',485,9,636,54)
            writer.addObject('actual_position',272,204,333,287)
        
        if '000002.jpg' in bgimg:
            writer.addObject('cap_q',22 ,230 ,53 ,264)
            writer.addObject('cap_w',81 ,229 ,118 ,266)
            writer.addObject('cap_e',151, 230 ,179 ,264)
            writer.addObject('cap_r',216, 228, 239 ,266)
            writer.addObject('cap_t',277, 229 ,304, 264)
            writer.addObject('cap_y',338 ,227, 367 ,264)
            writer.addObject('cap_u',401,228,431,263)
            writer.addObject('cap_i',463,228,488,266)
            writer.addObject('cap_o',525,228,556,266)
            writer.addObject('cap_p',592,228,617,266)
            writer.addObject('cap_a',56,279,86,313)
            writer.addObject('cap_s',118,279,145,313)
            writer.addObject('cap_d',181,279,210,313)
            writer.addObject('cap_f',246,279,271,313)
            writer.addObject('cap_g',306,279,337,313)
            writer.addObject('cap_h',368,279,400,313)
            writer.addObject('cap_j',432,279,457,313)
            writer.addObject('cap_k',494,279,524,313)
            writer.addObject('cap_l',558,279,589,313)
            writer.addObject('cap_z',86,328,117,363)
            writer.addObject('cap_x',151,328,180,363)
            writer.addObject('cap_c',212,328,243,363)
            writer.addObject('cap_v',274,328,304,363)
            writer.addObject('cap_b',337,328,365,363)
            writer.addObject('cap_n',400,328,430,363)
            writer.addObject('cap_m',463,328,493,363)
            writer.addObject('flag',214 ,97, 263 ,135)
            writer.addObject('delete',526, 103, 565 ,129)
            writer.addObject('return',586 ,99, 624 ,134)
            writer.addObject('suggestions',583 ,154, 621 ,191)
            writer.addObject('dash',516,329,566,365)
            writer.addObject('invshift',580,328,630,366)
            writer.addObject('change_type',11,407,149,455)
            writer.addObject('input_entry',252,404,319,453)
            writer.addObject('space',329,406,407,453)
            writer.addObject('search',506,407,634,455)

        if '000003.jpg' in bgimg:
            writer.addObject('menu_map_1',48,95,167,244)
            writer.addObject('menu_audio_1',194,95,310,244)
            writer.addObject('menu_phone_1',335,95,451,244)
            writer.addObject('menu_apps_1',479,95,594,244)
            writer.addObject('menu_info_1',50,276,167,423)
            writer.addObject('menu_setup_1',194,276,309,423)
            writer.addObject('menu_display_1',491,440,586,471)

        if '000004.jpg' in bgimg:
            writer.addObject('source',5,95,185,144)
            writer.addObject('am',240,108,339,227)
            writer.addObject('fm',368,108,466,227)
            writer.addObject('dab',497,108,598,227)
            writer.addObject('usb',240,253,340,371)
            writer.addObject('bluetooth',368,253,470,371)
            writer.addObject('mircast',495,253,600,371)
            writer.addObject('reorder',335,405,504,452)

        if '000005.jpg' in bgimg:
            writer.addObject('incar',3,69,187,118)
            writer.addObject('estore',214,113,310,245)
            writer.addObject('media',348,113,443,245)
            writer.addObject('coyote',478,113,577,245)

        if '000006.jpg' in bgimg:
            writer.addObject('pause_guidance',6,89,175,143)
            writer.addObject('traffic',5,154,175,195)
            writer.addObject('fuel',7,211,99,255)
            writer.addObject('parking',6,277,134,322)
            writer.addObject('route',7,336,127,385)
            writer.addObject('zoom',203,94,243,144)
            writer.addObject('search',203,158,244,203)
            writer.addObject('orientation_N',204,217,243,267)
            writer.addObject('voice_on',204,279,242,327)
            writer.addObject('more',200,338,245,387)
            writer.addObject('actual_position',410,201,479,287)

        if '000007.jpg' in bgimg:
            writer.addObject('on_route',13,90,182,139)
            writer.addObject('all',203,90,371,139)
            writer.addObject('detoured',391,90,556,139)
            writer.addObject('back',576,90,632,139)
            writer.addObject('up',605,160,625,191)
            writer.addObject('down',605,424,626,457)

        if '000008.jpg' in bgimg:
            writer.addObject('voice_off',6, 281, 52, 328)
            writer.addObject('zoom', 7, 92, 53, 144)
            writer.addObject('search', 5, 156, 51, 204)
            writer.addObject('orientation', 5, 216, 52, 266)
            writer.addObject('more_options', 7, 338, 50, 387)
            writer.addObject('actual_position',272,204,333,287)
            
        if '000009.jpg' in bgimg:
            writer.addObject('orientation_3d', 5, 216, 52, 266)
            writer.addObject('zoom', 7, 92, 53, 144)
            writer.addObject('search', 5, 156, 51, 204)
            writer.addObject('voice', 6, 281, 52, 328)
            writer.addObject('more_options', 7, 338, 50, 387)
            writer.addObject('actual_position',269,288,333,340)

        if '000010.jpg' in bgimg:
            writer.addObject('orientation_2d', 5, 216, 52, 266)
            writer.addObject('zoom', 7, 92, 53, 144)
            writer.addObject('search', 5, 156, 51, 204)
            writer.addObject('voice', 6, 281, 52, 328)
            writer.addObject('more_options', 7, 338, 50, 387)
            writer.addObject('actual_position',268,275,335,367)

        if '000011.jpg' in bgimg:
            writer.addObject('zoom', 7, 92, 53, 144)
            writer.addObject('zoom_in',5,153,49,211)
            writer.addObject('zoom_out',8,385,50,420)
            writer.addObject('zoom_scale',6,218,52,379)
            writer.addObject('actual_position',264,198,337,292)

        if '000012.jpg' in bgimg:
            writer.addObject('menu_map_2',81,59,135,185)
            writer.addObject('menu_audio_2',227,59,279,185)
            writer.addObject('menu_phone_2',363,59,424,185)
            writer.addObject('menu_apps_2',505,59,563,185)
            writer.addObject('menu_info_2',86,263,135,391)
            writer.addObject('menu_setup_2',226,263,277,391)
            writer.addObject('menu_display_2',489,434,586,471)
        
        new_anot_name = "../Annotations/"+zero_i+".xml"
        writer.save(new_anot_name)
        cv2.imwrite(new_img_name, base_img)
        i += 1

