
import socket
import sys
import requests
import tweepy
import json

# Credentials (INSERT YOUR KEYS AND TOKENS IN THE STRINGS BELOW)
api_key = "ECpg6qEt7Qj6FIkhIcWSCUW2D"
api_secret = "JD4mWvplBlEEyXwba5Ldqdm2m1Fq4K5Tsl7oa1ManlHG90dZT7"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAOpqkQEAAAAApLuQusulMIWTsVzIOi7iVK3jGug%3DN56kcnfSt3Sp61jlKNIV3rvBnLdW69fTuEzCx1aZlWRlnYsMEY"
access_token = "1598256500799045634-WeL5YUFnaZwmzmDrqT8BHtBQosOPyK"
access_token_secret = "Ocu8UWgywxsA9jOCk2krHDNK7nwIyn7qjFn9npCA9MkgY"

# Gainaing access and connecting to Twitter API using Credentials
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)


def send_tweets_to_spark(http_resp, tcp_connection):
    for line in http_resp.iter_lines():

            full_tweet = json.loads(line)
            #tweet_text = full_tweet['text'].encode("utf-8") + '\n' # pyspark can't accept stream, add '\n'
            dict=full_tweet['data']
            tweet_text=dict['text']
            print( tweet_text)
            print ("------------------------------------------")
            tcp_connection.send(tweet_text.encode())



def get_tweets():
    url='https://api.twitter.com/2/tweets/sample/stream'
    headers={"Authorization" : "Bearer {}".format(bearer_token)}
    response = requests.request("GET", url,headers=headers, stream=True)
    '''for line in response.iter_lines():
        if line:
            msg=json.loads(line)
            #print(json.dumps(msg,indent=4,sort_keys=True))
    for line in response.iter_lines():
            full_tweet = json.loads(line)
            #tweet_text = full_tweet['text'].encode("utf-8") + '\n' # pyspark can't accept stream, add '\n'
            print( full_tweet.keys())
            dict=full_tweet['data']
            tweet=dict['text']
            print( tweet)
            print ("------------------------------------------")'''

    return response








TCP_IP = "localhost"
TCP_PORT = 9009

conn = None
conn1 = None
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((TCP_IP, TCP_PORT))

s.listen(1)

print("Waiting for TCP connection...")
conn, addr = s.accept()

print("Connected... Start getting tweets.")
resp = get_tweets()
send_tweets_to_spark(resp,conn)

