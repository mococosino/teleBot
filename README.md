# My TelegramBot

>**Eng:**
  >Hi, I am creating my own telegram bot. I will write out all the updates, and add various changes here.

>**Рус:**
  >Привет, я создаю своего телеграм бота. Все обновления буду выписывать, ну и добавлять различные изменения сюда.
Данный будет по большей части площадкой для теста новых фич и т.д.

### Планы: ###
1. Создать привязку к SQLite :chart:
2. Использовать ID пользователей в дальнейшем 
  	- Научится извлекать ID пользователя из DB :chart:
  		- Создать на основе привязки ID *аккаунт пользователя в боте*
3. Попробовать создать личный кабинет пользователя

#### SQLite в телеграм боте: ####

* Призка SQLite
```
import sqlite3

con = sqlite3.connect("database.db", check_same_thread=False)
cursor = con.cursor()
```
* Запись ID, Имени пользователя
```
@api.message_handler(commands=['start'])
def start_message(message):
	api.send_message(message.chat.id, 'Добро пожаловать')

def db_table_val(id: int, name: str, surname:str, phone: str):
	cursor.execute('INSERT INTO users (id, name) VALUES (?, ?)', (id, name))
	con.commit()

@api.message_handler(content_types=['text'])
def get_text_messages(message):
	if message.text.lower() == 'Привет':
    		api.send_message(message.from_user.id, 'Added')

	us_id = message.from_user.id
	us_name = message.from_user.first_name

	db_table_val(id = us_id, name = us_name)

api.polling(none_stop=True)
```

### Идеи: ###
* Создать простую игру
> Игра на основе той, что я делал на **Python** до этого

* Создать бота рассылку на основе получения ID пользователя
> Нужно для заказа 
