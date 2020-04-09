import pDispose as d
 
def mix(sampleList):
    rSample = {}

    for sample in sampleList:
        for key in sample.keys():
            if key in rSample:
                rSample[key][-1] += sample.get(key)[-1]
            else :
                rSample[key] = [sample.get(key)[-1]]

    for sample in sampleList:
        sample = d.dispose(sample)
    
    return rSample


