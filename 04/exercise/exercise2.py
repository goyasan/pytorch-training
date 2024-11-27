import torch
from torch import nn


if __name__=="__main__":
    tensor = torch.ones(32,1024)
    print("演習2,1")
    print(torch.Tensor.size(tensor))

    print("演習2,2")
    ans2 = nn.Linear(in_features=1024, out_features=256, bias=True)
    print(torch.Tensor.size(ans2(tensor)))

    print("演習2,3")
    ans3 = nn.Linear(in_features=1024, out_features=2048, bias=True)
    print(torch.Tensor.size(ans3(tensor)))

    print("演習2,おまけ")
    omake = ans2(tensor)
    print(torch.Tensor.size(omake.view(32,16,16)))