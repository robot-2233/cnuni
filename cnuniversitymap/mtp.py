# from data import universities
# from deep_translator import GoogleTranslator
# import os
# os.environ["http_proxy"] = "http://127.0.0.1:7890"
# os.environ["https_proxy"] = "http://127.0.0.1:7890"
#
#
# print('universities = [')
# translator = GoogleTranslator(source='auto', target='en')
# for i in universities:
#     if i.en_name is None:
#         try:
#             i.en_name = translator.translate(i.cn_name).replace('"',"'").replace('\n','')
#         except:
#             pass
#     print(i,end=',\n')
# print(']')
# #单双引号 note
# # University(2756, '铁门关职业技术学院', None, 4165014660, '新疆生产建设兵团', '铁门关市', '专科', 'None'),
from data import universities
print()