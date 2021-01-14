import config
import logging

from aiogram import Bot, Dispatcher, executor, types
from sqlighter import SQLighter

# задаем некий уровень логов

logging.basicConfig(level=logging.INFO)

# инициализируем бота

bot = Bot(token=config.TOKEN)

dp = Dispatcher(bot)

# инициализация коннекта с бд

db = SQLighter('db.db')

# команда активации подписки

@db.message_handler(commands=['subscribe'])
async def subscribe(message: types.message):
    if(not db.sub_exists(message.from_user.id, False)):
        db.add_sub(message.from_user.id)
    else:
        db.update_sub(message.from_user.id, True)
    await message.answer("Вы подписались.")
# чтож эхо

# @dp.message_handler()
# async def echo(message: types.message):
#     await message.answer(message.text)

# ну давай запустим лонг поллинг
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


