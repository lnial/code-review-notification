code-review-notification
========================

code-review-notification

githubでプルリクにコメントが付いたらhipchatにメッセージを飛ばすwebHookサーバ
 
# 必要なpackage  
**[python-simple-hipchat](https://github.com/kurttheviking/python-simple-hipchat)**  
**[web.py](http://webpy.org/)**

# 必要事項
>  hipchat data  
> HIP_CHAT_TOKEN = ''  
> ROOM_ID  =   

# 実行
$ python hook.py [port]

githubのプロジェクトにwebhookをかませる



