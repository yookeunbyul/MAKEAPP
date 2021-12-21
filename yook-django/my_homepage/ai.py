import torch

x_train = torch.FloatTensor([[30],[60],[90]])
y_train = torch.FloatTensor([[700],[750],[800]])
W = torch.zeros(1)
b = torch.zeros(1)

lr = 0.0002

epochs = 10000

len_x = len(x_train)

for epoch in range(epochs):
  hypothesis = x_train * W + b
  cost = torch.mean((hypothesis -y_train)**2)

  gradient_w = torch.sum((W*x_train - y_train +b)*x_train)/ len_x
  gradient_b = torch.sum((W*x_train - y_train +b))/len_x

  W -= lr * gradient_w
  b -= lr * gradient_b
  
  if epoch % 1000 == 0:
    print('Epoch {:4d}/{} W:{:.6f} b:{:.6f} Cost: {:.6f}'.format(epoch,epochs,W.item() ,b.item() , cost.item()))
