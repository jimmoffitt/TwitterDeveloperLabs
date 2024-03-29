# TwitterDeveloperLabs
Incubating new example code for Twitter Developer Labs... 

Loosely based on code available at https://github.com/TwitterDev/labs-sample=code.

## Getting started

### Set up your Labs environment

+ Get an approved Twitter Developer Account.
+ Create a Twitter App, and generate its tokens needed for Twitter API authentication.
+ Join Labs.
+ Activate a Labs endpoint by assigning your Twitter App to it.

Now that you havde access to Twitter Developer Labs, it time to start writing code to interact with its APIs.

### Running Labs example scripts

+ Clone this repository.


#### Python scripts

+ Running the Python scripts:
  + Update the .env file with your Twitter authentication tokens.
  + Pick a script, perpare the command-line arguments. This information could include Tweet IDs, User names and IDs, and queries for matching on Tweets of interest. 
  + Run the script. E.g. ```$python3 get-users.py --users twitterdev,snowman```
  
  
##### Examples
  
  + **Sampled stream endpoint**
  We will start with this endpoint since it is the most simple endpoint. It does not require any input or command-line parameters. To start a real-time stream that delivers 1% of Tweets (and seconds after being posted) just run the following:
  ```$python3 get-sampled-stream.py```
  
  + **Get users endpoint**
  
  
  + **Get metrics endpoint**
  
 
 





