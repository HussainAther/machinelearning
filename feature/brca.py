from sklearn.decomposition import NMF
from sklearn.cluster import KMeans
from sklearn.metrics.cluster import adjusted_rand_score

import pandas as pd

import sklearn.preprocessing

expression_fname = 'https://dcc.icgc.org/api/v1/download?fn=/release_18/Projects/BRCA-US/protein_expression.BRCA-US.tsv.gz'

E = pd.read_csv(expression_fname, delimiter='\t')

E_mean = E.groupby(['icgc_donor_id','gene_name']).mean().unstack()

X = sklearn.preprocessing.MinMaxScaler().fit_transform(E_mean)

nmf = NMF(n_components=10).fit(X)

Ekmeans = KMeans(n_clusters=10, random_state=0).fit(X)

nmfkmeans = KMeans(n_clusters=10, random_state=0).fit(nmf)

print("Adj. Rand score", adjusted_rand_score(Ekmeans, nmfkmeans))
