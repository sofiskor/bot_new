from aiogram.types import KeyboardButton

start = [
    [
        KeyboardButton(text="Регистрация"),
        KeyboardButton(text="Авторизация")
    ],
]
contact = [
    [
        KeyboardButton(text="Отправить контакт",
                       request_contact=True)
    ],
]

organisation = [
    [
        KeyboardButton(text="RTK"),
        KeyboardButton(text="USTK")
    ],
]

create = KeyboardButton(text="Создать ФО по ТО")
state = KeyboardButton(text="Статус проверки")
helpp = KeyboardButton(text="Помощь")

down_FO_AFU = KeyboardButton(text="Загрузить ФО по АФУ")
down_FO_RRL = KeyboardButton(text="Загрузить ФО по РРЛ")
down_FO_AKB = KeyboardButton(text="Загрузить ФО по АКБ")
down_FO_screenshots = KeyboardButton(text="Загрузить скриншоты")
down_FO_KSH = KeyboardButton(text="Загрузить ФО по КШ")
down_FO_WES = KeyboardButton(text="Загрузить ФО по ВЭС")
down_FO_VID = KeyboardButton(text="Загрузить ФО по Общему виду")
down_FO_VIDEO = KeyboardButton(text="Загрузить видео")
down_FO_CHECK_LIST = KeyboardButton(text="Заполнить электронный чек-лист")
down_FO_OTCHET = KeyboardButton(text="Отправить отчет на проверку")
down_FO_EXIT = KeyboardButton(text="Выход без сохранения")

back = [[KeyboardButton(text="Вернуться назад")]]
back_menu = [[KeyboardButton(text="Назад")]]

ksh_number = KeyboardButton(text="Загрузить ФО Серийного номера КШ")
ksh_1 = KeyboardButton(text="Загрузить ФО 1 КШ")
ksh_2 = KeyboardButton(text="Загрузить ФО 2 КШ")
back_menu_ = KeyboardButton(text="Назад")

vid_number = KeyboardButton(text="Загрузить ФО Общий вид БС")
vid_closed = KeyboardButton(text="Загрузить ФО Общий вид закрытого КШ")
vid_opened = KeyboardButton(text="Загрузить ФО Общий вид открытого КШ")

flat_pack2 = KeyboardButton(text="Flat Pack2")
energomera_2 = KeyboardButton(text="Энергомера SP-II")
telecom_group = KeyboardButton(text="Телеком-Групп")
huawei = KeyboardButton(text="Huawei")
ericsson = KeyboardButton(text="Ericsson")
AEG = KeyboardButton(text="AEG")
delta = KeyboardButton(text="Delta")
powertel = KeyboardButton(text="Powertel")
shtil = KeyboardButton(text="Штиль")

previous_step = KeyboardButton(text="К предыдущему шагу")


energomera = KeyboardButton(text="Энергомера")
eltek = KeyboardButton(text="Eltek")
SC500 = KeyboardButton(text="SC500")
ipcom = KeyboardButton(text="IPCOM")
emerson = KeyboardButton(text="Emerson")

apparat = KeyboardButton(text="Аппаратная")
intercross = KeyboardButton(text="Интеркросс")
intercross_huawei = KeyboardButton(text="Интеркросс Huawei")
tech_room = KeyboardButton(text="Техническое помещение")
energomera_new = KeyboardButton(text="Энергомера (Новая)")

no_comment = KeyboardButton(text="Нет замечаний")