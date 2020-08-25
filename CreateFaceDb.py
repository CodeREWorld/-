#coding=utf-8
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkfacebody.request.v20191230.CreateFaceDbRequest import CreateFaceDbRequest

client = AcsClient('<accessKeyId>', '<accessSecret>', 'cn-shanghai')

request = CreateFaceDbRequest()

request.set_accept_format('json')

response = client.do_action_with_exception(request)

print(str(response, encoding='utf-8'))