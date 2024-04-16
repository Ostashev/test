import json
from datetime import datetime

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from request import aggregate_data
from states import CreateRequest

router = Router()


@router.message(F.text.lower() == "/start")
async def films(message: Message, state: FSMContext):
    await message.answer("Введите запрос ниже.")
    await state.set_state(CreateRequest.get_text)


@router.message(CreateRequest.get_text, F.text)
async def set_text_handler(message: Message, state: FSMContext):
    data = json.loads(message.text)
    dt_from = datetime.fromisoformat(data['dt_from'])
    dt_upto = datetime.fromisoformat(data['dt_upto'])
    result = await aggregate_data(dt_from=dt_from, dt_upto=dt_upto, group_type=data['group_type'])
    await message.answer(
        text=json.dumps(result)
    )
