@bot.on(events.NewMessage(chats=events.ChatType.GROUP))
async def handle_new_message(event):
    if event.chat.title == 'your_group_name':
        message = event.message.message
        if message.startswith('/arkadas'):
            chat = await bot.get_entity(event.chat_id)
            users = await bot.get_participants(chat)
            random_users = random.sample(users, 2)
            for user in random_users:
                await bot.send_message(chat, f'@{user.username} artık arkadaşınız!')

bot.run_until_disconnected()
