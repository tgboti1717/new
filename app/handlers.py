from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
import app.keyboard as kb
from aiogram.types import FSInputFile
from config import *
router1 = Router()

@router1.message(CommandStart())
async def start(message: Message):
    with open('start.jpg', 'rb') as photo:
            await message.delete()
            await message.answer_photo(FSInputFile('start.jpg'),
                caption=f'Добро пожаловать в бота {name}!\n\nДля начала работы вам необходимо зарегистрировать новый аккаунт на 1win, чтобы бот выдавал верные сигналы! \n\nНажмите на кнопку "Регистрация" ниже, зарегистрируйте аккаунт и нажмите на кнопку "Готово"!',
                parse_mode='html',
                reply_markup=kb.reg
            )
    

@router1.callback_query(F.data == 'yes')
async def yes_reg(callback: CallbackQuery):
    with open('start.jpg', 'rb') as photo:
            await callback.message.delete()
            await callback.message.answer_photo(FSInputFile('start.jpg'),
                caption=f'✅ Регистрация прошла успешно! \n\n🕹 Вы попали в главное меню:',
                parse_mode='html',
                reply_markup=kb.regget
                )
            
@router1.callback_query(F.data == 'play')
async def games(callback: CallbackQuery):
    with open('start.jpg', 'rb') as photo:
            await callback.message.delete()
            await callback.message.answer_photo(FSInputFile('start.jpg'),
                caption=f'Выберите игру:',
                parse_mode='html',
                reply_markup=kb.games
                )
            
@router1.callback_query(F.data == 'back')
async def manual(callback: CallbackQuery):
    with open('start.jpg', 'rb') as photo:
            await callback.message.delete()
            await callback.message.answer_photo(FSInputFile('start.jpg'),
                caption=f'🕹 Вы попали в главное меню:',
                parse_mode='html',
                reply_markup=kb.regget
                )