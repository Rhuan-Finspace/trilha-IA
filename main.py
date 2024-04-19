
class Neuron:
    def __init__(self, weights: list, bias: float = 0.0):
        self.weights = weights
        self.bias = bias

    def feedforward(self, inputs):
        total = self.bias
        for i in range(len(self.weights)):
            total += self.weights[i] * inputs[i]
        return 1 if total > 0 else 0
    
def and_gate(inputs):
    return Neuron(weights=[1, 1], bias=-1).feedforward(inputs)


def or_gate(inputs):
    return Neuron(weights=[1, 1], bias=0).feedforward(inputs)

def not_gate(inputs):
    return [Neuron(weights=[-1], bias=1).feedforward([i]) for i in inputs]

def xor_gate(inputs):
    and_inputs = and_gate(inputs)
    or_inputs = or_gate(inputs)
    not_and_inputs = not_gate([and_inputs])
    return and_gate([or_inputs, not_and_inputs[0]])

# Prints a table of results:
print('num AND OR XOR   NOT')
for i in range(2):
    for j in range(2):
        print(f'{i} {j}  {and_gate([i, j])}  {or_gate([i, j])}   {xor_gate([i, j])}  {not_gate([i, j])}')
print()



while(True):
    numbers = input('Escreva 2 numeros: ').split(' ')
    numbers = [int(i) for i in numbers]
    print(f'AND: {and_gate(numbers)}')
    print(f'OR: {or_gate(numbers)}')
    print(f'NOT: {not_gate(numbers)}')
    print(f'XOR: {xor_gate(numbers)}')
    
    
    

