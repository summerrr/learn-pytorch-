import torchvision as tv
import torchvision.transforms as transforms
import torch as t
from torchvision.transforms import ToPILImage
show=ToPILImage()       #��Tensorת��Image��������ӻ�
import matplotlib.pyplot as plt
import torchvision
import numpy as np


###############���ݼ�����Ԥ����
transform = transforms.Compose([transforms.ToTensor(),#תΪtensor
                                transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5)),#��һ��
                                ])
#ѵ����
trainset=tv.datasets.CIFAR10(root='/python projects/test/data/',
                             train=True,
                             download=True,
                             transform=transform)

trainloader=t.utils.data.DataLoader(trainset,
                                    batch_size=4,
                                    shuffle=True,
                                    num_workers=0)
#���Լ�
testset=tv.datasets.CIFAR10(root='/python projects/test/data/',
                             train=False,
                             download=True,
                             transform=transform)

testloader=t.utils.data.DataLoader(testset,
                                   batch_size=4,
                                   shuffle=True,
                                   num_workers=0)


classes=('plane','car','bird','cat','deer','dog','frog','horse','ship','truck')

(data,label)=trainset[100]
print(classes[label])

show((data+1)/2).resize((100,100))

# dataiter=iter(trainloader)
# images,labels=dataiter.next()
# print(''.join('11%s'%classes[labels[j]] for j in range(4)))
# show(tv.utils.make_grid(images+1)/2).resize((400,100))
def imshow(img):
    img = img / 2 + 0.5
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)))

dataiter = iter(trainloader)
images, labels = dataiter.next()
print(images.size())
imshow(torchvision.utils.make_grid(images))
plt.show()#�ص�ͼƬ�������������


#########################��������
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        super(Net,self).__init__()
        self.conv1=nn.Conv2d(3,6,5)
        self.conv2=nn.Conv2d(6,16,5)
        self.fc1=nn.Linear(16*5*5,120)
        self.fc2=nn.Linear(120,84)
        self.fc3=nn.Linear(84,10)

    def forward(self, x):
        x = F.max_pool2d(F.relu(self.conv1(x)),2)
        x = F.max_pool2d(F.relu(self.conv2(x)),2)
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

net=Net()
print(net)

#############������ʧ�������Ż���
from torch import optim
criterion=nn.CrossEntropyLoss()
optimizer=optim.SGD(net.parameters(),lr=0.01,momentum=0.9)

##############ѵ������
from torch.autograd import Variable
import time

start_time = time.time()
for epoch in range(2):
    running_loss=0.0
    for i,data in enumerate(trainloader,0):
        #��������
        inputs,labels=data
        inputs,labels=Variable(inputs),Variable(labels)
        #�ݶ�����
        optimizer.zero_grad()

        outputs=net(inputs)
        loss=criterion(outputs,labels)
        loss.backward()
        #���²���
        optimizer.step()

        # ��ӡlog
        running_loss += loss.data[0]
        if i % 2000 == 1999:
            print('[%d,%5d] loss:%.3f' % (epoch + 1, i + 1, running_loss / 2000))
            running_loss = 0.0
print('finished training')
end_time = time.time()
print("Spend time:", end_time - start_time)
