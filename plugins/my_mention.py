from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
from plugins.fetch_attendance import Fetch_attend

@respond_to('注文メール')
def mention_func(message):
    msg = '\nいつもお世話になっております。\nXXXです。\n\n先日はお見積もりをいただきありがとうございました。\n以下の商品を注文いたします。\n\nメーカー名  商品名（型番）  本数\n\n納期など分かりましたらお知らせいただけると幸いです。\nよろしくお願いいたします。\n\n今井淳之介'
    message.reply(msg)

@respond_to('^([ぁ-んァ-ン]{3})に見積もりメール')
def mention_func(message, something):
    message.reply(something)

