"""VOC Dataset Classes

Original author: Francisco Massa
https://github.com/fmassa/vision/blob/voc_dataset/torchvision/datasets/voc.py

Updated by: Ellis Brown, Max deGroot
"""
"""
Copyright (c) 2017 Max deGroot, Ellis Brown
Released under the MIT license
https://github.com/amdegroot/ssd.pytorch
Updated by: Takuya Mouri
"""
from .config import HOME
import os.path as osp
import sys
import torch
import torch.utils.data as data
import cv2
import numpy as np
if sys.version_info[0] == 2:
    import xml.etree.cElementTree as ET
else:
    import xml.etree.ElementTree as ET

'''
VOC_CLASSES = (  # always index 0
    'aeroplane', 'bicycle', 'bird', 'boat',
    'bottle', 'bus', 'car', 'cat', 'chair',
    'cow', 'diningtable', 'dog', 'horse',
    'motorbike', 'person', 'pottedplant',
    'sheep', 'sofa', 'train', 'tvmonitor')
'''

## TODO::kobo
VOC_CLASSES = (  # always index 0
   'zoom','search','orientation_n','voice','more_options','flag','delete',
   'return','suggestions','cap_q','cap_w','cap_e','cap_r','cap_t','cap_y','cap_u',
   'cap_i','cap_o','cap_p','cap_a','cap_s','cap_d','cap_f','cap_g','cap_h',
   'cap_j','cap_k','cap_l','cap_z','cap_x','cap_c','cap_v','cap_b','cap_n','cap_m',
   'menu_map_1','menu_audio_1','menu_phone_1','menu_apps_1',
   'menu_info_1','menu_setup_1','menu_display_1','source',
   'am','fm','dab','usb','bluetooth','mircast','reorder','incar','estore',
   'media','coyote','pause_guidance','traffic','fuel','parking','route',
   'zoom','search','orientation','voice_on','more','on_route','all',
   'detoured','back','up','down','voice_off','orientation_3d','orientation_2d',
   'zoom','zoom_in','zoom_out','zoom_scale','menu_map_2','menu_audio_2',
   'menu_phone_2','menu_apps_2','menu_info_2','menu_setup_2','menu_display_2',
   'dash','invshift','change_type','input_entry','space','search',
   'detour_menu','phone_bar','actual_position')

# handbook
# note: if you used our download scripts, this should be right
#VOC_ROOT = osp.join(HOME, "data/VOCdevkit/")
# 現在のディレクトリを取得
dir_cur = osp.dirname(__file__)
# データセットVOCのディレクトリを取得
dir_voc = osp.join(dir_cur, "..", "VOCdevkit")
# データセットVOCの絶対パスを設定
VOC_ROOT = osp.abspath(dir_voc)
# handbook

class VOCAnnotationTransform(object):
    """Transforms a VOC annotation into a Tensor of bbox coords and label index
    Initilized with a dictionary lookup of classnames to indexes

    Arguments:
        class_to_ind (dict, optional): dictionary lookup of classnames -> indexes
            (default: alphabetic indexing of VOC's 20 classes)
        keep_difficult (bool, optional): keep difficult instances or not
            (default: False)
        height (int): height
        width (int): width
    """

    def __init__(self, class_to_ind=None, keep_difficult=False):
        self.class_to_ind = class_to_ind or dict(
            zip(VOC_CLASSES, range(len(VOC_CLASSES))))
        self.keep_difficult = keep_difficult

    def __call__(self, target, width, height):
        """
        Arguments:
            target (annotation) : the target annotation to be made usable
                will be an ET.Element
        Returns:
            a list containing lists of bounding boxes  [bbox coords, class name]
        """



        res = []
        for obj in target.iter('object'):
            difficult = int(obj.find('difficult').text) == 1
            if not self.keep_difficult and difficult:
                continue

            name = obj.find('name').text.lower().strip()
            bbox = obj.find('bndbox')

            pts = ['xmin', 'ymin', 'xmax', 'ymax']
            bndbox = []
            for i, pt in enumerate(pts):
                cur_pt = int(bbox.find(pt).text) - 1
                # scale height or width
                #xmin,xmaxはwidth、ymin,ymaxはheightで割る
                cur_pt = cur_pt / width if i % 2 == 0 else cur_pt / height
                # bndboxに正解座標をセット
                bndbox.append(cur_pt)


            label_idx = self.class_to_ind[name]
            # 正解座標の後に正解ラベルのインデックスをセット
            bndbox.append(label_idx)
            res += [bndbox]  # [xmin, ymin, xmax, ymax, label_ind]
            # img_id = target.find('filename').text[:-4]
        # 1画像に複数物体あるので、[物体数,[bndbox]]のリストを作成する
        return res  # [[xmin, ymin, xmax, ymax, label_ind], ... ]


class VOCDetection(data.Dataset):
    """VOC Detection Dataset Object

    input is image, target is annotation

    Arguments:
        root (string): filepath to VOCdevkit folder.
        image_set (string): imageset to use (eg. 'train', 'val', 'test')
        transform (callable, optional): transformation to perform on the
            input image
        target_transform (callable, optional): transformation to perform on the
            target `annotation`
            (eg: take in caption string, return tensor of word indices)
        dataset_name (string, optional): which dataset to load
            (default: 'VOC2007')
    """

    def __init__(self, root,
                # handbook
                ## TODO::kobo
                image_sets=[('2019', 'trainval')],
                ## org## image_sets=[('2007', 'trainval'), ('2012', 'trainval')],
                #image_sets=[('2007', 'trainval')],
                # handbook
                transform=None, target_transform=VOCAnnotationTransform(),
                dataset_name='VOC0712'):
        self.root = root
        self.image_set = image_sets
        self.transform = transform
        self.target_transform = target_transform

        self.name = dataset_name
        self._annopath = osp.join('%s', 'Annotations', '%s.xml')
        self._imgpath = osp.join('%s', 'JPEGImages', '%s.jpg')
        self.ids = list()
        for (year, name) in image_sets:
            rootpath = osp.join(self.root, 'VOC' + year)
            for line in open(osp.join(rootpath, 'ImageSets', 'Main', name + '.txt')):
                self.ids.append((rootpath, line.strip()))

    def __getitem__(self, index):
        im, gt, h, w = self.pull_item(index)

        return im, gt

    def __len__(self):
        return len(self.ids)

    def pull_item(self, index):

        img_id = self.ids[index]
        target = ET.parse(self._annopath % img_id).getroot()
        img = cv2.imread(self._imgpath % img_id)
        height, width, channels = img.shape

        if self.target_transform is not None:
            target = self.target_transform(target, width, height)

        if self.transform is not None:
            target = np.array(target)
            img, boxes, labels = self.transform(img, target[:, :4], target[:, 4])
            # to rgb
            # cv2のchannelsはbgrなのでrgbの順番に変更
            img = img[:, :, (2, 1, 0)]
            # img = img.transpose(2, 0, 1)
            target = np.hstack((boxes, np.expand_dims(labels, axis=1)))
        # 画像の次元の順番をHWCからCHWに変更
        return torch.from_numpy(img).permute(2, 0, 1), target, height, width
        # return torch.from_numpy(img), target, height, width

    def pull_image(self, index):
        '''Returns the original image object at index in PIL form

        Note: not using self.__getitem__(), as any transformations passed in
        could mess up this functionality.

        Argument:
            index (int): index of img to show
        Return:
            PIL img
        '''
        img_id = self.ids[index]
        return cv2.imread(self._imgpath % img_id, cv2.IMREAD_COLOR)

    def pull_anno(self, index):
        '''Returns the original annotation of image at index

        Note: not using self.__getitem__(), as any transformations passed in
        could mess up this functionality.

        Argument:
            index (int): index of img to get annotation of
        Return:
            list:  [img_id, [(label, bbox coords),...]]
                eg: ('001718', [('dog', (96, 13, 438, 332))])
        '''
        img_id = self.ids[index]
        anno = ET.parse(self._annopath % img_id).getroot()
        gt = self.target_transform(anno, 1, 1)
        return img_id[1], gt

    def pull_tensor(self, index):
        '''Returns the original image at an index in tensor form

        Note: not using self.__getitem__(), as any transformations passed in
        could mess up this functionality.

        Argument:
            index (int): index of img to show
        Return:
            tensorized version of img, squeezed
        '''
        return torch.Tensor(self.pull_image(index)).unsqueeze_(0)
