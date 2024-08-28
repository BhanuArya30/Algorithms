import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.utils.data import DataLoader, TensorDataset, random_split

# Define the feedforward neural network
class FeedforwardNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(FeedforwardNN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Initialize the model, loss function, and optimizer
input_size = 4   # Example: for a dataset like Iris with 4 features
hidden_size = 10
output_size = 3  # Example: 3 classes for classification
model = FeedforwardNN(input_size, hidden_size, output_size)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Generate some random data
torch.manual_seed(0)
X = torch.randn(100, input_size)  # 100 samples, 4 features each
y = torch.randint(0, output_size, (100,))  # 100 labels (0, 1, or 2)

# Create a DataLoader for training
dataset = TensorDataset(X, y)
train_loader = DataLoader(dataset, batch_size=10, shuffle=True)

# Training loop
num_epochs = 50
for epoch in range(num_epochs):
    for batch_X, batch_y in train_loader:
        optimizer.zero_grad()         # Zero the gradients
        outputs = model(batch_X)       # Forward pass
        loss = criterion(outputs, batch_y)  # Compute loss
        loss.backward()                # Backpropagation
        optimizer.step()               # Update weights
    
    if (epoch+1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# Sample inference on new data
with torch.no_grad():
    new_X = torch.tensor([[0.5, -0.5, 0.3, 0.2]])  # New data point
    prediction = model(new_X)
    predicted_class = torch.argmax(prediction, dim=1)
    print(f'Predicted class: {predicted_class.item()}')
