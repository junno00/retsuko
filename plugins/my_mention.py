from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
from plugins.fetch_attendance import Fetch_attend

@respond_to('郵便受け')
def mention_func(message):
    message.reply('右に2回8を回して左に1回2だよ')

#@respond_to('見積もりメール')
#def mention_func(message):
#    msg = '\nいつもお世話になっております。\nMOLCUREの今井淳之介です。\n\n以下の商品のお見積もりをお願いできないでしょうか。\nメーカー名  商品名（型番）  本数\n\nよろしくお願いいたします。'
#    message.reply(msg)

@respond_to('注文メール')
def mention_func(message):
    msg = '\nいつもお世話になっております。\nMOLCUREの今井淳之介です。\n\n先日はお見積もりをいただきありがとうございました。\n以下の商品を注文いたします。\n\nメーカー名  商品名（型番）  本数\n\n納期など分かりましたらお知らせいただけると幸いです。\nよろしくお願いいたします。\n\n今井淳之介\n\n[内部連絡:資金@@@で処理をお願いします。]'
    message.reply(msg)

@respond_to('^([ぁ-んァ-ン]{3})に見積もりメール')
def mention_func(message, something):
    message.reply(something)

@respond_to('^(.*)さん(\d{4})年(\d)月のMOLCURE(\d{3})時間NEDO(\d{3})時間分の勤怠ちょうだい')
def mention_func(message, name, year, month, molcure_total, nedo_total):
    message.reply(name+'さんの'+month+'月の'+hour+'時間分の勤怠だね。')

