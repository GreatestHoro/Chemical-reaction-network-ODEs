import math

def disposePercent(sample, percent):
    for key in sample.keys():
        sample[key] = [math.ceil(sample.get(key)[-1] * (1 - percent))]
    return sample


def dispose(sample):
    for key in sample.keys():
        sample[key] = [0]
    return sample