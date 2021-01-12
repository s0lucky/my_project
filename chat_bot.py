from vkbottle.bot import Bot


bot = Bot("c57bd60c5b15c3015bbdc5fdfcef6466ca0dc869a435a2b8e800117e760895d5e3367e0757298973c7965")


@bot.on.message()
async def sms():
    return "Hello world!"

bot.run_forever()
