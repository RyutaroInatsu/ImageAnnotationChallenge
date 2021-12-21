import io

import albumentations as alb
import numpy as np
import torch
from albumentations.pytorch import ToTensorV2
from imgtag.ImgTagLitModule import ViTNet
from PIL import Image
from transformers import ViTModel

IMG_SIZE = 224


def get_model(class_num):
    # set up model
    vit_model = ViTModel.from_pretrained(
        "google/vit-base-patch16-224-in21k", output_attentions=True
    )
    model = ViTNet(vit_model, class_num)
    # model.load_state_dict(torch.load("./static/vit_model.pt"))
    model.load_state_dict(torch.load("./static/screw_vit_model.pt"))
    model.eval()
    return model


def transform_image(image_bytes):
    augmentation = alb.Compose(
        [
            alb.Resize(height=IMG_SIZE, width=IMG_SIZE),
            alb.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5)),
            ToTensorV2(),
        ]
    )
    image = Image.open(io.BytesIO(image_bytes))
    image = augmentation(image=np.squeeze(image))["image"]
    image = np.clip(image, 0, 1)
    return image.unsqueeze(0)
