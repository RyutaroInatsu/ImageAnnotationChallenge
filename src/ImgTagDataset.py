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
from albumentations.pytorch import ToTensorV2


class ImgTagDataset(Dataset):
    """
    Create dataset for multi-label classification.

    Parameters
    ----------------
    df : pd.DataFrame
        Pandas DataFrame object.
        it must be contained "directory", "filename", and multi-binarized encoded columns.

    root_path: str
        root path of Datasets
    """

    def __init__(self, df: pd.DataFrame, root_path, transform):
        self.df = df
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
        image = np.clip(image, 0, 1)
        label = torch.tensor(d[2:].tolist(), dtype=torch.float32)
        return image, label


class ImgTagDataModule(pl.LightningDataModule):
    def __init__(
        self,
        train_val_root_dir: str,
        test_root_dir: str,
        batch_size=32,
        img_size=224,
        mean=(0.5, 0.5, 0.5),
        std=(0.5, 0.5, 0.5),
    ):

        super().__init__()
        self.train_val_root_dir = train_val_root_dir
        self.test_root_dir = test_root_dir
        self.batch_size = batch_size

        self.train_ds = None
        self.val_ds = None
        self.test_ds = None

        # pre-processing
        self.train_augmentation = alb.Compose(
            [
                alb.RandomResizedCrop(
                    width=img_size, height=img_size, scale=(0.5, 1.0)
                ),
                alb.ShiftScaleRotate(),
                alb.RandomBrightnessContrast(
                    brightness_limit=0.1, contrast_limit=0.2, p=0.5
                ),
                alb.ImageCompression(quality_lower=90, quality_upper=100, p=0.5),
                alb.GaussianBlur(blur_limit=(1, 3)),
                # alb.CLAHE(clip_limit=6.0, tile_grid_size=(8, 8), p=1),
                alb.HorizontalFlip(),
                alb.Normalize(mean, std),
                ToTensorV2(),
            ]
        )

        self.val_augmentation = alb.Compose(
            [
                alb.Resize(height=img_size, width=img_size),
                alb.Normalize(mean=mean, std=std),
                ToTensorV2(),
            ]
        )

    def prepare_data(self):
        pass

    def split_train_val_df(self, df):
        train_df, val_df = train_test_split(df, test_size=0.2)
        return train_df, val_df

    def binarize_df(self, label_path):
        df = pd.read_csv(label_path)
        df = df.dropna(axis=1, how="all")  # save memory and process usage
        df = df.fillna("None")  # to avoid error

        mlb = MultiLabelBinarizer()
        result = mlb.fit_transform(df.drop(columns=["directory", "filename"]).values)  # drop not tagging cols

        bin_df = pd.DataFrame(result, columns=mlb.classes_).drop("None", axis=1)  # drop non-useless col.
        return df.drop(df.columns[2:], axis=1).join(bin_df)

    # Trainer.fit()ではtrain/valのDatasetを、Trainer.test()ではtestのDatasetを生成
    def setup(self, stage=None):
        if stage == 'fit' or stage is None:
            bin_df = self.binarize_df(os.path.join(self.train_val_root_dir, "label.csv"))
            train_df, val_df = self.split_train_val_df(bin_df)

            self.train_ds = ImgTagDataset(train_df, self.train_val_root_dir, self.train_augmentation)
            self.val_ds = ImgTagDataset(val_df, self.train_val_root_dir, self.val_augmentation)

        if stage == 'test' or stage is None:
            bin_test_df = self.binarize_df(os.path.join(self.test_root_dir, "label.csv"))
            self.test_ds = ImgTagDataset(bin_test_df, self.test_root_dir, self.val_augmentation)

    def get_loader(self, phase):
        return

    def train_dataloader(self):
        # (Known issue) In windows, num_workers > 0 makes stuck in validation checking.
        return DataLoader(self.train_ds, batch_size=self.batch_size, shuffle=True, num_workers=0)

    def val_dataloader(self):
        return DataLoader(self.val_ds, batch_size=self.batch_size, num_workers=0)

    def test_dataloader(self):
        return DataLoader(self.test_ds, batch_size=self.batch_size, num_workers=0)
