import torch
from torch import nn
from torch.nn import Module

class ExerciseModel(Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(in_channels=3, out_channels=256, kernel_size=5, stride=8, padding=2)
        self.norm = nn.BatchNorm2d(num_features=256)
        self.relu = nn.ReLU()
        self.linear = nn.Linear(in_features=256 *16 * 16, out_features=64, bias=True)

    def forward(self, x):
        temp = self.conv(x)
        temp = self.norm(temp)
        temp = self.relu(temp)
        temp = temp.view(-1, 256 * 16 *16)
        temp = self.linear(temp)
        return temp

