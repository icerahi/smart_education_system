# import webview
# import os
# import threading
# from time import sleep
# def server_start():
#     os.system('python manage.py runserver')
    

# def server_close():
#     os.system('pkill -f runserver')


# t1 = threading.Thread(target=server_start)
# t1.start()
# sleep(1)

# if __name__ == '__main__':

#     window = webview.create_window('Simple browser', 'http://localhost:8000',width=1280,height=700)
#     window.closing+=server_close
    
#     webview.start()
import webview
webview.create_window('Hello world', 'http://rahi.pythonanywhere.com/admin')
webview.start()
