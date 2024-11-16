from aiogram import types, Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.enums.chat_action import ChatAction
from databaseorm import add_user, add_message
from azure_api import chat_ai
from fsm_states_group import aiMode
from keyboards import *
from config import *


bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    start_message = (
        f"👋 <b>Hello! I'm your AI-powered assistant, ready to help you explore knowledge, answer questions, and provide support.</b>\n"
        "\n"
        f"🔹 To start using the AI features, click the button below to enter start using AI.\n"
        "\n"
        f"💡 Just click <b>'AI mode 🤖'</b> whenever you're ready to chat with the AI.\n"
    )
    start_photo = types.FSInputFile(path="img\\greeting.jpg")
    add_user(fullname=message.from_user.full_name, userid=message.from_user.id)
    await message.answer_photo(photo=start_photo, caption=start_message, parse_mode='HTML', reply_markup=get_start_keyboard())


@dp.message(F.text=='AI mode 🤖')
async def bot_ai_state(message: types.Message, state: FSMContext):
    await message.answer("✨ <b>AI mode activated!</b> Ask me anything", reply_markup=get_ai_mode_keyboard(), parse_mode='HTML')
    await state.set_state(aiMode.ai_mode)
    await state.update_data(question="Empty")
    await state.update_data(answer="Empty")


@dp.message(aiMode.ai_mode)
async def bot_ai_state_ai_mode(message: types.Message, state: FSMContext):
    if message.text == 'Leave AI mode ❌':
        await state.clear()
        await message.answer(text="🚫 <b>You have left AI mode</b>", reply_markup=get_start_keyboard(), parse_mode='HTML')
    else:
        data = await state.get_data()
        question = message.text
        prompt = f"Previous question was: '{data['question']}'.\nYour previous answer was: '{data['answer']}'.\nActual question from user is: {question}"
        await bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
        answer = chat_ai(prompt=prompt)
        add_message(userid=message.from_user.id, question=question, answer=answer)
        await message.answer(text=answer)
        await state.update_data(question=question)
        await state.update_data(answer=answer)
        await state.set_state(aiMode.ai_mode)



@dp.message(F.text)
async def echo(message: types.Message):
    await message.reply(text=message.text)