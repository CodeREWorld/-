#coding=utf-8
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkfacebody.request.v20191230.FaceBeautyRequest import FaceBeautyRequest

client = AcsClient('<accessKeyId>', '<accessSecret>', 'cn-shanghai')

request = FaceBeautyRequest()

request.set_accept_format('json')

request.set_Sharp("1")
request.set_Smooth(1)
request.set_White("1")
request.set_ImageURL("http://explorer-image.oss-cn-shanghai.aliyuncs.com/LxO6lCgTTmdxVPX1ExcIo3LZ/%E5%9B%BE%E7%89%872.png?OSSAccessKeyId=LTAI4Fk9FstqSEYnqKJ5Dpeo&Expires=1598329244&Signature=CibX%2BrwMrWeHGz63WHaSuhzlQRk%3D")

response = client.do_action_with_exception(request)

print(str(response, encoding='utf-8')