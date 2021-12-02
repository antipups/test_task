FIRST_NAME_LEN = 32
SECOND_NAME_LEN = 32
THIRD_NAME_LEN = 32

ID_LEN = 32

CLIENT_TYPE_LEN = 16
TIMEZONE_LEN = 16
GENDER_LEN = 16

CLIENT_TYPES = (('первичный', 'первичный'),
                ('повторный', 'повторный'),
                ('внешний', 'внешний'),
                ('косвенный', 'косвенный'))
GENDER = (('мужской', 'мужской'),
          ('женский', 'женский'),
          ('неизвестно', 'неизвестно'))
TIMEZONES = (('Москва', '+3:00'),
             ('Украина', '+4:00'),
             # ...
             )

PHONE_LEN = 20
SOCIAL_NAME_LEN = 16
SOCIAL_ID_LEN = 32

FULL_TITLE_LEN = 64
SHORT_TITLE_LEN = 32
DEPARTMENT_TITLE_LEN = 32
