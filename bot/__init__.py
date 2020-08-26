import requests
from bot.constants import BASE_ENDPOINT
import cli.app

@cli.app.CommandLineApp
def bot(app):
    ping_response = requests.get(BASE_ENDPOINT+'api/v3/ping')
    print(f'{ping_response}:{ping_response.json()}')


# bot.add_param("-h", "--help", help="HELP me")


if __name__ == '__main__':
    bot.run()
