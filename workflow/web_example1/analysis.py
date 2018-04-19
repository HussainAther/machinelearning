"""
MDS transformation of Iris dataset
"""

from sklearn.datasets import load_iris
from sklearn.manifold import MDS

# data is loaded when module is imported
iris_data = load_iris()
transformed_data = None

def get_results():
    """
    Return precalculated dataset
    """
    global transformed_data
    assert transformed_data is not None
    names = iris_data.target_names
    results = []
    for i in range(transformed_data.shape[0]):
        results.append({
            'x': transformed_data[i, 0],
            'y': transformed_data[i, 1],
            'label': names[iris_data.target[i]]
        })
    return results


def precalculate_models():
    """
    Precalculation step. Could take a while to compute
    """
    global transformed_data
    mds = MDS(n_components=2)
    transformed_data = mds.fit_transform(iris_data.data)
    print("DONE")
