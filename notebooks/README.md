## Notebooks

### Train using 9GB of data
- [1.0_data_prep.ipynb](1.0_data_prep.ipynb) - Clean up data and get 9GB of data
- [2.0_train_9g.ipynb](2.0_train_9g.ipynb) - Train a model on 9GB of data. 
- [3.0_results.ipynb](3.0_results.ipynb) - Analyze results of above model


### Train using usernames which got repeated more than 100 times
- [1.1_data_prep.ipynb](1.1_data_prep.ipynb) - Strip out all @domain.com and get all usernames which got repeated more than 100 times.
- [1.2_data_prep.ipynb](1.2_data_prep.ipynb) - split data to train, val and test
- [2.1_train_top_100_1m.ipynb](2.1_train_top_100_1m.ipynb) - Train a model using aboe dataset
- [3.1_results.ipynb](3.1_results.ipynb) - Analyze results of above model