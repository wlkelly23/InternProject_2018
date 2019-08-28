from wit import Wit

class WitAi(object):

    # 初始化:
    def __init__(self):
        self.client = Wit(access_token = " ")

    # 自訂private function:
    def _pack(self, key, entity_dict):
        temp_dict = {
            "entity" : key,
            "value" : entity_dict[key][0]["value"],
            "confidence" : entity_dict[key][0]["confidence"]
        }
        return temp_dict

    # 處理 wit.ai 自然語意
    def wit_understand(self, message_text):
        resp = self.client.message(message_text) 
        entity_dict = resp["entities"]
        threshold = 0.5
        entity_list = []
        

        if "intent" in entity_dict.keys():
            entity_list.append(self._pack("intent", entity_dict))

            if "moviegenre" in entity_dict.keys():
                entity_list.append(self._pack("moviegenre", entity_dict))
            
        elif "thanks" in entity_dict.keys():
            entity_list.append(self._pack("thanks", entity_dict))

        elif "greetings" in entity_dict.keys():
        
    
            entity_list.append(self._pack("greetings", entity_dict))
        else:
            entity_list = []
        
        return entity_list

    def wit_response(self, entity_list):
        if entity_list == []:
            message_text = "不好意思，我還在學習當中...><"

        else:
            for i in entity_list:

                if "intent" in i["entity"]:
                    message_text = "請問您想尋找什麼類型的電影呢?"  
                elif "moviegenre" in i["entity"]:
                    message_text = "馬上為您尋找"
                elif i["entity"] == "thanks":
                    message_text = "不客氣!"
                elif i["entity"] == "greetings":
                    message_text = "您好，很高興為您服務。"
                
                else:
                    message_text = "不好意思，我仍在學習當中。"
            

        return message_text
        
# witai = WitAi()