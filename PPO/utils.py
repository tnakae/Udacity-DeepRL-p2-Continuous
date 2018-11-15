import torch
import torch.nn as nn
import torch.nn.functional as F


class FCNetwork(nn.Module):
    def __init__(self, input_dim, hiddens, func=F.relu):
        super(FCNetwork, self).__init__()

        self.func =  func
        fc_first = nn.Linear(input_dim, hiddens[0])
        self.layers = nn.ModuleList([fc_first])
        layer_sizes = zip(hiddens[:-1], hiddens[1:])
        self.layers.extend([nn.Linear(h1, h2)
                            for h1, h2 in layer_sizes])

    def forward(self, x):
        for layer in self.layers:
            x = self.func(layer(x))
        return x
