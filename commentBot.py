import praw
import random
import time

bot = praw.Reddit(user_agent='Sarcastic Bot 0.0.1',
                     client_id='faECGlYFVehRgA', client_secret="yjIXpYK9aIifMNvJO_GdKiXszRY",
                     username='NotSarcasticBot', password='FODOR1')
subreddit = bot.subreddit('test')

replies = ["fodor is bae"]

for comment in bot.subreddit('test').stream.comments():
	s = comment.body
	asciiStr = s.encode('ascii', 'ignore')

	if asciiStr.find("!sarcasmBot") >= 0:
		message = replies[random.randint(0, len(replies))]
		comment.reply(message)
		time.sleep(600)

