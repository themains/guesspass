## guesspass: predict password from username

Building on our work that uses ~881M leaked passwords to build a [character-level password generator](https://github.com/themains/password) as a way to assess password strength, we more directly approach the problem of how predictable is the password in a setting where we know the user's password. We build a supervised model that uses the username to predict the password. We then test the model to see how well we can predict the password among unseen usernames, assessing the prediction accuracy with edit distance, etc., kinds of metrics. 


### Authors

Rajashekar Chintalapati and Gaurav Sood
