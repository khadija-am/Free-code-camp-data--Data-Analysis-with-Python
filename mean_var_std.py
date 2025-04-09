import numpy as np

def calculate(list):
    mat3by3= np.array(list).reshape(3,3)
    matmeanax0=np.mean(mat3by3,axis=0)
    matmeanax1=np.mean(mat3by3,axis=1)
    matmeanflat=np.mean(mat3by3)
    matvarax0=np.var(mat3by3,axis=0)
    matvarax1=np.var(mat3by3,axis=1)
    matvarflat=np.var(mat3by3)
    matstdax0 = np.std(mat3by3, axis=0)
    matstdax1 = np.std(mat3by3, axis=1)
    matstdflat = np.std(mat3by3)
    matmaxax0=np.max(mat3by3,axis=0)
    matmaxax1=np.max(mat3by3,axis=1)
    matmaxflat=np.max(mat3by3)
    matminax0=np.min(mat3by3,axis=0)
    matminax1=np.min(mat3by3,axis=1)
    matminflat=np.min(mat3by3)
    matsumax0=np.sum(mat3by3,axis=0)
    matsumax1=np.sum(mat3by3,axis=1)
    matsumflat=np.sum(mat3by3)
    names=['mean','variance','standard deviation','maximum','minimum','sum']
    values = [[matmeanax0.tolist(), matmeanax1.tolist(), matmeanflat],
    [matvarax0.tolist(), matvarax1.tolist(), matvarflat],
    [matstdax0.tolist(), matstdax1.tolist(), matstdflat],
    [matmaxax0.tolist(), matmaxax1.tolist(), matmaxflat],
    [matminax0.tolist(), matminax1.tolist(), matminflat],
    [matsumax0.tolist(), matsumax1.tolist(), matsumflat]]
    calculations = dict(zip(names, values))

    return calculations