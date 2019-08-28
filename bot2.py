import json
import requests
import utils
from setting import reply
from flask import Flask, request, abort
# from models import app, db, User
from utils import WitAi  

PAGE_ACCESS_TOKEN = " "  
VERIFY_TOKEN = " "
# db.create_all()

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def handle_verify():
    if(request.args.get('hub.verify_token','') == VERIFY_TOKEN):
        print("I'm successed!")
        return request.args.get('hub.challenge','')
    else:
        #app.logger.debug('we are in handle_message()')
        print('wrong verification token')
        return "Error, I'm failed!"

@app.route('/', methods = ['POST'])
def handle_message():
    data = request.get_json()
    # app.logger.debug(data)

    if data["object"] == "page":  # make sure this is a page subscription
        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                
                if messaging_event.get("message"):  # user sent us a message
                    received_message(messaging_event)
                elif messaging_event.get("postback"):
                    received_postback(messaging_event)
                
        return "ok", 200
    else:
        abort(400)

def received_message(messaging_event):
    # 查詢db, 看使用者id是否存在於資料庫
    # 若存在, 判斷使用者這次講的話, 跟上次機器人問的問題是否相關
    # 若不存在, 直接回覆＂我聽不懂＂
    sender_id = messaging_event["sender"]["id"]        # the facebook ID of the person sending you the message
    recipient_id = messaging_event["recipient"]["id"]  # facebook page's ID

    if "text" in messaging_event["message"]:
        message_text = messaging_event["message"]["text"]
        app.logger.debug("-----------------------------")


        # witai = utils.WitAi()
        # entity_list = witai.wit_understand(message_text)
        # app.logger.debug(entity_list)

        # message_text = witai.wit_response(entity_list)                     
        # app.logger.debug(message_text)


        if message_text == "網址按鈕":
            data = {
                "recipient":{
                    "id": sender_id
                }
            }
            data.update(reply["url_button"])
            call_send_api(json.dumps(data))
            
        elif message_text == "回傳按鈕":
            data = {
                "recipient":{
                    "id": sender_id
                }
            }
            data.update(reply["postback_button"])
            call_send_api(json.dumps(data))

        elif message_text == "分享按鈕":
            data = {
                "recipient":{
                    "id": sender_id
                }
            }
            data.update(reply["share_button"])
            call_send_api(json.dumps(data))

        elif message_text == "通話按鈕":
            data = {
                "recipient":{
                    "id": sender_id
                }
            }
            data.update(reply["call_button"])
            call_send_api(json.dumps(data))

        elif message_text == "一般型範本":
            data = {
                "recipient":{
                    "id": sender_id
                }
            }
            data.update(reply["simple_template"])
            call_send_api(json.dumps(data))

        elif message_text == "清單範本":
            data = {
                "recipient":{
                    "id": sender_id
                }
            }
            data.update(reply["list_template"])
            call_send_api(json.dumps(data))
        
        elif message_text == "清單範本例子":
            data = {
                "recipient":{
                    "id": sender_id
                }
            }
            data.update(reply["list_template_example"])
            call_send_api(json.dumps(data))

        elif message_text == "按鈕範本":
            data = {
                "recipient":{
                    "id": sender_id
                }
            }
            data.update(reply["button_template"])
            call_send_api(json.dumps(data))

        elif message_text == "媒體範本":
            data = {
                "recipient":{
                    "id": sender_id
                }
            }
            data.update(reply["media_template"])
            call_send_api(json.dumps(data))

        elif message_text == "比賽10k" :
            data = {
                "recipient":{
                    "id": sender_id
                }
            }
            data.update(reply["10k"])
            call_send_api(json.dumps(data))

        elif message_text == "比賽21k" :
            data = {
                "recipient":{
                    "id": sender_id
                }
            }
            data.update(reply["21k"])
            call_send_api(json.dumps(data))
        
        elif message_text == "減重(待補)" or message_text == "突破個人PB(待補)":
            send_text_message(sender_id, "目前尚未有資料。")
        
        elif message_text == "4週課程" :
            send_text_message(sender_id, "即將為您打造課程。")

        elif message_text == "8週課程" :
            send_text_message(sender_id, "即將為您打造課程。")
        
        elif message_text == "本週課表" :
            send_text_message(sender_id, "即將為您查詢本週課表。")

        elif message_text == "下週課表" :
            send_text_message(sender_id, "即將為您查詢下週課表。")

        # send_text_message(sender_id, message_text)
            
            

    elif "attachments" in messaging_event["message"]:
        send_text_message(sender_id, "傳文字給我啦 ~ ><!")

def received_postback(messaging_event):
    sender_id = messaging_event["sender"]["id"] 
    recipient_id = messaging_event["recipient"]["id"]
    payload = messaging_event["postback"]["payload"]
    app.logger.debug("-----------------------------")
    
   

    if payload == "開始吧!":
        send_text_message(sender_id, "Welcome to Lingbot,我是您專屬的虛擬教練!:")
    elif payload == "打造課程":
        data = {
            "recipient":{
                "id": sender_id
            }
        }
        data.update(reply["generate_program"])
        call_send_api(json.dumps(data))

        
    elif payload == "查詢課程":
        data = {
            "recipient":{
                "id": sender_id
            }
        }
        data.update(reply["query_program"])
        call_send_api(json.dumps(data))

    else:
        send_text_message(sender_id, "Postback called")

# # 插入數據
# def create(sender_id, payload):

#     user = User(sender_id, payload)
#     db.session.add(user)
#     db.session.commit()

# # 查詢指定數據
# def search(sender_id, payload):
#     # 搜尋最新一筆(資料庫中的最後一筆)資料
#     user = User.query.order_by("-id").first()





def send_text_message(recipient_id, message):
    data = json.dumps({
        "recipient":{
            "id":recipient_id
            },
        "message":{
            "text":message
            }
    })
    
    call_send_api(data)
    

def call_send_api(data):
    params = {
        "access_token":PAGE_ACCESS_TOKEN
    }
    headers = {
        "Content-type":"application/json"
    }

    r = requests.post("https://graph.facebook.com/v2.6/me/messages",params=params, headers=headers, data=data)

if __name__ == "__main__":
    app.run(debug=True)