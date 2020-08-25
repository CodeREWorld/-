#coding=utf-8
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkfacebody.request.v20191230.SearchFaceRequest import SearchFaceRequest

client = AcsClient('<accessKeyId>', '<accessSecret>', 'cn-shanghai')

request = SearchFaceRequest()
request.set_accept_format('json')

request.set_ImageUrl("http://explorer-image.oss-cn-shanghai.aliyuncs.com/LxO6lCgTTmdxVPX1ExcIo3LZ/1598323282(1).png?OSSAccessKeyId=LTAI4Fk9FstqSEYnqKJ5Dpeo&Expires=1598327916&Signature=Y0VGLZP8f28PEUKpzObLMu9QZt8%3D")
request.set_DbName("default")
request.set_Limit(1)

response = client.do_action_with_exception(request)

print(str(response, encoding='utf-8'))