
with open('in.txt') as input_file:
    data = input_file.readline()

width = 25
length = 6
layer_len = width * length
layers = [layer for layer in zip(*(iter(data),) * layer_len)]
full_img = {}
for layer in layers:
    for px_num in range(len(layer)):
        if px_num not in full_img or full_img[px_num] == "2":
            full_img[px_num] = layer[px_num]

for px in zip(*(iter(["  " if px_val == "0" else "# " for px_val in full_img.values()]),) * width):
    print("".join(px))
