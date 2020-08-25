#coding=utf-8
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkimagerecog.request.v20190930.RecognizeLogoRequest import RecognizeLogoRequest

client = AcsClient('<accessKeyId>', '<accessSecret>', 'cn-shanghai')

request = RecognizeLogoRequest()
request.set_accept_format('json')

request.set_Taskss([
  {
    "ImageURL": "http://explorer-image.oss-cn-shanghai.aliyuncs.com/LxO6lCgTTmdxVPX1ExcIo3LZ/el_sku_YH0L19_558x768_0.jpg?OSSAccessKeyId=LTAI4Fk9FstqSEYnqKJ5Dpeo&Expires=1598332493&Signature=FAmwE5gbWG2kOFcI4Gp4qikt428%3D"
  }
])

response = client.do_action_with_exception(request)

print(str(response, encoding='utf-8'))