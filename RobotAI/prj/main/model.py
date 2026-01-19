import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import os

import numpy as np

class Linear_QNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.linear1 = nn.Linear(input_size, hidden_size)
        self.linear2 = nn.Linear(hidden_size, output_size)

    # la funzione forward definisce come i dati passano attraverso la rete. 
    # Ogni layer della rete prende un input, lo trasforma e passa l’output al layer successivo.
    def forward(self, x):
        x = F.relu(self.linear1(x))
        x = self.linear2(x)
        return x
    
    def save(self, file_name='model.pth'):
        model_path = './main/model'
        if not os.path.exists(model_path):
            os.makedirs(model_path)
        file_name = os.path.join(model_path, file_name)
        torch.save(self.state_dict(), file_name)

class QTrainer:
    def __init__(self, model, lr, gamma):
        self.lr = lr
        self.gamma = gamma
        self.model = model
        self.optimizer = optim.Adam(model.parameters(), lr=self.lr)
        self.criterion = nn.MSELoss()

    def train_step(self, state, action, reward, next_state):
        # converti input in tensori
        state = torch.tensor(np.array(state), dtype=torch.float)
        next_state = torch.tensor(np.array(next_state), dtype=torch.float)
        action = torch.tensor(np.array(action), dtype=torch.long)
        reward = torch.tensor(np.array(reward), dtype=torch.float)

        # aggiungi batch dimension se necessario
        if len(state.shape) == 1:
            state = torch.unsqueeze(state, 0)
            next_state = torch.unsqueeze(next_state, 0)
            action = torch.unsqueeze(action, 0)
            reward = torch.unsqueeze(reward, 0)

        pred = self.model(state)
        target = pred.clone().detach()

        # target Q è sempre calcolato con il next_state.
        for idx in range(len(state)):
            # Q_new calcolato sempre sul next_state
            Q_new = reward[idx] + self.gamma * torch.max(self.model(next_state[idx]).detach())
            target[idx][torch.argmax(action[idx]).item()] = Q_new

        self.optimizer.zero_grad()
        loss = self.criterion(target, pred)
        loss.backward()
        self.optimizer.step()

        return loss.item()
