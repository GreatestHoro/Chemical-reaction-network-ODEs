import pSplit as s
import pDispose as d
import pMix as m

def split(sample, sampleList, percentList):
    return s.split(sample, sampleList, percentList)

def dispose(sample):
    return d.dispose(sample)

def disposePercent(sample, percent):
    return d.disposePercent(sample, percent)

def mix(sampleList):
    return m.mix(sampleList)