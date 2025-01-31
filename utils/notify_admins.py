from aiogram import Dispatcher
from aiogram.utils.exceptions import ChatNotFound
from loguru import logger

from data.config import load_config


async def on_startup_notify(dp: Dispatcher):
    logger.info("Оповещение администрации...")
    for admin in load_config().tg_bot.admin_ids:
        try:
            await dp.bot.send_message(
                admin, "Бот был успешно запущен", disable_notification=True
            )
        except ChatNotFound:
            logger.debug("Чат с админом не найден")
