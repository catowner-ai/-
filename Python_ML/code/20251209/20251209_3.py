# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 18:55:56 2024

@author: Louis_office
"""
# ref : https://scikit-learn.org/stable/index.html
# ref : https://scikit-learn.org/1.3/tutorial/machine_learning_map/
# ref : https://scikit-learn.org/stable/api/sklearn.datasets.html

from sklearn import datasets

iris = datasets.load_iris()


import matplotlib.pyplot as plt


_, ax = plt.subplots()

scatter = ax.scatter(iris.data[:, 2], iris.data[:, 3], c=iris.target)


ax.set(xlabel=iris.feature_names[2], ylabel=iris.feature_names[3])


_ = ax.legend(scatter.legend_elements()[0], iris.target_names, loc="lower right", title="Classes")



#%%

# legend1 = ax.legend(scatter.legend_elements()[0],iris.target_names,
#                     loc="lower right", title="Classes")


# ax.add_artist(legend1)

# legend1 = ax.legend(scatter.legend_elements(),loc="lower right", title="Classes")




# handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6)
# legend2 = ax.legend(handles, labels, loc="upper right", title="Sizes")

# plt.show()
