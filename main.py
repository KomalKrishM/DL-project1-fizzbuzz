import torch
PATH = './classifier2.pt'
NUM_DIGITS = 10
NUM_HIDDEN = 150
BATCH_SIZE = 128
model = torch.nn.Sequential(
    torch.nn.Linear(NUM_DIGITS, NUM_HIDDEN),
    torch.nn.ReLU(),
    torch.nn.Linear(NUM_HIDDEN, 4)
)
model.load_state_dict(torch.load(PATH))
def binary_encode(i, num_digits):
    return np.array([i >> d & 1 for d in range(num_digits)])

def fizz_buzz_encode(i):
    if   i % 15 == 0: return 3
    elif i % 5  == 0: return 2
    elif i % 3  == 0: return 1
    else:             return 0

def fizz_buzz_decode(i, prediction):
    return [str(i), "fizz", "buzz", "fizzbuzz"][prediction]

import numpy as np
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--test-data')
args = parser.parse_args()
args = vars(args)
f_path = args['test_data']
with open(f_path) as f:
    s = f.read()
    s_ints = [ int(x) for x in s.split() ]
testX = torch.Tensor([binary_encode(i, NUM_DIGITS) for i in s_ints])
testY = model(testX)
predictions = zip(s_ints, list(testY.max(1)[1].data.tolist()))
out1 = open('software_2.txt','w')
for (i, x) in predictions:
    out1.write(fizz_buzz_decode(i, x))
    out1.write('\n')
out = open('software_1.txt','w')
for i in s_ints:
    if (i%15==0):
        out.write('fizzbuzz')
        out.write('\n')
    elif(i%5==0):
        out.write('buzz')
        out.write('\n')
    elif(i%3==0):
        out.write('fizz')
        out.write('\n')
    else:
        out.write(str(i))
        out.write('\n')