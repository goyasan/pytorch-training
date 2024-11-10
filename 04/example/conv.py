import torch
from torch import nn

if __name__ == "__main__":
    my_tensor = torch.full((16,3,256,256), 2.718)

    conv = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3)
    out = conv(my_tensor)
    print(repr(out.size()))

    conv2 = nn.Conv2d(in_channels=3, out_channels=128, kernel_size=5, stride=2, padding=2)
    out2 = conv2(my_tensor)
    print(repr(out2.size()))

    