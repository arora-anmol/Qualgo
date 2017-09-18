# Qualgo
### Inspiration
The idea came from our belief that market prices move irrationally in response to public opinion. We believed we could capture the expected value of stocks based on the recent public sentiment of high profile Twitter posts regarding them. However, we soon realised that this could only be one use for this software, so generalised the platform to be able to search any user-defined string, enabling users to search for public sentiment of many topics such as various movies, nations, etc.

### What it does
The current iteration of the web app takes in a user defined 'name' and then scans recent Twitter posts containing that string, using ML algorithms to calculate a weighted score defining public sentiment towards that 'name'. It also displays some of the more recent Tweets, and data about them.

### How we built it
We built it integrating the Twitter Search REST API with the Google Cloud Natural Language Machine Learning API on a Python Flask web framework. Deployments were managed by Google App Engine.

### Challenges we ran into
We needed to determine a way in which we could weight the relative sentiment scores of different tweets, taking into account each user's followers, the number of retweets and the post's salience.

### Accomplishments that we're proud of
Completing a first version of a working app despite the fact that half of the team had to leave half way through the Hackathon.

### What we learned
We became familiar with building and deploying a web app on the Google App Engine, and how to integrate with the Twitter API and Google Cloud Machine Learning API.

### What's next for Qualgo
We plan on improving the way in which we weight the relative sentiment scores.

Also, we will create other views which show 10 companies ranked with the highest current sentiment score. This will also be done on other views for other topics, such as movies/countries/celebrities.

Further, we intend on improving our search speed so that we can pool a larger set of Tweets in order to achieve a more statistically significant sentiment score. This will be made robust by setting up MySQL DB to manage Tweets and Topic sin the backend.

