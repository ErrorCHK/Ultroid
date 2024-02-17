# Ultroid - UserBot
# Copyright (C) 2021-2023 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.

import sys

from decouple import config

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


class Var:
    # mandatory
    API_ID = (
        int(sys.argv[1]) if len(sys.argv) > 1 else config("24194175", default=6, cast=int)
    )
    API_HASH = (
        sys.argv[2]
        if len(sys.argv) > 2
        else config("d34f50e58d861fe519d9a917c4c1dac8", default="eb06d4abfb49dc3eeb1aeb98ae0f581e")
    )
    SESSION = sys.argv[3] if len(sys.argv) > 3 else config("1BJWap1wBuygzzuFyTltLerdnT7a1EvBYinpOQWja_QuGGGqntSODWTpoktr9tyfAE_JD_0rFvUsqkZ1dqldxyHydTinEuGdOyR5vxTCF4A2Li8ypOv3Xe0EUfYNA1zidNtFOj0JZUsvNhtITduUN22P8KayZ2Xpk6FVNE9cwcAfvan0o_D9e_FGF5S-z16ptyGHhii-lCx_dJo8lUeRcFZVQkS-uEF1aTwpvB8slscVyPTFEsdjQPgqS-yaWUD-mNwsJGzRH26LKYUzxFnwnrJeLvJROxnqIx86lMcUbS_EcX42jVXdYuACbNUHwH9dHuQ7w4Y6SSfW5DkzKiV_wBaJpJ8lUZLk=", default=None)
    REDIS_URI = (
        sys.argv[4]
        if len(sys.argv) > 4
        else (config("redis-18840.c264.ap-south-1-1.ec2.cloud.redislabs.com:18840", default=None) or config("REDIS_URL", default=None))
    )
    REDIS_PASSWORD = (
        sys.argv[5] if len(sys.argv) > 5 else config("RBfDvEt7X18d30ygIqkHaBCQ9wmOZpBV", default=None)
    )
    # extras
    BOT_TOKEN = config("5995230290:AAHuL13pm6i-QU-rpxXD6tHRuQpQKOLslL4", default=None)
    LOG_CHANNEL = config("-1002081863152", default=0, cast=int)
    HEROKU_APP_NAME = config("HEROKU_APP_NAME", default=None)
    HEROKU_API = config("HEROKU_API", default=None)
    VC_SESSION = config("1BJWap1wBuygzzuFyTltLerdnT7a1EvBYinpOQWja_QuGGGqntSODWTpoktr9tyfAE_JD_0rFvUsqkZ1dqldxyHydTinEuGdOyR5vxTCF4A2Li8ypOv3Xe0EUfYNA1zidNtFOj0JZUsvNhtITduUN22P8KayZ2Xpk6FVNE9cwcAfvan0o_D9e_FGF5S-z16ptyGHhii-lCx_dJo8lUeRcFZVQkS-uEF1aTwpvB8slscVyPTFEsdjQPgqS-yaWUD-mNwsJGzRH26LKYUzxFnwnrJeLvJROxnqIx86lMcUbS_EcX42jVXdYuACbNUHwH9dHuQ7w4Y6SSfW5DkzKiV_wBaJpJ8lUZLk=", default=None)
    ADDONS = config("ADDONS", default=False, cast=bool)
    VCBOT = config("6461298155:AAEU7BiisaP7n0v4RiAvZuKfOUD-B5f__ec", default=False, cast=bool)
    # for railway
    REDISPASSWORD = config("RBfDvEt7X18d30ygIqkHaBCQ9wmOZpBV", default=None)
    REDISHOST = config("redis-18840.c264.ap-south-1-1.ec2.cloud.redislabs.com", default=None)
    REDISPORT = config("18840", default=None)
    REDISUSER = config("default", default=None)
    # for sql
    DATABASE_URL = config("postgres://rvwivxyt:rSB363EMKrTEuv3FOx95Ly15BSRbWYDv@kesavan.db.elephantsql.com/rvwivxyt", default=None)
    # for MONGODB users
    MONGO_URI = config("mongodb+srv://errorxd:Error99@cluster0.1p0is05.mongodb.net/?retryWrites=true&w=majority", default=None)
