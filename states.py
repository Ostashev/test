from aiogram.fsm.state import State, StatesGroup


class CreateRequest(StatesGroup):
    get_text = State()
    confirm_sender = State()
