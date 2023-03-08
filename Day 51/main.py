from internetspeedtwitterbot import InternetSpeedTwitterBot

twitter = InternetSpeedTwitterBot()
twitter.get_internet_speed()

if float(twitter.speed) < 100:
    twitter.tweet_at_provider()
