# ENG
## Bot for warming up your Twitter accounts that are imported into the AdsPower
Everyone understands that Twitter accounts must be active. I periodically use this tool for my farm and during 8 months only 4 accounts were banned (0.12$ each). This bot will help to save you a huge amount of time and some money. It works with Twitter accounts that are imported into [AdsPower] (https://share.adspower.net/Btc9YYgpiyJxhmW).

My telegram: https://t.me/CrytoBusher <br>
My Twitter: https://twitter.com/CryptoBusher <br>

My telegram channel [RU]: https://t.me/CryptoKiddiesClub <br>
Our telegram chat [RU]: https://t.me/CryptoKiddiesChat <br>

## 🔥 Latest updates
- [x] 20.06.2023 - Possibility to subscribe to random accounts from the database (random subscribtions). <br>
- [x] 20.06.2023 - Possibility to subscribe to mandatory accounts from the list (required subscriptions). <br>
- [x] 20.06.2023 - Updated warmup scenario, enhanced randomization. <br>
- [x] 20.06.2023 - Now bot can check if AdsPower profile was already opened by the user. If it was already opened - bot can skip or warmup Twitter account according to user settings. <br>
- [x] 04.08.2023 - The script detects pop-ups and dodges them. Fully customized feature. <br>
- [x] 04.08.2023 - The bot can now navigate the feed, like, retweet and subscribe to the authors of posts (high level of randomization). <br>

## Features
1. Post tweets
2. Subscribe to random accounts from the list
3. Subscribe to all accounts specified as required
4. Surf the feed, like, retweet, subscribe to authors
5. Dodge Twitter pop-ups

## Pros
1. Randomization of the coordinates at which the button is clicked
2. Randomization of text input in the text fields
3. Delays randomization
4. Randomization of the sequence of performing different types of activities
5. AdsPower support
6. Reports in the form of screenshots
7. Profile status checks (open / closed), customized bot actions in case when profile was already opened by a user (work / skip)
8. 🔥 Activities in the feed (like, retweet, subscribe)

## Cons
1. Single-threaded

## Script logic
1. An AdsPower profile is randomly selected
2. The warm-up scenario starts according to the settings
   1. Checking profile status (open / closed). If the profile was already open, it can be warmed up or skipped (depending on the user settings)
   2. Opening a profile if it was closed
   3. Randomization of activities (tweet, random subscriptions, mandatory subscriptions, feed surfing)
   4. All activities are randomly performed
   5. Closing a profile in case it was opened by bot
3. Next profile

## First start
1. Install Python 3.10
2. Download the repository
3. Open a terminal, navigate to the folder with the files and run the command "pip install -r requirements.txt"
4. Open the file "data/config.py" using any text editor and adjust the randomization settings
5. Open the file "data/profile_ids.py" using any text editor and enter all required information about the AdsPower profiles ("any_name":"AdsPower ID")
6. Open the file "data/tweets.txt" and upload the tweets base. You can generate tweets using ChatGPT. The fewer tweets, the more often they will be repeated, as they are chosen randomly
7. Open the file "data/twitter_handles.txt" and enter your Twitter usernames there so that they correspond to the accounts entered in the file “data/profile_ids.py”
8. Open the file "data/random_users_to_follow" and enter Twitter usernames (without "@"). This will be the list for random subscriptions
9. Run the command "python3 adspower_twitter_warmup.py" in your terminal


# RU
## Скрипт для прогрева ваших Твиттеров, которые импортированны в ферму AdsPower
Все понимают, что Твиттеры нужно греть. Я периодически прогреваю свои акки и за 8 месяцев у меня отлетело всего 4 штуки (покупал их по USD 0.12). Этот скрипт поможет сэкономить тебе бешенное количество времени и немного денег. Он работает с профилями Twitter, которые импортированны в [AdsPower](https://share.adspower.net/Btc9YYgpiyJxhmW).

Связь с создателем: https://t.me/CrytoBusher <br>
Если ты больше по Твиттеру: https://twitter.com/CryptoBusher <br>

Залетай сюда, чтоб не пропускать дропы подобных скриптов: https://t.me/CryptoKiddiesClub <br>
И сюда, чтоб общаться с крутыми ребятами: https://t.me/CryptoKiddiesChat <br>

## 🔥 Последние обновления
- [x] 20.06.2023 - Добавлена функция подписки на рандомные аккаунты из базы <br>
- [x] 20.06.2023 - Добавлена функция подписки на обязательные аккаунты из списка <br>
- [x] 20.06.2023 - Обновлен сценарий, добавлена рандомизация всех видов активностей <br>
- [x] 20.06.2023 - Скрипт теперь проверяет, открыт ли профиль пользователем, если открыт - может его скипнуть или прогреть <br>
- [x] 04.08.2023 - Скрипт детектит всплывающие модалки и закрывает их. Закрытие модалок настраивается пользователем. <br>
- [x] 04.08.2023 - Скрипт теперь умеет гулять по ленте, лайкать, ретвитить и подписываться на авторов постов. Максимальная рандомизация серфинга ленты. <br>

## Функции
1. Постинг твитов
2. Подписка на рандомные аккаунты из списка
3. Подписка на все аккаунты, указанные как обязательные
4. Серфинг летны с рандомным лайком, ретвитом и подпиской на автора поста
5. Закрытие всплывающих окон Твиттера

## Преимущества
1. Рандомизация координат, по которым производится клик по кнопке
2. Рандомизация ввода текста в поле для твита
3. Рандомизация других задержек
4. Рандомизация последовательности выполнения разного вида активностей
5. Работа через AdsPower
6. Отчетность в виде скриншотов
7. Проверка статуса профиля (открыт / закрыт), настройка работы с кейсом, когда профиль уже открыт пользователем (пропустить, прогреть)
8. 🔥 Активность в ленте (лайк, ретвит, подписка)

## Недостатки
1. Однопоточность

## Логика работы
1. Рандомно выбирается профиль AdsPower
2. Запускается сценарий прогрева согласно настройкам
   1. Проверка статуса профиля (открыт / закрыт). Если профиль уже открыт - производится либо прогрев либо пропуск (в зависимости от настроек)
   2. Запуск профиля, если он был закрыт
   3. Рандомизация активностей (твит, рандомные подписки, обязательные подписки, серфинг ленты)
   4. Производятся все активности, которые выбраны пользователем, согласно рандомному порядку
   5. Закрытие профиля, если он не был ранее открыт. Если профиль уже был открыт - он не закрывается
3. Повтор с новым профилем

## Первый запуск
1. Устанавливаем Python 3.10
2. Качаем репозиторий
3. Открываем терминал, переходим в папку с файлами и пишем команду "pip install -r requirements.txt"
4. Открываем файл "data/config.py" с помощью любого текстового редактора и подбиваем настройки рандомизации
5. Открываем файл "data/profile_ids.py" с помощью любого текстового редактора и забиваем свои профиля как в примере ("название":"ID из AdsPower")
6. Открываем файл "data/tweets.txt" и закидываем базу твитов. Нагенерить можно самому, на фрилансе или в ChatGPT. Чем меньше твитов - тем чаще они будут повторяться, тк они выбираются рандомом
7. Открываем файл "data/twitter_handles.txt" и забиваем туда свои Twitter Username, так, чтоб они соответствовали аккаунтам, вбитым в файл "data/profile_ids.py".
8. Открываем файл "data/random_users_to_follow" и забиваем туда юзернеймы аккаунтов (без @). Это будет база для рандомных подписок
9. В терминале, находясь в папке проекта, вписываем команду "python3 adspower_twitter_warmup.py" и жмем ENTER
