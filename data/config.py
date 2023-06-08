config = {
    # запускать браузер в скрытом режиме (True / False)
    "headless": True,

    # сколько профилей прогреть
    "profiles_to_warmup": 10,

    # пауза между аккаунтами в минутах
    "min_idle_minutes": 10,
    "max_idle_minutes": 30,

    # пауза перед следующим действием в рамках прогрева
    "min_random_pause_sec": 4,
    "max_random_pause_sec": 15,

    # пауза между вводом символов в процессе печатания
    "min_typing_pause_seconds": 0.02,
    "max_typing_pause_seconds": 0.8,

    # селениум кликает всегда в один и тот же пиксель, этот параметр отвечает
    # за максимальное рандомное отклонение от этого пикселя (0 - 1)
    "max_height_deviation": 0.1,
    "max_widht_deviation": 0.1
}
