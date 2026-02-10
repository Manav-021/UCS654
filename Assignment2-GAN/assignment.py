import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import torch
import torch.nn as nn
import torch.optim as optim

# Roll number calculations
r = 102317270
a_r = 0.5 * (r % 7)
b_r = 0.3 * ((r % 5) + 1)

# Load data
df = pd.read_csv("data.csv")
x = df["no2"].dropna().values

# transformation
z_data = x + a_r * np.sin(b_r * x)

# Convert to tensor for PyTorch
real_data = torch.tensor(z_data, dtype=torch.float32).view(-1, 1)

# models
G = nn.Sequential(
    nn.Linear(1, 32),
    nn.ReLU(),
    nn.Linear(32, 1)
)

D = nn.Sequential(
    nn.Linear(1, 32),
    nn.ReLU(),
    nn.Linear(32, 1),
    nn.Sigmoid()
)

# Optimizers and Loss
lr = 0.0002
optimizer_G = optim.Adam(G.parameters(), lr=lr)
optimizer_D = optim.Adam(D.parameters(), lr=lr)
criterion = nn.BCELoss()

# Training
epochs = 3000
batch_size = 64

for epoch in range(epochs):
    # Train Discriminator
    idx = torch.randint(0, len(real_data), (batch_size,))
    real_batch = real_data[idx]

    # Generate fake data
    noise = torch.randn(batch_size, 1)
    fake_batch = G(noise)


    loss_real = criterion(D(real_batch), torch.ones(batch_size, 1))
    loss_fake = criterion(D(fake_batch.detach()), torch.zeros(batch_size, 1))
    loss_D = loss_real + loss_fake

    optimizer_D.zero_grad()
    loss_D.backward()
    optimizer_D.step()

    # Train Generator
    loss_G = criterion(D(fake_batch), torch.ones(batch_size, 1))

    optimizer_G.zero_grad()
    loss_G.backward()
    optimizer_G.step()

    # Print progress
    if epoch % 500 == 0:
        print(f"Epoch {epoch} | Loss D: {loss_D.item():.4f} | Loss G: {loss_G.item():.4f}")

# plotting
with torch.no_grad():
    generated_data = G(torch.randn(5000, 1)).numpy()

plt.figure(figsize=(8, 5))
plt.hist(z_data, bins=60, density=True, alpha=0.6, label="Real Data (z)")
plt.hist(generated_data, bins=60, density=True, alpha=0.6, label="GAN Generated")
plt.xlabel("NO2 Concentration (Transformed)")
plt.ylabel("Density")
plt.title(f"GAN PDF Approximation (Roll No: {r})")
plt.legend()
plt.show()
