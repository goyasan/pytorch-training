import torch
from torch.nn import Module

class ExerciseModel(Module):

    def __init__(self, mytensor, elem_add, elem_multiply):
        super().__init__()
        self.mytensor = mytensor
        self.elem_add = elem_add
        self.elem_multiply = elem_multiply

    def forward(self, x):        
        a = self.mytensor + x
        b = a + self.elem_add
        c = b * self.elem_multiply
        return a,b,c
    

if __name__ == "__main__":
    mymodel = ExerciseModel(torch.ones((3, 3)), 4, 6)

    p2out, p3out, p4out = mymodel(torch.full((3, 3), 2))

    print("問題2") 
    print(repr(p2out))
    
    print("問題3") 
    print(repr(p3out))

    print("問題4")    
    print(repr(p4out))
