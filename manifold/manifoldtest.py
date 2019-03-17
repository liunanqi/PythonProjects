import matplotlib.pyplot as plt
from matplotlib.image import imread
import seaborn as sns; sns.set()
import numpy as np

def makeTextPic(word, N=1000, rseed=42):
    fig, ax = plt.subplots(figsize=(4, 1))
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    ax.axis('off')
    ax.text(0.5, 0.4, word, va='center', ha='center', weight='bold', size=85)
    
    imgname= word + '.png'
    fig.savefig(imgname)
    plt.close(fig)
    
    imgdata = imread(imgname)
    print(imgdata)
    data = imgdata[::-1, :, 0].T
    print(data)
    rng = np.random.RandomState(rseed)
    X = rng.rand(4 * N, 2)
    i, j = (X * data.shape).astype(int).T
    
    mask = (data[i, j] < 1)
    X = X[mask]
    X[:, 0] *= (data.shape[0] / data.shape[1])
    X = X[:N]
    result = dict([('resultX', X[np.argsort(X[:, 0])]), ("colorsize", len(word))])
    return result

result = makeTextPic('ABCDE', 1000, 42)
X = result['resultX']
colorsize = dict(c=X[:, 0], cmap=plt.cm.get_cmap('rainbow', result['colorsize']))
plt.scatter(X[:, 0], X[:, 1], **colorsize)
plt.axis('equal')

plt.show()