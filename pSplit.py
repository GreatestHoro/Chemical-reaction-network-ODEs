import math
import pDispose as d
import numpy as np

def combinedPercent(percentList):
    result = 0
    for number in percentList:
        result += number
    return result

def split(sample, sampleList, percentList):

    for key, value in sample.items():
        for i in range(0, len(sampleList)):
            sampleList[i][key] = [math.floor(value[-1] * percentList[i])]

    percent = combinedPercent(percentList)

    if percent == 1:
        sample = d.dispose(sample)
    else:
        sample = d.disposePercent(sample, percent)

    return sample, sampleList

    