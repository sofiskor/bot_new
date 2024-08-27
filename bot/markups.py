import bot.buttons as bt

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

keyboard_start = ReplyKeyboardMarkup(keyboard=bt.start,
                                     resize_keyboard=True,
                                     input_field_placeholder="Ввойдите"
                                     )

send_contact = ReplyKeyboardMarkup(keyboard=bt.contact,
                                   resize_keyboard=True
                                   )

organisation = ReplyKeyboardMarkup(keyboard=bt.organisation,
                                   resize_keyboard=True
                                   )

go_back = ReplyKeyboardMarkup(keyboard=bt.back,
                              resize_keyboard=True
                              )

go_back_menu = ReplyKeyboardMarkup(keyboard=bt.back_menu,
                                  resize_keyboard=True
                                  )

# auth_menu = ReplyKeyboardMarkup(keyboard=bt.auth,
#                                     resize_keyboard=True
#                                     )

auth_menu = ReplyKeyboardBuilder()
auth_menu.row(bt.create, bt.state)
auth_menu.row(bt.helpp)

numbers = ReplyKeyboardBuilder()
for i in range(1, 10):
    numbers.add(KeyboardButton(text=str(i)))
    numbers.adjust(3)

send_menu = ReplyKeyboardBuilder()
send_menu.row(bt.down_FO_AFU, bt.down_FO_RRL, bt.down_FO_AKB)
send_menu.row(bt.down_FO_screenshots, bt.down_FO_KSH, bt.down_FO_WES)
send_menu.row(bt.down_FO_VID, bt.down_FO_VIDEO)
send_menu.row(bt.down_FO_CHECK_LIST)
send_menu.row(bt.down_FO_OTCHET, bt.down_FO_EXIT)

ksh_menu = ReplyKeyboardBuilder()
ksh_menu.row(bt.ksh_number, bt.ksh_1)
ksh_menu.row(bt.ksh_2, bt.back_menu_)

vid_menu = ReplyKeyboardBuilder()
vid_menu.row(bt.vid_number, bt.vid_closed)
vid_menu.row(bt.vid_opened, bt.back_menu_)

rectifier_menu = ReplyKeyboardBuilder()
rectifier_menu.row(bt.flat_pack2, bt.energomera_2)
rectifier_menu.row(bt.telecom_group, bt.huawei)
rectifier_menu.row(bt.ericsson, bt.AEG, bt.delta)
rectifier_menu.row(bt.powertel, bt.shtil)
rectifier_menu.row(bt.previous_step)

previous_step = ReplyKeyboardBuilder()
previous_step.row(bt.previous_step)


power_type_menu = ReplyKeyboardBuilder()
power_type_menu.row(bt.energomera, bt.eltek)
power_type_menu.row(bt.SC500, bt.huawei, bt.emerson)
power_type_menu.row(bt.ipcom, bt.AEG, bt.delta)
power_type_menu.row(bt.powertel, bt.shtil)
power_type_menu.row(bt.previous_step)


ksh_type_menu = ReplyKeyboardBuilder()
ksh_type_menu.row(bt.eltek, bt.ericsson)
ksh_type_menu.row(bt.powertel, bt.apparat)
ksh_type_menu.row(bt.intercross, bt.intercross_huawei)
ksh_type_menu.row(bt.telecom_group, bt.shtil)
ksh_type_menu.row(bt.tech_room)
ksh_type_menu.row(bt.energomera, bt.energomera_new)
ksh_type_menu.row(bt.previous_step)

comments = ReplyKeyboardBuilder()
comments.row(bt.no_comment)
comments.row(bt.previous_step)