import numpy as np
from random import seed
from random import random
import itertools


def bool_f2(input):
    output = []
    for i in input:
        #output.append(i[0] ^ i[1])
        output.append((i[0] and i[1] and i[2] and i[3]) ^ (i[4] and i[5] and i[6] and i[7]) )
    return np.array(output).reshape(len(output),1)





num_input = 8
inputs = np.array(list(itertools.product([1,0],repeat=num_input)))
outputs = bool_f2(inputs)


# In[4]:


# Initialize a network
def initialize_network(n_inputs, n_hidden, n_outputs):
    network = list()
    hidden_layer = [{'weights':[random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
    network.append(hidden_layer)
    output_layer = [{'weights':[random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
    network.append(output_layer)
    return network


# In[5]:


seed(1)
network = initialize_network(8, 2, 1)
for layer in network:
    print(layer)


# In[6]:


# Calculate neuron activation for an input
def activate(weights, inputs):
    activation = weights[-1]
    for i in range(len(weights)-1):
        activation += weights[i] * inputs[i]
    return activation

# Transfer neuron activation
def transfer(activation):
    return 1.0 / (1.0 + np.exp(-activation))


# Calculate the derivative of an neuron output
def transfer_derivative(output):
    return output * (1.0 - output)


# In[7]:


# Forward propagate input to a network output
def forward_propagate(network, row):
    inputs = row
    for layer in network:
        new_inputs = []
        for neuron in layer:
            activation = activate(neuron['weights'], inputs)
            neuron['output'] = transfer(activation)
            new_inputs.append(neuron['output'])
        inputs = new_inputs
    return inputs


# In[8]:


# Backpropagate error and store in neurons
def backward_propagate_error(network, expected):
    for i in reversed(range(len(network))):
        layer = network[i]
        errors = list()
        if i != len(network)-1:
            for j in range(len(layer)):
                error = 0.0
                for neuron in network[i + 1]:
                    error += (neuron['weights'][j] * neuron['delta'])
                errors.append(error)
        else:
            for j in range(len(layer)):
                neuron = layer[j]
                errors.append(expected[j] - neuron['output'])
        for j in range(len(layer)):
            neuron = layer[j]
            neuron['delta'] = errors[j] * transfer_derivative(neuron['output'])


# In[9]:


# Update network weights with error
def update_weights(network, row, l_rate):
    for i in range(len(network)):
        inputs = row[:-1]
        if i != 0:
            inputs = [neuron['output'] for neuron in network[i - 1]]
        for neuron in network[i]:
            for j in range(len(inputs)):
                neuron['weights'][j] += l_rate * neuron['delta'] * inputs[j]
            neuron['weights'][-1] += l_rate * neuron['delta']


# In[10]:


# Train a network for a fixed number of epochs
def train_network(network, train, l_rate, n_epoch, n_outputs):
    for epoch in range(n_epoch):
        sum_error = 0
        for row in train:
            outputs = forward_propagate(network, row)
            expected = [0 for i in range(n_outputs)]
            expected[row[-1]] = 1
            sum_error += sum([(expected[i]-outputs[i])**2 for i in range(len(expected))])
            backward_propagate_error(network, expected)
            update_weights(network, row, l_rate)
        print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))


# In[11]:


data = np.concatenate((inputs, outputs), axis = 1)


# In[12]:


# Test training backprop algorithm
seed(1)
n_inputs = 8
n_outputs = 2
network = initialize_network(n_inputs, 1, n_outputs)
train_network(network, data, 1, 1000, n_outputs)
for layer in network:
    print(layer)


# In[13]:


print(forward_propagate(network, [1,1,1,1,1,1,0,1]))


# In[181]:


data[1]


# In[182]:


def neuron_output(weights, inputs):

    bias = weights[-1]
    
    return sum(weights[i] * inputs[i] for i in range(len(inputs)-1)) + bias


# In[184]:


neuron_output([1,1,2],[0,1,1])


# In[186]:


activate([1,1,2],[0,1,1])


# In[188]:


for layer in network:
        outputs = []
        for neuron in layer:
            print(neuron)


# In[189]:


network


# In[192]:


list(reversed(range(len(network))))


# In[193]:


len(network)
