import io

# import albumentations as alb
# import numpy as np
import torch

# from albumentations.pytorch import ToTensorV2
from PIL import Image
from transformers import BeitFeatureExtractor, BeitModel

from imgtag.ImgTagLitModule import BeiTNet

IMG_SIZE = 224


def get_model(class_num):
    # set up model
    beit_model = BeitModel.from_pretrained(
        "microsoft/beit-base-patch16-224-pt22k-ft22k"
    )
    model = BeiTNet(beit_model, class_num)
    model.load_state_dict(torch.load("./static/screw_beit_model.pt"))
    model.eval()
    return model


def transform_image(image_bytes):
    beit_feature_extractor = BeitFeatureExtractor.from_pretrained(
        "microsoft/beit-base-patch16-224-pt22k-ft22k"
    )
    # augmentation = alb.Compose(
    #     [
    #         alb.Resize(height=IMG_SIZE, width=IMG_SIZE),
    #         # alb.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5)),
    #         ToTensorV2(),
    #     ]
    # )
    image = Image.open(io.BytesIO(image_bytes))
    # image = augmentation(image=np.squeeze(image))["image"]
    image = beit_feature_extractor(images=image, return_tensors="pt")[
        "pixel_values"
    ].squeeze(0)
    # image = np.clip(image, 0, 1)
    return image.unsqueeze(0)
