from albumentations import (
    HorizontalFlip, IAAPerspective, ShiftScaleRotate, CLAHE, RandomRotate90,
    Transpose, ShiftScaleRotate, Blur, OpticalDistortion, GridDistortion, HueSaturationValue,
    IAAAdditiveGaussianNoise, GaussNoise, MotionBlur, MedianBlur, IAAPiecewiseAffine,
    IAASharpen, IAAEmboss, RandomBrightnessContrast, Flip, OneOf, Compose
)
import numpy as np

def strong_aug(p=0.5):
    return Compose([
        RandomRotate90(),
        Flip(),
        Transpose(),
        OneOf([
            IAAAdditiveGaussianNoise(),
            GaussNoise(),
        ], p=0.2),
        OneOf([
            MotionBlur(p=0.2),
            MedianBlur(blur_limit=3, p=0.1),
            Blur(blur_limit=3, p=0.1),
        ], p=0.2),
        ShiftScaleRotate(shift_limit=0.0625, scale_limit=0.2, rotate_limit=45, p=0.2),
        OneOf([
            OpticalDistortion(p=0.3),
            GridDistortion(p=0.1),
            IAAPiecewiseAffine(p=0.3),
        ], p=0.2),
        OneOf([
            CLAHE(clip_limit=2),
            IAASharpen(),
            IAAEmboss(),
            RandomBrightnessContrast(),
        ], p=0.3),
        HueSaturationValue(p=0.3),
    ], p=p)


img = "/home/rohitgupta/Workspace_edfi/POCs/OCR_yolo/src/utils/pan3.png"
# from PIL import Image
# import numpy as np
#
# pillow_image = Image.open(img)
# image = np.array(pillow_image)

def image_aug(image):
    from PIL import Image
    import numpy as np
    pillow_image = Image.open(img)
    image = np.array(pillow_image)
    # image = np.ones((300, 300, 3), dtype=np.uint8)
    mask = np.ones((300, 300), dtype=np.uint8)
    whatever_data = "my name"
    augmentation = strong_aug(p=0.9)
    data = {"image": image, "mask": mask, "whatever_data": whatever_data, "additional": "hello"}
    augmented = augmentation(**data)
    image, mask, whatever_data, additional = augmented["image"], augmented["mask"], augmented["whatever_data"], augmented["additional"]
    image = Image.fromarray(image, 'RGB')
    image.save('my.png')
    image.show()
    return image

from PIL import Image
import numpy as np



print(image_aug(img))
