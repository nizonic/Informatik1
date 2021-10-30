from collections import defaultdict

# Dataset contains data that will be reverse indexed
dataset = [
    "Hello world",
    "This is the WORLD",
    "hello again",
    "helloworld",
    "Hello hello"
 ]

def reverse_index(dataset):
    index_dictionary = {}
    dataset = [x.lower() for x in dataset]
    for line in dataset:
        for word in line.split():
            indices = []
            for i, _ in enumerate(dataset):
                if word in dataset[i].split():
                    indices.append(i)
            index_dictionary[word] = indices
    return index_dictionary

# You can see the output of your function here
print(reverse_index(dataset))
