"""
In the skimage package, the label function under the measure submodule can be used to realize the connected component labelling.

Use two pass algorithm.
First pass:
Scan through the image by row, look at each pixel's neighbours.
For 4-connectivity, we need to examine neighbours above/left of the current pixel.

There are three scenarios:
1) If there are no labelled neighbours, the pixel is labelled the current element;
2) If there are one or more same labelled neighbours, the pixel is labelled the same as its neighbours.
3) If there are neighbours with different values, label the current pixel with the smallest of its neighbours' labels.
   Use the Disjoint-Set data structure to store the label equivalences,
   and retrieve the lowest label as the representativen in each set of equivalent labels.

Second pass:
Scan again, to check if there is any equivalent labels recorded in the disjiont-set data structure.
If this happens, we replace the pixel's label with the lowest label in the equivalence set.

"""

from skimage import measure
import numpy as np

# read the input file as 2d-array, input parameters of label function need to be ndarray of dtype int
input_img = np.genfromtxt("/Users/peng/Desktop/AY20_MBDS_questions/Question 4/input_question_4",
                          dtype=int)
labels = measure.label(input_img, connectivity=1)  # connectivity equals 1 is using 4-connectivity

with open('output_question_4', 'w') as f:
    for i in range(len(labels)):
        for j in range(len(labels[i])):
            f.write(str(labels[i][j]))
            f.write('\t')
        f.write('\n')