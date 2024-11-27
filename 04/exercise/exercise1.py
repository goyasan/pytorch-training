import torch
from torch import nn


if __name__=="__main__":
    tensor = torch.ones(32,3,128,128)
    print("演習1,1")
    print(torch.Tensor.size(tensor))

    print("演習1,2")
    conv = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3)
    tensor2 = conv(tensor)
    print(torch.Tensor.size(tensor2))

    print("演習1,3")
    conv2 = nn.Conv2d(in_channels=3, out_channels=256, kernel_size=3, stride=2, padding=1)
    tensor3 = conv2(tensor)
    print(torch.Tensor.size(tensor3))

    print("演習1,4")
    conv3 = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=5, padding=1)
    tensor4 = conv3(tensor)
    print(torch.Tensor.size(tensor4))

    conv4 = nn.Conv2d(in_channels=3, out_channels=256, kernel_size=5, stride=2, padding=2)
    tensor5 = conv4(tensor)
    print(torch.Tensor.size(tensor5))