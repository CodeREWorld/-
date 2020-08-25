#coding=utf-8
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkfacebody.request.v20191230.EnhanceFaceRequest import EnhanceFaceRequest

client = AcsClient('<accessKeyId>', '<accessSecret>', 'cn-shanghai')

request = EnhanceFaceRequest()

request.set_accept_format('json')

request.set_ImageURL("http://viapi-test.oss-cn-shanghai.aliyuncs.com/sanjiye-meizi/%E4%BA%BA%E8%84%B8%E4%BF%AE%E5%A4%8D%E5%A2%9E%E5%BC%BA.jpg")

response = client.do_action_with_exception(request)

print(str(response, encoding='utf-8'))