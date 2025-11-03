import torch
import matplotlib.pyplot as plt
import numpy as np
from torch import nn
from pathlib import Path

MODEL_PATH = Path("models")
MODEL_PATH.mkdir(parents=True, exist_ok=True)
MODEL_SAVE_PATH = MODEL_PATH / "binary_representation_model.pth"

def plt_predictions(train_data,
                    train_labels,
                    test_data,
                    test_labels,
                    predictions=None):
    
    """
    plot.figure(figsize=(10, 7)) 设置图像大小
    plt.scatter() 绘制散点图
    plt.plot() 绘制折线图 (无s参数)
    plt.legend() 图例
    plt.show() 显示图像
    """

    plt.figure(figsize=(10, 7)) #设置图像大小

    plt.scatter(train_data, train_labels,c='b',s=4,label='Training data') #绘制训练数据（color,size,label）

    plt.scatter(test_data, test_labels,c='g',s=4,label='Testing data') #绘制测试数据 （color,size,label）

    if predictions is not None:

        plt.scatter(test_data, predictions,c='r',s=4,label='Predictions')

    plt.legend(prop={'size':14})

    plt.savefig("predictions.png")

# Data preparation
X = torch.arange(-10, 10, 0.01).unsqueeze(dim=1)

y = torch.pow(X, 2) * 3.0 + 4.0

print(f"X的前5行数据:\n{X[:5]}")
print(f"y的前5行数据:\n{y[:5]}")

# Data Split

split_ratio = 0.8
split_index = int(len(X) * split_ratio)

X_train, X_test = X[:split_index], X[split_index:]
y_train, y_test = y[:split_index], y[split_index:]
print(f"X_train shape: {X_train.shape}, y_train shape: {y_train.shape}")
print(f"X_test shape: {X_test.shape}, y_test shape: {y_test.shape}")

# Model Definition
class BinaryRepresentationModel(nn.Module):
    def __init__(self):
        super().__init__()

        self.linear = nn.Linear(in_features=1, out_features=1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.linear(torch.pow(x, 2))
    
torch.manual_seed(42)

model = BinaryRepresentationModel()
print(model.state_dict())

# # Training Setup
# loss_fn = nn.L1Loss()
# optimizer = torch.optim.SGD(params=model.parameters(), lr=0.01)

# # Training Loop

# epochs = 1000

# epoch_count = []
# loss_values = []
# test_loss_values = []

# for epoch in range(epochs):

#     model.train()

#     y_pred = model(X_train)

#     loss = loss_fn(y_pred, y_train)

#     optimizer.zero_grad()

#     loss.backward()

#     optimizer.step()

#     if epoch % 10 == 0:
#         model.eval()
#         with torch.inference_mode():
#             y_test_pred = model(X_test)

#             test_loss = loss_fn(y_test_pred, y_test)

#         epoch_count.append(epoch)
#         loss_values.append(loss.detach().numpy())
#         test_loss_values.append(test_loss.detach().numpy())
#         print(f"Epoch: {epoch} | Train Loss: {loss:.4f} | Test Loss: {test_loss:.4f}")

# # Plot Loss Curves
# plt.figure(figsize=(10, 7))
# plt.plot(epoch_count, loss_values, label="Train Loss")
# plt.plot(epoch_count, test_loss_values, label="Test Loss")
# plt.xlabel("Epoch")
# plt.ylabel("Loss")
# plt.title("Training and Test Loss Over Epochs")
# plt.legend()
# plt.savefig("loss_curve.png")

# # Save model

# torch.save(obj=model.state_dict(), f=MODEL_SAVE_PATH)
# print(f"模型已保存到 {MODEL_SAVE_PATH}")

# load Model

with torch.inference_mode():
    load_model = BinaryRepresentationModel()
    load_model.load_state_dict(torch.load(MODEL_SAVE_PATH))
    print(f"加载的模型参数: {load_model.state_dict()}")
    y_predictions = load_model(X_test)
    plt_predictions(train_data=X_train,
                    train_labels=y_train,
                    test_data=X_test,
                    test_labels=y_test,
                    predictions=y_predictions)