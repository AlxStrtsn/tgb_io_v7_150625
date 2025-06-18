from aiogram import Bot, Router
from aiogram.types import BotCommand

router = Router()

# КНОПКА МЕНЮ СЛЕВА
# Создаём асинхронную функцию
async def set_main_menu(bot: Bot):
    # Список команд и их описание для кнопки меню
    main_menu_commands = [
        BotCommand(command='/help',         description='Помощь.'),
        BotCommand(command='/no_button',    description='Если не видно кнопок выборы'),
        BotCommand(command='/start',        description='Сначала.')
    ]
    await bot.set_my_commands(main_menu_commands)