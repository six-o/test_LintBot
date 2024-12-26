from linebot.models import MessageEvent, TextMessage, TextSendMessage, FlexSendMessage, TemplateSendMessage, ImageCarouselTemplate, ImageCarouselColumn, URIAction, BubbleContainer, QuickReply, QuickReplyButton, MessageAction, PostbackAction, PostbackEvent
from linebot.exceptions import InvalidSignatureError
from linebot import LineBotApi, WebhookHandler
from flask import request, abort
from flask import Flask, jsonify
from flask import render_template
import sqlite3
import os
app = Flask(__name__)

# Reference other modules as needed

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
                    "type": "postback",
                    "label": "查看黑芝麻乳酪",
                    "data": "action=view&itemId=1"
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
    },
    {  # 第二份:蛋糕吐司
        "type": "bubble",
        "hero": {
            "type": "image",
            "url": "https://shoplineimg.com/63e0b4ffec1ae90043e78120/652910397bfa4e000e75d18f/800x.webp?source_format=jpg",
            "size": "full",
                "aspectRatio": "16:12",
                "aspectMode": "cover",
                "action": {
                    "type": "postback",
                    "label": "查看蛋糕吐司",
                    "data": "action=view&itemId=2"
                }
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "蛋糕吐司",
                    "weight": "bold",
                    "size": "xl"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                            {
                                "type": "text",
                                        "text": "價格： NT$108"
                            },
                        {
                                "type": "text",
                                        "text": "營養資訊："
                        },
                        {
                                "type": "text",
                                        "text": "熱量：200-250 大卡"
                        },
                        {
                                "type": "text",
                                        "text": "蛋白質：3-4 克"
                        },
                        {
                                "type": "text",
                                        "text": "碳水化合物：20-25 克"
                        },
                        {
                                "type": "text",
                                        "text": "膳食纖維：1 克"
                        },
                        {
                                "type": "text",
                                        "text": "脂肪：12-15 克"
                        },
                        {
                                "type": "text",
                                        "text": "鈉：100-150 毫克"
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
                                    "uri": "https://www.windsor.com.tw/products/5030100020"
                                }
                    }
            ],
            "flex": 0
        }
    },
    {  # 第三份:奶皇芋頭麻吉爆漿吐司
        "type": "bubble",
        "hero": {
            "type": "image",
            "url": "https://shoplineimg.com/63e0b4ffec1ae90043e78120/6703a5dc7fd394c616e71901/800x.webp?source_format=jpg",
            "size": "full",
                "aspectRatio": "16:12",
                "aspectMode": "cover",
                "action": {
                    "type": "postback",
                    "label": "查看奶皇芋頭麻吉爆漿吐司",
                    "data": "action=view&itemId=3"
                }
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "奶皇芋頭麻吉爆漿吐司",
                    "weight": "bold",
                    "size": "xl"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                            {
                                "type": "text",
                                        "text": "價格： NT$128"
                            },
                        {
                                "type": "text",
                                        "text": "營養資訊："
                        },
                        {
                                "type": "text",
                                        "text": "熱量：250-280 大卡"
                        },
                        {
                                "type": "text",
                                        "text": "蛋白質：4-5 克"
                        },
                        {
                                "type": "text",
                                        "text": "碳水化合物：25-30 克"
                        },
                        {
                                "type": "text",
                                        "text": "膳食纖維：1 克"
                        },
                        {
                                "type": "text",
                                        "text": "脂肪：15-18 克"
                        },
                        {
                                "type": "text",
                                        "text": "鈉：250-300 毫克"
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
                                    "uri": "https://www.windsor.com.tw/products/5020100024"
                                }
                    }
            ],
            "flex": 0
        }
    },
    {  # 第四份:肉鬆沙拉麵包
        "type": "bubble",
        "hero": {
            "type": "image",
            "url": "https://shoplineimg.com/63e0b4ffec1ae90043e78120/64df0c7d06e855001fdebb5c/800x.webp?source_format=png",
            "size": "full",
                "aspectRatio": "16:12",
                "aspectMode": "cover",
                "action": {
                    "type": "postback",
                    "label": "查看肉鬆沙拉麵包",
                    "data": "action=view&itemId=4"
                }
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "肉鬆沙拉麵包",
                    "weight": "bold",
                    "size": "xl"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                            {
                                "type": "text",
                                        "text": "價格： NT$38"
                            },
                        {
                                "type": "text",
                                        "text": "營養資訊："
                        },
                        {
                                "type": "text",
                                        "text": "熱量：350-400 大卡"
                        },
                        {
                                "type": "text",
                                        "text": "蛋白質：4-6 克"
                        },
                        {
                                "type": "text",
                                        "text": "碳水化合物：40-45 克"
                        },
                        {
                                "type": "text",
                                        "text": "膳食纖維：2 克"
                        },
                        {
                                "type": "text",
                                        "text": "脂肪：18-22 克"
                        },
                        {
                                "type": "text",
                                        "text": "鈉：250-300 毫克"
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
                                    "uri": "https://www.windsor.com.tw/products/5010100011"
                                }
                    }
            ],
            "flex": 0
        }
    },
    {  # 第五份:香蔥麵包
        "type": "bubble",
        "hero": {
            "type": "image",
            "url": "https://shoplineimg.com/63e0b4ffec1ae90043e78120/64df0b4ccc5b5a0013dc2db2/800x.webp?source_format=png",
            "size": "full",
                "aspectRatio": "16:12",
                "aspectMode": "cover",
                "action": {
                    "type": "postback",
                    "label": "查看香蔥麵包",
                    "data": "action=view&itemId=5"
                }
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "香蔥麵包",
                    "weight": "bold",
                    "size": "xl"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                            {
                                "type": "text",
                                        "text": "價格： NT$35"
                            },
                        {
                                "type": "text",
                                        "text": "營養資訊："
                        },
                        {
                                "type": "text",
                                        "text": "熱量：200-250 大卡"
                        },
                        {
                                "type": "text",
                                        "text": "蛋白質：4-5 克"
                        },
                        {
                                "type": "text",
                                        "text": "碳水化合物：20-25 克"
                        },
                        {
                                "type": "text",
                                        "text": "膳食纖維：3-4 克"
                        },
                        {
                                "type": "text",
                                        "text": "脂肪：10-15 克"
                        },
                        {
                                "type": "text",
                                        "text": "鈉：80-100 毫克"
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
                                    "uri": "https://www.windsor.com.tw/products/5010300012"
                                }
                    }
            ],
            "flex": 0
        }
    },
    {  # 第六份:葡式蛋塔
        "type": "bubble",
        "hero": {
            "type": "image",
            "url": "https://shoplineimg.com/63e0b4ffec1ae90043e78120/64d5e5eb8b6587001c29d4a5/800x.webp?source_format=png",
            "size": "full",
                "aspectRatio": "16:12",
                "aspectMode": "cover",
                "action": {
                    "type": "postback",
                    "label": "查看葡式蛋塔",
                    "data": "action=view&itemId=6"
                }
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "葡式蛋塔",
                    "weight": "bold",
                    "size": "xl"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                            {
                                "type": "text",
                                        "text": "價格： NT$39"
                            },
                        {
                                "type": "text",
                                        "text": "營養資訊："
                        },
                        {
                                "type": "text",
                                        "text": "熱量：250-280 大卡"
                        },
                        {
                                "type": "text",
                                        "text": "蛋白質：4-5 克"
                        },
                        {
                                "type": "text",
                                        "text": "碳水化合物：20-25 克"
                        },
                        {
                                "type": "text",
                                        "text": "膳食纖維：0.5-1 克"
                        },
                        {
                                "type": "text",
                                        "text": "脂肪：15-18 克"
                        },
                        {
                                "type": "text",
                                        "text": "鈉：150-200 毫克"
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
                                    "uri": "https://www.windsor.com.tw/products/5030100048"
                                }
                    }
            ],
            "flex": 0
        }
    },
    {  # 第七份:牛奶蔓越莓軟歐
        "type": "bubble",
        "hero": {
            "type": "image",
            "url": "https://shoplineimg.com/63e0b4ffec1ae90043e78120/64d5d0d3ba48730019a8b5a6/800x.webp?source_format=png",
            "size": "full",
                "aspectRatio": "16:12",
                "aspectMode": "cover",
                "action": {
                    "type": "postback",
                    "label": "查看牛奶蔓越莓軟歐",
                    "data": "action=view&itemId=7"
                }
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "牛奶蔓越莓軟歐",
                    "weight": "bold",
                    "size": "xl"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                            {
                                "type": "text",
                                        "text": "價格： NT$58"
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
                                        "text": "蛋白質：6-8 克"
                        },
                        {
                                "type": "text",
                                        "text": "碳水化合物：45-50 克"
                        },
                        {
                                "type": "text",
                                        "text": "膳食纖維：2-3 克"
                        },
                        {
                                "type": "text",
                                        "text": "脂肪：4-6 克"
                        },
                        {
                                "type": "text",
                                        "text": "鈉：200-250 毫克"
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
                                    "uri": "https://www.windsor.com.tw/products/5030100048"
                                }
                    }
            ],
            "flex": 0
        }
    },
    {  # 第八份:蔓越莓奶酥吐司
        "type": "bubble",
        "hero": {
            "type": "image",
            "url": "https://shoplineimg.com/63e0b4ffec1ae90043e78120/64d5ccd5f6800100194a2a37/800x.webp?source_format=png",
            "size": "full",
                "aspectRatio": "16:12",
                "aspectMode": "cover",
                "action": {
                    "type": "postback",
                    "label": "查看蔓越莓奶酥吐司",
                    "data": "action=view&itemId=8"
                }
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "蔓越莓奶酥吐司",
                    "weight": "bold",
                    "size": "xl"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                            {
                                "type": "text",
                                        "text": "價格： NT$95"
                            },
                        {
                                "type": "text",
                                        "text": "營養資訊："
                        },
                        {
                                "type": "text",
                                        "text": "熱量：220-260 大卡"
                        },
                        {
                                "type": "text",
                                        "text": "蛋白質：4-5 克"
                        },
                        {
                                "type": "text",
                                        "text": "碳水化合物：30-35 克"
                        },
                        {
                                "type": "text",
                                        "text": "膳食纖維：1-2 克"
                        },
                        {
                                "type": "text",
                                        "text": "脂肪：8-10 克"
                        },
                        {
                                "type": "text",
                                        "text": "鈉：150-200 毫克"
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
                                    "uri": "https://www.windsor.com.tw/products/5020100020"
                                }
                    }
            ],
            "flex": 0
        }
    },
    {  # 第九份:葡萄吐司
        "type": "bubble",
        "hero": {
            "type": "image",
            "url": "https://shoplineimg.com/63e0b4ffec1ae90043e78120/64d5cc7d886500001cf2d629/800x.webp?source_format=png",
            "size": "full",
                "aspectRatio": "16:12",
                "aspectMode": "cover",
                "action": {
                    "type": "postback",
                    "label": "查看葡萄吐司",
                    "data": "action=view&itemId=9"
                }
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "葡萄吐司",
                    "weight": "bold",
                    "size": "xl"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                            {
                                "type": "text",
                                        "text": "價格： NT$95"
                            },
                        {
                                "type": "text",
                                        "text": "營養資訊："
                        },
                        {
                                "type": "text",
                                        "text": "熱量：180-220 大卡"
                        },
                        {
                                "type": "text",
                                        "text": "蛋白質：4-5 克"
                        },
                        {
                                "type": "text",
                                        "text": "碳水化合物：30-35 克"
                        },
                        {
                                "type": "text",
                                        "text": "膳食纖維：1-2 克"
                        },
                        {
                                "type": "text",
                                        "text": "脂肪：3-5 克"
                        },
                        {
                                "type": "text",
                                        "text": "鈉：100-150 毫克"
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
                                    "uri": "https://www.windsor.com.tw/products/5020100006"
                                }
                    }
            ],
            "flex": 0
        }
    },
    {  # 第十份:檸檬蛋糕
        "type": "bubble",
        "hero": {
            "type": "image",
            "url": "https://shoplineimg.com/63e0b4ffec1ae90043e78120/64d5e22237005b0010f51563/800x.webp?source_format=png",
            "size": "full",
                "aspectRatio": "16:12",
                "aspectMode": "cover",
                "action": {
                    "type": "postback",
                    "label": "查看檸檬蛋糕",
                    "data": "action=view&itemId=10"
                }
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "檸檬蛋糕",
                    "weight": "bold",
                    "size": "xl"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                            {
                                "type": "text",
                                        "text": "價格： NT$26"
                            },
                        {
                                "type": "text",
                                        "text": "營養資訊："
                        },
                        {
                                "type": "text",
                                        "text": "熱量：220-270 大卡"
                        },
                        {
                                "type": "text",
                                        "text": "蛋白質：3-4 克"
                        },
                        {
                                "type": "text",
                                        "text": "碳水化合物：30-35 克"
                        },
                        {
                                "type": "text",
                                        "text": "膳食纖維：1 克以下"
                        },
                        {
                                "type": "text",
                                        "text": "脂肪：10-15 克"
                        },
                        {
                                "type": "text",
                                        "text": "鈉：150-200 毫克"
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
                                    "uri": "https://www.windsor.com.tw/products/5030100008"
                                }
                    }
            ],
            "flex": 0
        }
    }
]


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"


# line_bot_api = LineBotApi(
#     "z2uS3YGDyn589qxGU6NgU4/DTn9y+FU69lgm9BHvE6ma+nWSdxgCeVour9cjljF+6zEM8tK+tT34V5s904nvfaGDLgUqIXJOyg/fMKYJmAx8zoMhhkF8aTb0QRkG/46xfAvQQjBPO72sXKVRy4T6dgdB04t89/1O/w1cDnyilFU=")
# handler = WebhookHandler("6a80dfb05eccbe33d199d3497e7ef0a3")
line_bot_api = LineBotApi(os.environ.get('Channel_Access_Token'))
handler = WebhookHandler(os.environ.get('Channel_Secret'))

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:12345678@localhost/project'

# liffid = '2006706294-ng4Jr96g'
# LIFF Endpoint


@app.route("/liff", methods=["GET"])
def liff_page():
    return render_template("book.html")


@app.route("/liff2", methods=["GET"])
def liff_page2():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    data = request.json  # 取得前端傳來的 JSON 資料
    username = data.get("username")
    password = data.get("password")

    # 模擬用戶資料
    # users = {
    #     "admin": {"password": "123456", "name": "管理員"},
    #     "user": {"password": "password", "name": "普通用戶"}
    # }
    conn = sqlite3.connect('project.sqlite')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM users WHERE username = ? AND password = ?
    ''', (username, password))
    user = cursor.fetchone()  # 取得查詢結果

    if user:
        return jsonify({"status": "success", "name": username})  # 驗證成功
    else:
        return jsonify({"status": "fail", "message": "帳號或密碼錯誤"})  # 驗證失敗
    conn.close()

    # # 驗證帳號與密碼
    # if username in users and users[username]["password"] == password:
    #     return jsonify({"status": "success", "name": users[username]["name"]})
    # else:
    #     return jsonify({"status": "fail", "message": "帳號或密碼錯誤"})


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    mtext = event.message.text
    if mtext == "@熱門商品":
        popular_items(event)
    elif mtext == "@所有商品":
        All_items(event)
    elif mtext == "@官方網站":
        WebSite(event)
    elif mtext == "@門市資訊":
        Local(event)
    # elif mtext == '@隨機推薦':


@handler.add(PostbackEvent)
def handle_postback(event):
    data = event.postback.data
    params = {kv.split('=')[0]: kv.split('=')[1] for kv in data.split('&')}
    action = params.get("action")
    item_id = params.get("itemId")

    if action == "view":
        # 根據 item_id 返回商品詳細資訊
        product_details = bubble_data[int(item_id) - 1]  # 提取商品 Flex Message
        detailed_message = FlexSendMessage(
            alt_text="商品詳細資訊",
            contents=product_details
        )
        line_bot_api.reply_message(event.reply_token, detailed_message)
    else:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text="無法處理的操作。")
        )


def popular_items(event):
    try:
        message = TemplateSendMessage(
            alt_text='Carousel template',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://shoplineimg.com/63e0b4ffec1ae90043e78120/64df0c7d06e855001fdebb5c/800x.webp?source_format=png',
                        action=PostbackAction(
                            label='肉鬆沙拉麵包', data='action=view&itemId=4')
                    ),
                    ImageCarouselColumn(
                        image_url='https://shoplineimg.com/63e0b4ffec1ae90043e78120/64df0b4ccc5b5a0013dc2db2/800x.webp?source_format=png',
                        action=PostbackAction(
                            label='香蔥麵包', data='action=view&itemId=5')
                    ),
                    ImageCarouselColumn(
                        image_url='https://shoplineimg.com/63e0b4ffec1ae90043e78120/64d5e5eb8b6587001c29d4a5/800x.webp?source_format=png',
                        action=PostbackAction(
                            label='葡式蛋塔', data='action=view&itemId=6')
                    ),
                    ImageCarouselColumn(
                        image_url='https://shoplineimg.com/63e0b4ffec1ae90043e78120/64d5e22237005b0010f51563/800x.webp?source_format=png',
                        action=PostbackAction(
                            label='檸檬蛋糕', data='action=view&itemId=10')

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
                        image_url='https://shoplineimg.com/63e0b4ffec1ae90043e78120/652910397bfa4e000e75d18f/800x.webp?source_format=jpg',
                        action=URIAction(
                            label='蛋糕吐司', uri='https://www.windsor.com.tw/products/5030100020')
                    ),
                    ImageCarouselColumn(
                        image_url='https://shoplineimg.com/63e0b4ffec1ae90043e78120/6703a5dc7fd394c616e71901/800x.webp?source_format=jpg',
                        action=URIAction(
                            label='奶皇芋頭麻吉爆漿吐司', uri='https://www.windsor.com.tw/products/5020100024')
                    ),
                    ImageCarouselColumn(
                        image_url='https://shoplineimg.com/63e0b4ffec1ae90043e78120/64df0c7d06e855001fdebb5c/800x.webp?source_format=png',
                        action=URIAction(
                            label='肉鬆沙拉麵包', uri='https://www.windsor.com.tw/products/5010100011')
                    ),
                    ImageCarouselColumn(
                        image_url='https://shoplineimg.com/63e0b4ffec1ae90043e78120/64df0b4ccc5b5a0013dc2db2/800x.webp?source_format=png',
                        action=URIAction(
                            label='香蔥麵包', uri='https://www.windsor.com.tw/products/5010300012')
                    ),
                    ImageCarouselColumn(
                        image_url='https://shoplineimg.com/63e0b4ffec1ae90043e78120/64d5e5eb8b6587001c29d4a5/800x.webp?source_format=png',
                        action=URIAction(
                            label='葡式蛋塔', uri='https://www.windsor.com.tw/products/5030100048')
                    ),
                    ImageCarouselColumn(
                        image_url='https://shoplineimg.com/63e0b4ffec1ae90043e78120/64d5d0d3ba48730019a8b5a6/800x.webp?source_format=png',
                        action=URIAction(
                            label='牛奶蔓越莓軟歐', uri='https://www.windsor.com.tw/products/5020300023')
                    ),
                    ImageCarouselColumn(
                        image_url='https://shoplineimg.com/63e0b4ffec1ae90043e78120/64d5ccd5f6800100194a2a37/800x.webp?source_format=png',
                        action=URIAction(
                            label='蔓越莓奶酥吐司', uri='https://www.windsor.com.tw/products/5020100020')
                    ),
                    ImageCarouselColumn(
                        image_url='https://shoplineimg.com/63e0b4ffec1ae90043e78120/64d5cc7d886500001cf2d629/800x.webp?source_format=png',
                        action=URIAction(
                            label='葡萄吐司', uri='https://www.windsor.com.tw/products/5020100006')
                    ),
                    ImageCarouselColumn(
                        image_url='https://shoplineimg.com/63e0b4ffec1ae90043e78120/64d5e22237005b0010f51563/800x.webp?source_format=png',
                        action=URIAction(
                            label='檸檬蛋糕', uri='https://www.windsor.com.tw/products/5030100008')
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
                    ),
                    QuickReplyButton(
                        action=URIAction(
                            label='基隆市仁愛區仁二路', uri='https://maps.app.goo.gl/AULMRmijC4A3bc377')
                    ),
                    QuickReplyButton(
                        action=URIAction(
                            label='基隆市安樂區', uri='https://maps.app.goo.gl/gtRBGY3jojBMSAvt6')
                    ),
                    QuickReplyButton(
                        action=URIAction(
                            label='基隆市七堵區', uri='https://maps.app.goo.gl/KWfGDLtaANRVnExQ7')
                    ),
                    QuickReplyButton(
                        action=URIAction(
                            label='新北市汐止區', uri='https://maps.app.goo.gl/qG5haVGyt2n9CNgV7')
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text="發生錯誤!"))


if __name__ == "__main__":
    app.run(port=5001)
