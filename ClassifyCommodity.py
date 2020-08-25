#coding=utf-8
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkgoodstech.request.v20191230.ClassifyCommodityRequest import ClassifyCommodityRequest

client = AcsClient('<accessKeyId>', '<accessSecret>', 'cn-shanghai')

request = ClassifyCommodityRequest()

request.set_accept_format('json')

request.set_ImageURL("http://explorer-image.oss-cn-shanghai.aliyuncs.com/z15Aued3IVo6fMn_yDJEeO8Y/%E5%9B%BE%E7%89%875.png?OSSAccessKeyId=LTAI4Fk9FstqSEYnqKJ5Dpeo&Expires=1598333231&Signature=yS6ql7DCXH9wZGKExGL93wJo6Yw%3D")

response = client.do_action_with_exception(request)

print(str(response, encoding='utf-8'))