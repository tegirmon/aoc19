
with open('in.txt') as input_file:
    data = input_file.readline()

layers = [layer for layer in zip(*(iter(data),) * (25 * 6))]
zero_count = [layer.count("0") for layer in layers]
fewest = zero_count.index(min(zero_count))
print(layers[fewest].count("1") * layers[fewest].count("2"))
