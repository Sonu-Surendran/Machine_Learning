import pickle

input_file = "model_1.bin"

with open(input_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

print(dv)
print(model)