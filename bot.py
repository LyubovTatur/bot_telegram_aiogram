import config
import logging
from aiogram import Bot, Dispatcher, executor, types

# задаем некий уровень логов

logging.basicConfig(level=logging.INFO)

# инициализируем бота

bot = Bot(token=config.TOKEN)

dp = Dispatcher(bot)

# чтож эхо

@dp.message_handler()
async def echo(message: types.message):
    await message.answer(message.text)

# ну давай запустим лонг поллинг
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


