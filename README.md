# api_yamdb
Групповой проект.

Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»). 

Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). 

Добавлять произведения, категории и жанры может только администратор.

Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.

Пользователи могут оставлять комментарии к отзывам.

Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.

## Наполнение базы данных
Для фиктивного наполнения базы данных используйте в cli команду:
`python manage.py import `

Для удаления всех данных используйте команду:
`python manage.py import -d`

# Над проектом работали:
- https://github.com/mfilinov - team-lead, занимался вопросами:
   - системы регистрации и аутентификации,
   - прав доступа,
   - работы с токеном,
   - системы подтверждения через e-mail.
- https://github.com/evgengurgen - занимался разработкой моделей, viewsets и endpoints:
   - произведений,
   - категорий,
   - жанров;
   - реализации импорта данных из csv файлов.
- https://github.com/Fryzgh - занимался разработкой моделей, viewsets и endpoints:
   - отзывов,
   - комментариев,
   - рейтингов произведений.

 # Ресурсы API YaMDb
  - Ресурс auth: аутентификация.
  - Ресурс users: пользователи.
  - Ресурс titles: произведения, к которым пишут отзывы (определённый фильм, книга или песенка).
  - Ресурс categories: категории (типы) произведений («Фильмы», «Книги», «Музыка»). Одно произведение может быть привязано только к одной категории.
  - Ресурс genres: жанры произведений. Одно произведение может быть привязано к нескольким жанрам.
  - Ресурс reviews: отзывы на произведения. Отзыв привязан к определённому произведению.
  - Ресурс comments: комментарии к отзывам. Комментарий привязан к определённому отзыву.

# Самостоятельная регистрация новых пользователей
  - Пользователь отправляет POST-запрос с параметрами email и username на эндпоинт /api/v1/auth/signup/.
  - Сервис YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на указанный адрес email.
  - Пользователь отправляет POST-запрос с параметрами username и confirmation_code на эндпоинт /api/v1/auth/token/, в ответе на запрос ему приходит token (JWT-токен).
  - В результате пользователь получает токен и может работать с API проекта, отправляя этот токен с каждым запросом. 
  - После регистрации и получения токена пользователь может отправить PATCH-запрос на эндпоинт /api/v1/users/me/ и заполнить поля в своём профайле (описание полей — в документации).
