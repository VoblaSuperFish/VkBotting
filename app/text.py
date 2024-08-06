hello_user_text = """
💎 Добрый день, дорогой пользователь, этот бот принадлежит SuperVoblaFish 💎
✈ Он умеет: ✈
✔ Получать интересные факты о введеном числе.
✔ Показывать определения по ключевым словам из Wiki.
✔ Сообщать погоду по названию города.
✔ Оставлять заметки и получать их от бота.
✔ Делать рассылку всем пользователям, которые обращались к боту (права админа).

🎲 GitHub проекта: https://github.com/VoblaSuperFish/VkBot 🎲
"""

help_user_text = """
🌌 Ниже представлены функции и команды, которые умеет делать бот 🌌
💻 Показывать определение из вики по ключевому слову - /wiki.
☀ Получать информацию о погоде по названию города  - /weathers.
✳ Получать интересные факты о введеном числе - /numbers.
🕐 Просмотреть инфомарцию о ваших заметках - /zametki.
💌 Сделать рассылку - /sends.
Также можете просто нажать на кнопки, которые у вас появились.
"""

no_command_search_text = """
🌐 У данного бота ещё нет такой команды 🌐
Введите команду /help для получения списка доступных команд или нажмите кнопку снизу
"""

wiki_start_text = """
📋 Ниже введите ваше ключевое слово для поиска по википедии 📋
Можете нажать кнопку отмена или ввести команду /stop для отмены.
"""

exit_all_process_text = """
✅ Вы вышли из процесса ожидания ✅
Выберите другую функцию из списка кнопок ниже, хорошего дня.
"""

no_exit_text = """
❗ Вы не находитесь в процессе ожидания ❗
Выберите другую функцию из списка кнопок ниже, хорошего дня.
"""

weather_start_text = """
🌍 Ниже введите название города для вывода данных о погоде в нём. 🌍
Можете нажать кнопку отмена или ввести команду /stop для отмены.
"""
number_start_text = """
🔢 Ниже введите цифру, по которой хотите получить интересный факт. 🔢
Можете нажать кнопку отмена или ввести команду /stop для отмены.
"""


code_smile:dict = {
    "Clear": "Ясно \U00002600",
    "Clouds": "Облачно \U00002601",
    "Rain": "Дождь \U00002614",
    "Drizzle": "Дождь \U00002614",
    "Thunderstorm": "Гроза \U000026A1",
    "Snow": "Снег \U0001F328",
    "Mist": "Туман \U0001F32B"
}

no_found_city_text = """
🐸 Города с таким названием не было найдено 🐸
Попробуйте ввести название другого города ниже.
"""

exceptionn_500_text = """
❗ Ошибка сервера ❗
Обратитесь к данной функции позже.
"""

