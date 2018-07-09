import discord

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!why'):
        msg = 'blame claudia and my inability to not realize when a joke is taken too far'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!botboy'):
        await client.send_message(message.channel, "fuck off idiot")
    elif message.content.startswith('!helpme'):
        msg = 'there is no one that can help you now' .format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!slav'):
        msg = 'сука блять' .format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!ping'):
        msg = 'pong!' .format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!help'):
        msg = 'type !commands' .format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!frog'):
        msg = 'im aware, thanks.' .format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!degenerates'):
        msg = 'https://www.youtube.com/watch?v=AJmDKXrRGXY' .format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!phrases'):
        msg = 'i react to these phrases: fat fucking nuts, solas, speedrunner, hewwo, owo, fuck you botboy, and cock' .format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!commands'):
        msg = 'the full list of commands are: !why !botboy !help !helpme !slav !ping !frog !phrases and !degenerates' .format(message)
        await client.send_message(message.channel, msg)
        # beginning of phrases list 
    elif message.content.startswith('fat fucking nuts'):
        msg = 'please dont say that {0.author.mention}' .format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('FAT FUCKING NUTS'):
        msg = 'please dont say that {0.author.mention}' .format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('Fat fucking nuts'):
        msg = 'please dont say that {0.author.mention}' .format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('solas'):
        msg = 'https://78.media.tumblr.com/859e591bd650e4c04c8eb858eb65e217/tumblr_pbjvgtyi921r5x7c3o1_500.jpg' .format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('Solas'):
        msg = 'https://78.media.tumblr.com/859e591bd650e4c04c8eb858eb65e217/tumblr_pbjvgtyi921r5x7c3o1_500.jpg' .format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('SOLAS'):
        msg = 'https://78.media.tumblr.com/859e591bd650e4c04c8eb858eb65e217/tumblr_pbjvgtyi921r5x7c3o1_500.jpg' .format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('speedrunner'):
        msg = 'If you mean world record, that doesnt mean anything. My dogs taken the most shits in my backyard. Its a WORLD RECORD!!! No other dog has squirted out more shits than this one! HOLY FUCK!!!......' .format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('Speedrunner'):
        msg = 'If you mean world record, that doesnt mean anything. My dogs taken the most shits in my backyard. Its a WORLD RECORD!!! No other dog has squirted out more shits than this one! HOLY FUCK!!!......' .format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('SPEEDRUNNER'):
        msg = 'If you mean world record, that doesnt mean anything. My dogs taken the most shits in my backyard. Its a WORLD RECORD!!! No other dog has squirted out more shits than this one! HOLY FUCK!!!......' .format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('hewwo'):
        msg = 'HEWWO?!?!?!' .format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('Hewwo'):
        msg = 'HEWWO?!?!?!' .format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('HEWWO'):
        msg = 'HEWWO?!?!?!' .format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('owo'):
        msg = 'hewwo xD can i has SR plsss?? nuzzles ur hand OwO maybe we can trade!!~ i’ll give u cuddles :3 and u give me SR? plsss!!!~~ licks ur hand MEOW!!~ :3333! i’ll be a good kitty (◕‿◕✿) cuddles u' .format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('OWO'):
        msg = 'hewwo xD can i has SR plsss?? nuzzles ur hand OwO maybe we can trade!!~ i’ll give u cuddles :3 and u give me SR? plsss!!!~~ licks ur hand MEOW!!~ :3333! i’ll be a good kitty (◕‿◕✿) cuddles u' .format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('OwO'):
        msg = 'hewwo xD can i has SR plsss?? nuzzles ur hand OwO maybe we can trade!!~ i’ll give u cuddles :3 and u give me SR? plsss!!!~~ licks ur hand MEOW!!~ :3333! i’ll be a good kitty (◕‿◕✿) cuddles u' .format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('fuck you botboy'):
        msg = 'Что ебать ты просто чертовски говорила обо мне, маленькая сука? Я тебе зкажу, я закончил вершину моего класса в ВДВ, и я принимал участие в многочисленных секретных рейдов на Аль-Каидой, и у меня есть более 300 подтвержденных убийств. Я тренировался в парижском войны, и я сверху снайпер в целых российских вооруженных сил. Вы ничто для меня, но только другая цель. Я протрите тебе нахрен с точностью, подобных которым никогда не видели раньше на этой Земле, запомните мои чертовы слова. Вы думаете, что вы можете уйти с того, что дерьмо для меня через Интернет? Подумайте еще раз, ублюдок. Как мы говорим Я контактирую мой секретный сеть шпионов по всей России, и ваш IP-трассируется прямо сейчас, так что вам лучше подготовиться к шторму, козу. Шторм, который стирает жалкий небольшое вещь ты называеш твоя жизнь. Ты находишься чертовски мертвых, малыш. Я могу быть где угодно, в любое время, и я могу убить тебя в более семисот способами, и это только голыми руками. Я не только обучен приемам рукопашного боя, но у меня есть доступ ко всей арсенале Воздушно-десантные войска, и я буду использовать его в полной мере, чтобы вытереть задницу жалкий с лица континента, небольшое дерьма. Если бы только ты мог знать, что нечестивый возмездие ваш маленький "умный" комментарий был готов обрушить тебе, может быть, ты бы провели свой гребаный язык. Но ты не мог, ты не сделал, и теперь ты платишь цену, ты идиот проклятый. Я дерьмо ярость все над тобойи ты тонуть в нем. Ты находишься чертовски мертв, детка.' .format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('Fuck you botboy'):
        msg = 'Что ебать ты просто чертовски говорила обо мне, маленькая сука? Я тебе зкажу, я закончил вершину моего класса в ВДВ, и я принимал участие в многочисленных секретных рейдов на Аль-Каидой, и у меня есть более 300 подтвержденных убийств. Я тренировался в парижском войны, и я сверху снайпер в целых российских вооруженных сил. Вы ничто для меня, но только другая цель. Я протрите тебе нахрен с точностью, подобных которым никогда не видели раньше на этой Земле, запомните мои чертовы слова. Вы думаете, что вы можете уйти с того, что дерьмо для меня через Интернет? Подумайте еще раз, ублюдок. Как мы говорим Я контактирую мой секретный сеть шпионов по всей России, и ваш IP-трассируется прямо сейчас, так что вам лучше подготовиться к шторму, козу. Шторм, который стирает жалкий небольшое вещь ты называеш твоя жизнь. Ты находишься чертовски мертвых, малыш. Я могу быть где угодно, в любое время, и я могу убить тебя в более семисот способами, и это только голыми руками. Я не только обучен приемам рукопашного боя, но у меня есть доступ ко всей арсенале Воздушно-десантные войска, и я буду использовать его в полной мере, чтобы вытереть задницу жалкий с лица континента, небольшое дерьма. Если бы только ты мог знать, что нечестивый возмездие ваш маленький "умный" комментарий был готов обрушить тебе, может быть, ты бы провели свой гребаный язык. Но ты не мог, ты не сделал, и теперь ты платишь цену, ты идиот проклятый. Я дерьмо ярость все над тобойи ты тонуть в нем. Ты находишься чертовски мертв, детка.' .format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('FUCK YOU BOTBOY'):
        msg = 'Что ебать ты просто чертовски говорила обо мне, маленькая сука? Я тебе зкажу, я закончил вершину моего класса в ВДВ, и я принимал участие в многочисленных секретных рейдов на Аль-Каидой, и у меня есть более 300 подтвержденных убийств. Я тренировался в парижском войны, и я сверху снайпер в целых российских вооруженных сил. Вы ничто для меня, но только другая цель. Я протрите тебе нахрен с точностью, подобных которым никогда не видели раньше на этой Земле, запомните мои чертовы слова. Вы думаете, что вы можете уйти с того, что дерьмо для меня через Интернет? Подумайте еще раз, ублюдок. Как мы говорим Я контактирую мой секретный сеть шпионов по всей России, и ваш IP-трассируется прямо сейчас, так что вам лучше подготовиться к шторму, козу. Шторм, который стирает жалкий небольшое вещь ты называеш твоя жизнь. Ты находишься чертовски мертвых, малыш. Я могу быть где угодно, в любое время, и я могу убить тебя в более семисот способами, и это только голыми руками. Я не только обучен приемам рукопашного боя, но у меня есть доступ ко всей арсенале Воздушно-десантные войска, и я буду использовать его в полной мере, чтобы вытереть задницу жалкий с лица континента, небольшое дерьма. Если бы только ты мог знать, что нечестивый возмездие ваш маленький "умный" комментарий был готов обрушить тебе, может быть, ты бы провели свой гребаный язык. Но ты не мог, ты не сделал, и теперь ты платишь цену, ты идиот проклятый. Я дерьмо ярость все над тобойи ты тонуть в нем. Ты находишься чертовски мертв, детка.' .format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('cock'):
        msg = 'uh oh! you activated me! perhaps you could use another word {0.author.mention} , unless if you want to get punished by my long, deep, and thick banhammer ;).' .format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('Cock'):
        msg = 'uh oh! you activated me! perhaps you could use another word {0.author.mention} , unless if you want to get punished by my long, deep, and thick banhammer ;).' .format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('COCK'):
        msg = 'uh oh! you activated me! perhaps you could use another word {0.author.mention} , unless if you want to get punished by my long, deep, and thick banhammer ;).' .format(message)
        await client.send_message(message.channel, msg)

 
    

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('MzgzMDk1NDM2NTE0MTY0NzY2.DiQS3g.5u2JZw4iNHitKdqWZXAv6OjhC5I')
