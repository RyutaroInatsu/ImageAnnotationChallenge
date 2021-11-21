import pytorch_lightning as pl
import torch
import torch.optim as optim
from torch import nn


class ViTNet(nn.Module):
    def __init__(self, pretrained_vit_model, class_num):
        super(ViTNet, self).__init__()
        self.vit = pretrained_vit_model
        self.fc = nn.Linear(768, class_num)

    def _get_cls_vec(self, states):
        return states['last_hidden_state'][:, 0, :]

    def forward(self, input_ids):
        states = self.vit(input_ids)
        states = self._get_cls_vec(states)
        states = self.fc(states)
        return states


class ImgTagLitModule(pl.LightningModule):
    def __init__(self, net, class_num, lr=5e-4, pos_weight=None):
        super().__init__()
        self.save_hyperparameters()

        self.lr = lr
        self.pos_weight = pos_weight
        self.net = ViTNet(net, class_num)

    def forward(self, img):
        return self.net(img).squeeze(1)

    def binary_cross_entropy_with_logits(self, logits, labels):
        return nn.functional.binary_cross_entropy_with_logits(
            logits, labels, pos_weight=self.pos_weight
        )

    def training_step(self, batch, batch_idx):
        img, label = batch

        logits = self.forward(img)
        loss = self.binary_cross_entropy_with_logits(logits, label)
        loss = torch.sigmoid(logits).data > 0.5
        self.log("train_loss", loss)
        return loss

    def validation_step(self, batch, batch_idx):
        img, label = batch

        logits = self.forward(img)
        loss = self.binary_cross_entropy_with_logits(logits, label)
        loss = torch.sigmoid(logits).data > 0.5
        self.log("val_loss", loss)
        return loss

    def test_step(self, batch, batch_idx):
        img, label = batch

        logits = self.forward(img)
        loss = self.binary_cross_entropy_with_logits(logits, label)
        loss = torch.sigmoid(logits).data > 0.5
        self.log("test_loss", loss)
        return loss

    def configure_optimizers(self):
        # まず全パラメータを勾配計算Falseにする
        for param in self.parameters():
            param.requires_grad = False

        # 追加したクラス分類用の全結合層を勾配計算ありに変更
        for param in self.net.fc.parameters():
            param.requires_grad = True

        optimizer = optim.Adam([{"params": self.net.fc.parameters(), "lr": self.lr}])

        return optimizer
