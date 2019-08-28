import json
import requests
from flask import Flask, request, abort
# from utils import WitAi
# -*- coding: utf-8 -*- 

PAGE_ACCESS_TOKEN = " "  
VERIFY_TOKEN = " "
# bot = Bot(PAGE_ACCESS_TOKEN)

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
    app.logger.debug(data)
    if data["object"] == "page":
        for entry in data["entry"]:

            for messaging_event in entry["messaging"]:

                if messaging_event.get("message"):
                    # 取得event的值
                    sender_id = messaging_event["sender"]["id"]        
                    recipient_id = messaging_event["recipient"]["id"]  
                    message_text = messaging_event["message"]["text"] 
                    nlp_dict = messaging_event["message"]["nlp"]
                    app.logger.debug("--------------------------------")
                    # 處理NLP物件, 回傳信心程度最高的attribute以及內容, 或None
                    entity_list = understand(nlp_dict)
                    app.logger.debug(entity_list)

                    # 根據值取得回覆內容 
                    message_text = response_content(entity_list)
                    app.logger.debug(message_text)

                    # 把回覆內容傳給sender
                    send_text_message(sender_id,message_text)  
        return "ok", 200
    else:
        abort(400)

def understand(nlp_dict):
    entity_dict = nlp_dict["entities"]
    temp_max = -float("inf")
    threshold = 0.7
    entity_list = []
    # 處理 fb 自然語意event
    for key,value in entity_dict.items():
        understand_result = {}
        confidence = value[0]["confidence"]

        if confidence > threshold:
            understand_result["entity"] = key
            understand_result["confidence"] = value[0]["confidence"]
            understand_result["value"] = value[0]["value"]
            
            if key in ["bye","thanks","greetings"]:
                understand_result["body"] = None
            else:    
                understand_result["body"] = value[0]["_body"]
            entity_list.append(understand_result)
        else:
            pass
   
    return entity_list

def response_content(entity_list):  
    if entity_list == []:
     
        message_text = "偵測到0個實體。"


    else:
        entity_num = len(entity_list)
        message_text = "偵測到"+str(entity_num)+"個實體:\n"
        for i in entity_list:
            message_text += i["entity"] +"的信心程度為 "+str(i["confidence"])+"\n"
            # f'偵測到{entity_num}個實體:\n'

    
       
    return message_text

               

def send_text_message(recipient_id, message):

    data=json.dumps({
          "messaging_type":"RESPONSE",
          "recipient": {"id": recipient_id},
          "message": {"text": message}   #決定回什麼話
        })
    params={
        "access_token": PAGE_ACCESS_TOKEN
    }
    headers={
        'Content-type': 'application/json'
    }

    # Send POST request to messenger
    r = requests.post("https://graph.facebook.com/v2.6/me/messages",params=params, headers=headers, data=data)



if __name__ == '__main__':
    # Run Server
    app.run(debug=True)
