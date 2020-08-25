#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkimageseg.request.v20191230.ParseFaceRequest import ParseFaceRequest

client = AcsClient('<accessKeyId>', '<accessSecret>', 'cn-shanghai')

request = ParseFaceRequest()
request.set_accept_format('json')

request.set_ImageURL("http://explorer-image.oss-cn-shanghai.aliyuncs.com/ocbBJ1yO2mQ_-15vH7ipHZfK/%E5%9B%BE%E7%89%871.png?OSSAccessKeyId=LTAI4Fk9FstqSEYnqKJ5Dpeo&Expires=1598323942&Signature=3YajwnG490uRz8KwMCWJXdxvxvc%3D")

response = client.do_action_with_exception(request)

print(str(response, encoding='utf-8'))