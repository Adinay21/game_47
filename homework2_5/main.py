from decouple import Config
from logic import start_game


config = Config('settings.ini')


range_min = config('range_min', default=1, cast=int)
range_max = config('range_max', default=100, cast=int)
attempts = config('attempts', default=5, cast=int)
starting_balance = config('starting_balance', default=1000, cast=int)


if __name__ == "__main__":
    start_game(range_min, range_max, attempts, starting_balance)
