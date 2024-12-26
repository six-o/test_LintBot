import random
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FlexSendMessage, TemplateSendMessage, ImageCarouselTemplate, ImageCarouselColumn, URIAction, BubbleContainer, QuickReply, QuickReplyButton, MessageAction, RichMenu, RichMenuSize, RichMenuBounds, RichMenuArea
from linebot.exceptions import InvalidSignatureError
from linebot import LineBotApi, WebhookHandler
from flask import request, abort
from flask import Flask
app = Flask(__name__)

# Reference other modules as needed


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"


line_bot_api = LineBotApi(
    "Y8+zGvZUu9Lutlz3hjSKViMgIhhszAHOWeBFXiQ6B0RTONa6/+Y+Zu06wWB15Ek1ywhH0+Q+lihORblPakReWsBhcJavlsJMGZvEKScOxGtZdfYcTQvg5NsjfWSyhHDH73LEhSOmK5hdBwswcUVB+AdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("a120a3af12eaceb3006e2d9a85573e64")


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    mtext = event.message.text
    if mtext == "@熱門品項":
        Popular_items(event)
    elif mtext == "@所有品項":
        All_items(event)
    elif mtext == "@官方網站":
        WebSite(event)
    # elif mtext == "@隨機推薦":
    # 	Random_Recommend()
    elif mtext == "@門市資訊":
        Local(event)
    elif mtext == '@隨機推薦':
        try:
            bubble_data = [
                {  # 第一份:黑芝麻乳酪
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://shoplineimg.com/63e0b4ffec1ae90043e78120/65291149870830001a1d8d82/800x.webp?source_format=png",
                            "size": "full",
                            "aspectRatio": "16:12",
                            "aspectMode": "cover",
                            "action": {
                                "type": "uri",
                                "uri": "https://shoplineimg.com/63e0b4ffec1ae90043e78120/65291149870830001a1d8d82/800x.webp?source_format=png"
                            }
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "黑芝麻乳酪",
                                "weight": "bold",
                                "size": "xl"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                        {
                                            "type": "text",
                                                    "text": "價格： NT$85"
                                        },
                                    {
                                            "type": "text",
                                                    "text": "營養資訊："
                                    },
                                    {
                                            "type": "text",
                                                    "text": "熱量：250-300 大卡"
                                    },
                                    {
                                            "type": "text",
                                                    "text": "蛋白質：8-10 克"
                                    },
                                    {
                                            "type": "text",
                                                    "text": "碳水化合物：50-55 克"
                                    },
                                    {
                                            "type": "text",
                                                    "text": "膳食纖維：2-3 克"
                                    },
                                    {
                                            "type": "text",
                                                    "text": "脂肪：1-2 克"
                                    },
                                    {
                                            "type": "text",
                                                    "text": "鈉：400-500 毫克"
                                    }
                                ]
                            }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                                {
                                    "type": "button",
                                    "style": "link",
                                    "height": "sm",
                                            "action": {
                                                "type": "uri",
                                                "label": "訂購",
                                                "uri": "https://www.windsor.com.tw/products/5020300002"
                                            }
                                }
                        ],
                        "flex": 0
                    }
                }
            ]
            ran_Number = random.randint(0, 9)
            print(ran_Number)
            line_bot_api.reply_message(event.reply_token, FlexSendMessage(
                alt_text='Flex Message', contents=bubble_data[ran_Number]))
        except:
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text="發生錯誤!"))


def Popular_items(event):
    try:
        message = TemplateSendMessage(
            alt_text='Carousel template',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://shoplineimg.com/63e0b4ffec1ae90043e78120/64df0c7d06e855001fdebb5c/800x.webp?source_format=png',
                        action=URIAction(
                            label='肉鬆沙拉麵包', uri='https://www.windsor.com.tw/products/5010100011')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text="發生錯誤!"))


def All_items(event):
    try:
        message = TemplateSendMessage(
            alt_text='Carousel template',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://shoplineimg.com/63e0b4ffec1ae90043e78120/65291149870830001a1d8d82/800x.webp?source_format=png',
                        action=URIAction(
                            label='黑芝麻乳酪', uri='https://www.windsor.com.tw/products/5020300002')
                    ),
                    ImageCarouselColumn(
                        image_url='https://shoplineimg.com/63e0b4ffec1ae90043e78120/65291149870830001a1d8d82/800x.webp?source_format=png',
                        action=URIAction(
                            label='黑芝麻乳酪', uri='https://www.windsor.com.tw/products/5020300002')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text="發生錯誤!"))


def WebSite(event):
    try:
        message = TextSendMessage(
            text="官網: https://www.windsor.com.tw/"
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text="發生錯誤!"))


def Local(event):
    try:
        message = TextSendMessage(
            text="請選擇你想去的地點 \n 也可前往此網址，瞭解更詳細 https://www.windsor.com.tw/pages/store",
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=URIAction(
                            label='基隆市仁愛區忠一路', uri='https://maps.app.goo.gl/BKWyZUJ8ecZrcNEy9')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text="發生錯誤!"))


@app.route('/create_rich_menu', methods=['POST'])
def create_rich_menu():
    try:
        # 創建圖文選單結構
        rich_menu_to_create = RichMenu(
            size=RichMenuSize(width=2500, height=1686),  # 圖文選單大小
            selected=True,
            name="Sample Rich Menu",  # 圖文選單名稱
            chat_bar_text="Menu",  # 下方選單文字
            areas=[
                RichMenuArea(  # 第一個點擊區域
                    bounds=RichMenuBounds(x=0, y=0, width=833, height=843),
                    action=MessageAction(label="@熱門商品", text="@熱門商品")
                ),
                RichMenuArea(  # 第二個點擊區域
                    bounds=RichMenuBounds(x=833, y=0, width=833, height=843),
                    action=MessageAction(label="@所有商品", text="@所有商品")
                ),
                RichMenuArea(  # 第一個點擊區域
                    bounds=RichMenuBounds(x=1666, y=0, width=833, height=843),
                    action=MessageAction(label="@隨機推薦", text="@隨機推薦")
                ),
                RichMenuArea(  # 第二個點擊區域
                    bounds=RichMenuBounds(x=0, y=843, width=833, height=843),
                    action=MessageAction(label="@官方網站", text="@官方網站")
                ),
                RichMenuArea(  # 第一個點擊區域
                    bounds=RichMenuBounds(x=833, y=843, width=833, height=843),
                    action=MessageAction(label="@門市資訊", text="@門市資訊")
                ),
                RichMenuArea(  # 第二個點擊區域
                    bounds=RichMenuBounds(
                        x=1666, y=843, width=833, height=843),
                    action=MessageAction(label="@集點卡", text="@集點卡")
                )
            ]
        )

        # 上傳圖文選單結構
        rich_menu_id = line_bot_api.create_rich_menu(
            rich_menu=rich_menu_to_create)

        # 上傳圖文選單圖片
        with open('0hInLGlT.jpg', 'rb') as f:
            line_bot_api.set_rich_menu_image(rich_menu_id, 'image/jpeg', f)

        # 設置為全域預設圖文選單
        line_bot_api.set_default_rich_menu(rich_menu_id)

        return f"Rich Menu created with ID: {rich_menu_id}"

    except Exception as e:
        return f"Error: {str(e)}"

# 處理 Postback 事件


if __name__ == "__main__":
    app.run(debug=True)
