# Assignment-1:- MLLD: NAIVE BAYES CLASSIFIER 

1. mapp.py, redr.py : first run these files for word counting / training.
2. mapp_cntr.py, redr_cntr.py : These files count the number of occurrences of each class and the number of words in them. Number of mappers should always be 1. Output of this should be stored locally with name "classes.txt".
3. mapp_test_cntr.py, reducer_test_counter.py : Requirement for test set is created by these codes. Number of mappers should always be 1.
4. mapp_final.py, redr_final.py : These files merge the trained model and to be tested model. Number of reducers should always be 1.
5. NB_mapp.py, NB_redr.py : These files implement the Naive Bayes algorithm. Number of reducers should always be 1. NB_mapp1 implements 1st algorithm and NB_mapp2 implements 2nd algorithm.

test1.py : Local Naive Bayes implementation of algorithm 1. test2.py : Local Naive Bayes implementation of algorithm 2.
