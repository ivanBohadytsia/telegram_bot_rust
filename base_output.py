from aiogram import types, F
from aiogram.utils.markdown import hbold
from aiogram.dispatcher.router import Router
from bases_list_read import data_pictures


base_output_router = Router()

for num_dict in range(len(data_pictures["bases"])):
    for base in list(data_pictures["bases"][num_dict].keys()):
        @base_output_router.message(F.text.lower() == base)
        async def base_send(message: types.Message):
            data_picture = []
            for num_base in range(len(data_pictures["bases"])):
                data_picture_for = data_pictures["bases"][num_base].get(message.text.lower())
                if data_picture_for is not None:
                    data_picture += data_picture_for
                    break
            kb = [
                [types.KeyboardButton(text="⬅️ Меню")]
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
            await message.answer_photo(photo=types.FSInputFile(path=data_picture[0]),
                                       reply_markup=keyboard,
                                       caption=hbold("Ресурси:\n") + data_picture[1])
