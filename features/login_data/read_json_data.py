import json
file_path = 'C:/Users/Kundan_Kumar/PycharmProjects/selenium_envsetup_practise/features/login_data/credentials.json'
with open(file=file_path,mode='r') as json_file:
    data = json.load(json_file) # load is to convert json file into python readable format
    usrname = data[0]['username']
    pswrd = data[0]['password']
