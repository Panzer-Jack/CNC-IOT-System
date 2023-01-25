
SECRET_KEY = "DAS<:WDIONIZCNISDSD_)+UWHAI"

# 数据库的配置信息
HOSTNAME = "127.0.0.1"
PORT = 3306
USERNAME = "root"
PASSWORD = "123456123"
DATABAEE = "zhihu_simple"

DB_URI = \
    f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:" \
    f"{PORT}/{DATABAEE}?charset=utf8"
SQLALCHEMY_DATABASE_URI = DB_URI


# 邮箱配置
# RHGEXLBHKWDRJFMY
MAIL_SERVER = "imap.exmail.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "panzer_jack@panzer-jack.cn"
MAIL_PASSWORD = "sHEN20020311"
MAIL_DEFAULT_SENDER = "panzer_jack@panzer-jack.cn"
