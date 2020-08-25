#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkfacebody.request.v20191230.DetectFaceRequest import DetectFaceRequest

client = AcsClient('<accessKeyId>', '<accessSecret>', 'cn-shanghai')

request = DetectFaceRequest()

request.set_accept_format('json')

request.set_ImageURL("http://explorer-image.oss-cn-shanghai.aliyuncs.com/z15Aued3IVo6fMn_yDJEeO8Y/%E5%9B%BE%E7%89%872.png?OSSAccessKeyId=LTAI4Fk9FstqSEYnqKJ5Dpeo&Expires=1598333690&Signature=OXHbvoTqMiw1Vsw8z1S3kQyTMyQ%3D")

response = client.do_action_with_exception(request)

print(str(response, encoding='utf-8'))