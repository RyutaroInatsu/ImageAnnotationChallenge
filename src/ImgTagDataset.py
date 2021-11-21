import os

import albumentations as alb
import numpy as np
import pandas as pd
import pytorch_lightning as pl
import torch
from PIL import Image
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms


class ImgTagDataset(Dataset):
    """
    Create dataset for multi-label classification.

    Parameters
    ----------------
    df : pd.DataFrame
        Pandas DataFrame object.
        it must be contained "directory", "filename", and one-hot encoded columns.

    root_path: str
        root path of Datasets
    """

    def __init__(self, root_path, transform):
        self.root_path = root_path
        self.transform = transform

    def __len__(self):
        return len(self.df)

    def __getitem__(self, index):
        d = self.df.iloc[index]
        image = Image.open(
            os.path.join(self.root_path, d["directory"], d["filename"])
        ).convert("RGB")
        image = self.transform(image=np.squeeze(image))["image"]
        label = torch.tensor(d[2:].tolist(), dtype=torch.float32)
        return image, label


class ImgTagDataModule(pl.LightningDataModule):
    def __init__(
        self,
        train_val_root_dir: str,
        test_root_dir: str,
        batch_size=32,
        img_size=224,
        mean=(0.485, 0.456, 0.406),
        std=(0.229, 0.224, 0.225),
    ):

        super().__init__()
        self.train_val_root_dir = train_val_root_dir
        self.test_root_dir = test_root_dir
        self.batch_size = batch_size

        self.train_ds = None
        self.val_ds = None
        self.test_ds = None

        # pre-processing
        self.train_transforms = alb.Compose(
            [
                alb.RandomResizedCrop(
                    width=img_size, height=img_size, scale=(0.5, 1.0)
                ),
                alb.RandomBrightnessContrast(
                    brightness_limit=0.1, contrast_limit=0.2, p=0.5
                ),
                alb.ImageCompression(quality_lower=90, quality_upper=100, p=0.5),
                alb.GaussianBlur(blur_limit=(1, 3)),
                alb.CLAHE(clip_limit=6.0, tile_grid_size=(8, 8), p=1),
                alb.HorizontalFlip(),
                alb.Normalize(mean, std),
            ]
        )

        self.val_test_transforms = transforms.Compose(
            [
                transforms.Resize(img_size),
                transforms.CenterCrop(img_size),
                transforms.ToTensor(),
                transforms.Normalize(mean=mean, std=std),
            ]
        )

    def prepare_data(self):
        pass

    def split_train_val_df(self, df):
        train_df, val_df = train_test_split(df, test_size=0.2)
        return train_df, val_df

    # Trainer.fit()ではtrain/valのDatasetを、Trainer.test()ではtestのDatasetを生成
    def setup(self, stage=None):
        if stage == 'fit' or stage is None:
            df = pd.read_csv(os.path.join(self.train_val_root_dir, "label.csv"))
            df = df.dropna(axis=1, how="all")  # save memory and process usage
            df = df.fillna("None")  # to avoid error

            mlb = MultiLabelBinarizer()
            result = mlb.fit_transform(df.drop(columns=["directory", "filename"]).values)  # drop not tagging cols

            bin_df = pd.DataFrame(result, columns=mlb.classes_).drop("None", axis=1)  # drop non-useless col.
            bin_df = df.drop(df.columns[2:], axis=1).join(bin_df)

            train_df, val_df = self.split_train_val_df(bin_df)
            self.train_ds = ImgTagDataset(train_df, self.train_val_root_dir, self.train_transforms)
            self.val_ds = ImgTagDataset(val_df, self.train_val_root_dir, self.val_test_transforms)

        if stage == 'test' or stage is None:
            test_df = pd.read_csv(os.path.join(self.test_root_dir, "label.csv"))
            self.test_ds = ImgTagDataset(test_df, self.test_root_dir, self.val_test_transforms)

    def train_dataloader(self):
        return DataLoader(self.train_dataset, batch_size=self.batch_size, shuffle=True, num_workers=8, pin_memory=True)

    def val_dataloader(self):
        return DataLoader(self.val_dataset, batch_size=self.batch_size, num_workers=8, pin_memory=True)

    def test_dataloader(self):
        return DataLoader(self.test_dataset, batch_size=self.batch_size, num_workers=8, pin_memory=True)
