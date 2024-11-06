import torch
import numpy as np

data = np.array([
    [[85, 78], [67, 82], [92, 88], [75, 70], [60, 64]],
    [[70, 68], [77, 72], [85, 90], [60, 65], [78, 76]],
    [[80, 84], [88, 87], [66, 68], [72, 73], [64, 60]]
])


print("演習1")
data_tensor = torch.from_numpy(data)
print(torch.Tensor.size(data_tensor))

print("演習2")
torch.permute(data_tensor,(0,2,1))
print(torch.Tensor.size(data_tensor) ,"\n")

print("演習3")
sum_tensor = torch.sum(data_tensor, axis=2)
print(sum_tensor,"\n")

print("演習4")
print(torch.mean(sum_tensor.float(), axis=1),"\n")

print("演習5")
print(torch.sum(sum_tensor, axis=1) / torch.Tensor.size(sum_tensor, axis=1), "\n")