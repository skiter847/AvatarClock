from datetime import datetime


def progressbar(time: str):
    """
    Вернет строку в виде прогресс бара из параметра text.
    За каждый час к текущему времени который берется из параметра text к строке progressbar прибавляется символ █,
    в ином случает ставится символ ─
    """

    progressbar = ''

    # количество  часов с начала дня
    current_hour = int(time.split(':')[0])

    # левый край прогресс бара
    progressbar += '|'

    for hour in range(1, 25):
        if hour <= current_hour:
            progressbar += '█'
            continue
        progressbar += '─'

    # правая граница прогресс бара
    progressbar += '|'

    return progressbar


def percent(time: str):
    """
    :return количество времени с начала дня в процентах
    """
    second = 0

    hour, minutes = time.split(':')

    # количество секунд с начала дня
    second += (int(hour) * (60 * 60)) + (int(minutes) * 60)

    return str(round(second * 100 / 86400, 2)) + '%'



def current_time():
    return datetime.now().strftime("%H:%M")

