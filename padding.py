import torch
from torch import nn
import torch.autograd as autograd
from torch.autograd import Variable
m = nn.ReflectionPad2d((3,1,1,3))
input = autograd.Variable(torch.randn(2,3,3))
print(input)
output = m(input)
print(output)