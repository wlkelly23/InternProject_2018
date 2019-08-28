import json


reply = {
    "generate_program":{
            
            "message":{
                "text": "請問您的訓練目標是?\n(或以打字輸入~~)",
                "quick_replies":[
                    {
                        "content_type":"text",
                        "title":"比賽10k",
                        "payload":"比賽10k"
                    },
                    {
                        "content_type":"text",
                        "title":"比賽21k",
                        "payload":"比賽21k"
                    },
                    {
                        "content_type":"text",
                        "title":"減重(待補)",
                        "payload":"減重(待補)"
                    },
                    {
                        "content_type":"text",
                        "title":"突破個人PB(待補)",
                        "payload":"突破個人PB(待補)"
                    }
                ]
            }

    },
    

    
    "query_program":{
            "message":{
                "text": "請問您想查詢的課表為?",
                "quick_replies":[
                    {
                        "content_type":"text",
                        "title":"本週課表",
                        "payload":"本週課表"
                    },
                    {
                        "content_type":"text",
                        "title":"下週課表",
                        "payload":"下週課表"
                    }
                ]
            }
    },

    "10k":{
            "message":{
                "text": "請輸入訓練週數?\n(請點選按鈕來輸入~)",
                "quick_replies":[
                    {
                        "content_type":"text",
                        "title":"4週課程",
                        "payload":"4週課程"
                    },
                    {
                        "content_type":"text",
                        "title":"8週課程",
                        "payload":"8週課程"
                    }
                ]
            }
    },
    "21k":{
            "message":{
                "text": "請輸入訓練週數?\n(請點選按鈕來輸入~)",
                "quick_replies":[
                    {
                        "content_type":"text",
                        "title":"4週課程",
                        "payload":"4週課程"
                    },
                    {
                        "content_type":"text",
                        "title":"8週課程",
                        "payload":"8週課程"
                    }
                ]
            }
    },

    "url_button":{

            "message":{
                "attachment":{
                    "type":"template",
                    "payload":{
                        "template_type":"button",
                        "text":"我是網址按鈕!(字數不限)",
                        "buttons":[
                        {
                            "type":"web_url",
                            "url":"https://www.google.com",
                            "title":"URL Button(上限20字)",
                            "webview_height_ratio": "tall"
                        }
                        ]
                    }
                }
            }
    },

    "postback_button":{

            "message":{
                "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"button",
                    "text":"我是回傳按鈕!(字數不限)",
                    "buttons":[
                    {
                        "type":"postback",
                        "title":"Postback Button(上限20字)",
                        "payload":"postback button"
                    }
                    ]
                }
                }
            }
    },

    "share_button":{

        "message":{
            "attachment":{
            "type":"template",
            "payload":{
                "template_type":"generic",
                "elements":[
                {
                    "title":"我是分享按鈕!(標題上限80字)",
                    "subtitle":"副標上限80字",
                    "image_url":"http://media.tumblr.com/2718b659b0c2a16c062969959f577665/tumblr_inline_mntmm1JGR11qz4rgp.jpg",
                    "buttons": [
                    {
                        "type": "element_share",
                        "share_contents": { 
                        "attachment": {
                            "type": "template",
                            "payload": {
                            "template_type": "generic",
                            "elements": [
                                {
                                "title": "NO PAIN, NO GAIN!(標題上限80字)",
                                "subtitle": "Your only limit is you.(副標上限80字)",
                                "image_url": "https://s-media-cache-ak0.pinimg.com/736x/da/63/fa/da63fa4f18be7dc3cedbbd581856db2f.jpg",
                                "buttons": [
                                    {
                                    "type": "web_url",
                                    "url": "http://www.nike.com", 
                                    "title": "Take a look!"
                                    }
                                ]
                                }
                            ]
                            }
                        }
                        }
                    }
                    ]
                }
                ]
            }
            }
        }
    },

    "call_button":{

            "message":{
                "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"button",
                    "text":"我是通話按鈕!(字數不限)",
                    "buttons":[
                    {
                        "type":"phone_number",
                        "title":"Call Button (上限20字)",
                        "payload":"+886223456789"
                    }
                    ]
                }
                }
            }
    },

    "simple_template":{

            "message":{
                "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"generic",
                    "elements":[
                    {
                        "title":"我是一般型範本!(標題上限80字)",
                        "image_url":"https://cdn1.thr.com/sites/default/files/2011/12/imdb_a.jpg",
                        "subtitle":"支持網址按鈕、回傳按鈕、分享按鈕、通話按鈕等。(副標上限80字)",
                        "default_action": {
                        "type": "web_url",
                        "url": "https://www.imdb.com/",
                      
                        "webview_height_ratio": "tall"

                        },
                        "buttons":[
                        {
                            "type":"web_url",
                            "url":"https://www.imdb.com/",
                            "title":"View Website"
                        }            
                        ]      
                    },
                    {
                        "title":"我是一般型範本!(標題上限80字)",
                        "image_url":"https://cdn1.thr.com/sites/default/files/2011/12/imdb_a.jpg",
                        "subtitle":"兩個按鈕。(副標上限80字)",
                        "default_action": {
                        "type": "web_url",
                        "url": "https://www.imdb.com/",
                     
                        "webview_height_ratio": "tall"

                        },
                        "buttons":[
                        {
                            "type":"web_url",
                            "url":"https://www.imdb.com/",
                            "title":"View Website"
                        },{
                            "type":"postback",
                            "title":"Start Chatting",
                            "payload":"postback button"
                        }              
                        ]      
                    },
                    {
                        "title":"我是一般型範本!(標題上限80字)",
                        "image_url":"https://cdn1.thr.com/sites/default/files/2011/12/imdb_a.jpg",
                        "subtitle":"最多可含三個按鈕。(副標上限80字)",
                        "default_action": {
                        "type": "web_url",
                        "url": "https://www.imdb.com/",
                   
                        "webview_height_ratio": "tall"

                        },
                        "buttons":[
                        {
                            "type":"web_url",
                            "url":"https://www.imdb.com/",
                            "title":"View Website"
                        },{
                            "type":"postback",
                            "title":"Start Chatting",
                            "payload":"postback button"
                        },
                        {
                            "type":"phone_number",
                            "title":"Call Me",
                            "payload":"+886223456789"
                        }                    
                        ]      
                    }
                    ]
                }
                }
            }
    },

    "list_template":{

            "message": {
                "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "list",
                    "top_element_style": "compact",
                    "elements": [
                                
                    {
                        "title": "我是清單範本! 最多含四個清單(標題上限80字，但會受行數限制)",
                        "subtitle": "支持網址按鈕、回傳按鈕、分享按鈕、通話按鈕等。(副標上限80字，但會受行數限制)",
                        "image_url": "https://www.commodorewaves.com/wp-content/uploads/2017/11/Movie-Night.jpg",
                                    "default_action": {
                        "type": "web_url",
                        "url": "https://www.vscinemas.com.tw/",
                        "webview_height_ratio": "tall"
                        }

                    },
                                
                    {
                        "title": "IMDB",
                        "subtitle": "Let's watch movies!",
                                    "image_url":"https://cdn1.thr.com/sites/default/files/2011/12/imdb_a.jpg",
                        "default_action": {
                        "type": "web_url",
                        "url": "https://www.imdb.com/",
                        "webview_height_ratio": "tall"
                        },
                                    "buttons": [
                        {
                            "title": "View",
                            "type": "web_url",
                            "url": "https://www.vscinemas.com.tw/",
                            "webview_height_ratio": "tall"
                        }
                        ]
                    },
                                
                    {
                        "title": "YOUTUBE",
                        "subtitle": "Let's listen to musics!",
                        "image_url": "https://d1oaeulqqi12bi.cloudfront.net/data/Images/03/96/df/57/e9e38e68fcb9137747de909_815x611.jpg?v=1533052800",
                        "default_action": {
                        "type": "web_url",
                        "url": "https://www.youtube.com",
                        "webview_height_ratio": "tall"
                        },
                        "buttons": [
                        {
                            "title": "View",
                            "type": "web_url",
                            "url": "https://www.youtube.com",
                            "webview_height_ratio": "tall"
                    
                        }
                        ]        
                    },
                                
                    ],
                    "buttons": [
                    {
                        "title": "View More",
                        "type": "postback",
                        "payload": "payload"            
                    }
                    ]  
                }
                }
            }
    },

    "list_template_example":{

            "message": {
                "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "list",
                    "top_element_style": "large",
                    "elements": [
                                
                    {
                        "title": "跑前熱身",
                        "subtitle": "跑步前的熱身活動，幫助我們預防損傷，跑出健康與活力。根據從一般到專項的熱身原則，我們從關節功能開始進行...",
                        "image_url": "https://i.ytimg.com/vi/8bz8ip2ptJQ/maxresdefault.jpg"
                    },
                                
                    {
                        "title": "膝關節熱身",
                        "subtitle": "20次， 無器械",
                        "image_url":"https://www.orthosleeve.com/wp-content/uploads/2015/10/Female-Runner-knee-pain-684x1024.jpg",
                        "default_action": {
                        "type": "web_url",
                        "url": "https://www.youtube.com/",
                        "webview_height_ratio": "tall"
                        },
                        "buttons": [
                        {
                            "title": "View",
                            "type": "web_url",
                            "url": "https://www.youtube.com/",
                            "webview_height_ratio": "tall"
                        }
                        ]
                    },
                                
                    {
                        "title": "臀部動態拉伸",
                        "subtitle": "20次, 無器械",
                        "image_url": "https://i3.read01.com/SIG=29rsgr4/304666674b716d746738.jpg",
                        "default_action": {
                        "type": "web_url",
                        "url": "https://www.youtube.com/",
                        "webview_height_ratio": "tall"
                        },
                        "buttons": [
                        {
                            "title": "View",
                            "type": "web_url",
                            "url": "https://www.youtube.com/",
                            "webview_height_ratio": "tall"
                    
                        }
                        ]        
                    },
                    {
                        "title": "向前肩部繞環",
                        "subtitle": "8次, 無器械",
                        "image_url": "https://img.appledaily.com.tw/images/twapple/640pix/20060323/SN06/SN06_009.jpg",
                        "default_action": {
                        "type": "web_url",
                        "url": "https://www.youtube.com",
                        "webview_height_ratio": "tall"
                        },
                        "buttons": [
                        {
                            "title": "View",
                            "type": "web_url",
                            "url": "https://www.youtube.com",
                            "webview_height_ratio": "tall"
                    
                        }
                        ]        
                    }
                                
                    ],
                    "buttons": [
                    {
                        "title": "查看更多",
                        "type": "postback",
                        "payload": "payload"            
                    }
                    ]  
                }
                }
            }
    },

    "button_template":{

            "message":{
                "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"button",
                    "text":"我是按鈕範本! 最多使用三個按鈕，支持網址按鈕、回傳按鈕、通話按鈕等。(字數不限)",
                    "buttons":[
                    {
                        "type":"web_url",
                        "url":"https://www.messenger.com",
                        "title":"View Website"
                    },
                    {
                        "type":"postback",
                        "title":"Start Chatting",
                        "payload":"postback button"
                    },
                    {
                        "type":"phone_number",
                        "title":"Call Us",
                        "payload":"+886223456789"
                    }
                    ]
                }
                }
            }
    },
    "media_template":{

            "message":{
                "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "media",
                    "elements": [
                        {
                            "media_type": "image",
                            "attachment_id": "311350469439666",
                            "buttons":[
                            {
                                "type":"web_url",
                                "url":"https://www.imdb.com/",
                                "title":"我是媒體範本! 最多可含三個按鈕 "
                            },
                            {
                                "type":"web_url",
                                "url":"https://www.imdb.com/",
                                "title":"可傳圖像、GIF和影片"
                            },
                    
                            {
                                "type":"web_url",
                                "url":"https://www.imdb.com/",
                                "title":"支持網址、回傳、分享、通話按鈕等。"
                            }
                            ]
                        }
                    ]
                }
                }    
            }
    }




    

}