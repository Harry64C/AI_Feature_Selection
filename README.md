# Introduction
This is a class project for Machine Learning (ML) I completed alone over 2 months. Here I implement the ML classification algorithm called Nearest Neighbor, assisted by the Feature Selection algirithm. 

# Code Design
- I created the Validator and Classifier in a different file which I then import to the search algorithm file. I implemented Greedy Search using a regular list to hold the frontier nodes (which are feature states) and a set to keep track of unchecked features list. 
- After finishing part 3 and painstakingly running my code on the large dataset, I decided to improve performance. The method I decided on is “throw some away” data pruning. I added a function that calculates the distance between each data point and its closest neighbor of another class. It then sorts this information and prunes the least relevant 66% of points. This improved evaluation speed by around 10 times.  
- For code documentation, I used the ‘queue’, ‘copy’, ‘scipy.spatial’, ‘numpy’, and ‘time’ libraries. 

# Dataset Details
- The General Small Dataset: 10 features, 100 instances.
- The General Large Dataset: 40 features, 1000 instances.
- Personal Small Dataset 19: 10 features, 100 instances.
- Personal Large Dataset 19: 40 features, 1000 instances.

# Algorithms
- Forward Selection: This algorithm starts with no features then creates a frontier of all the desired features that have yet to be chosen (which is all of them at first). It recursively chooses the feature set with the highest accuracy until the current state contains all features. The output is the feature set state explored with the highest accuracy.
- Backward Elimination: This algorithm starts with all features then creates a frontier of all the desired features that have yet to be chosen to be eliminated (which is all of them at first). It recursively chooses the feature set with the highest accuracy until the current state contains no features. The output is the feature set state explored with the highest accuracy. 

# Analysis
<img width="660" alt="Screenshot 2024-07-05 at 4 14 19 PM" src="https://github.com/Harry64C/AI_Feature_Selection/assets/57604508/7442dbb9-4de8-4088-906d-2f3156f6c2d4">
- Experiment 1: Comparing Forward Selection vs Backward Elimination. While both algorithms performed the same on the sample datasets, backward elimination seemed to perform far worse on my personal dataset. It would eliminate relevant features early because they seemed less accurate than a combination of another set of features (that in isolation were revealed to be less relevant). I didn’t find any upsides to it at all. On the other hand, forward selection was consistently effective because it would find the relevant features early. However even in comparison to backward elimination, using no feature selection at all was terrible. The best default accuracy I saw was 0.672 (most common class / total number of instances). 
- Experiment 2: Effect of normalization. Normalization didn’t make any visible difference for the sample datasets, probably because they were designed to give consistent results. Normalization made a large difference on my personal datasets, generally improving the accuracy by about 0.2. This is because the feature units could have been skewed to appear closer or further than they really were, prior to normalization. 
- Experiment 3: Effect of number neighbors (k). I experimented with changing my test function to evaluate using the 3 nearest neighbors. I was surprised to see this change greatly improved the accuracy of nearly every small dataset evaluation. However, 3-NN had about the same effectiveness as 1-NN on the large datasets, likely because more points meant more consistency. 

# Conclusion
Forward selection was always equal or better than backward elimination. Both were far better than no feature selection using the default “guess” evaluation. Normalization would improve accuracy to varying degrees on some datasets. 3-NN was much more accurate than 1-NN on small datasets, but less impactful on large datasets. Potential improvements include using a better algorithm for greedy search and a larger k for k-NN. 
