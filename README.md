## guesspass: predict password from username

Building on our work that uses ~881M leaked passwords to build a [character-level password generator](https://github.com/themains/password) as a way to assess password strength, we more directly approach the problem of how predictable is the password in a setting where we know the username. We build a supervised model that uses the username to predict the password. We then test the model to see how well we can predict the password among unseen usernames, assessing the prediction accuracy with edit distance, etc., kinds of metrics. 

In our data, we have the same username appear multiple times. Multiple entries for the same username can exist for three reasons: 1. duplicates (as we synthesize over multiple data breaches), 2. people sign up to multiple accounts with the same username, esp. a commercial email username like gmail and these are all separate accounts, and 3. default for separate accounts may be the same username, e.g., test@mongodb.com. We could split the data into train/test by username to address #1 but in the experiments described below. 

### Experiments

#### Random Sample (9GB)

* [Data Prep.](notebooks/1.0_data_prep.ipynb)
* [Train](notebooks/2.0_train_9g.ipynb)
* Results
	* [Lookup Results](notebooks/3.2_results.ipynb)
	* [Comparison to username, etc.](notebooks/3.0.1_graphs.ipynb)
	* [Comparison Between Model and Baselines](notebooks/3.2.1_compare.ipynb)

Of the 10,000 randomly selected usernames, lookup only yields 1700 hits. On the usernames we are able to lookup,  the average min. edit distance over 100 tries from the model is 7.28 while for the lookup, it is 6.23. 

#### Common Usernames

We filter to common usernames (usernames in our database more than 100 times). 

We randomly split the data into train and test and estimate a seq-to-seq model. We measure performance using edit distance and test against the baseline of a simple lookup into the training dataset.

**Notebooks**

* Data Prep.
	* [Prep. 1](notebooks/1.1_data_prep.ipynb)
	* [Data Prep.](notebooks/1.2_data_prep.ipynb)
* [Train](notebooks/2.1_train_top_100_1m.ipynb)
* [Results](notebooks/3.1_results.ipynb)

### Authors

Rajashekar Chintalapati and Gaurav Sood
