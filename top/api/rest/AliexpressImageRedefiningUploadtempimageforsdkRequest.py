'''
Created by auto_sdk on 2018.07.25
'''
from top.api.base import RestApi
class AliexpressImageRedefiningUploadtempimageforsdkRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.file_data = None
		self.src_file_name = None

	def getapiname(self):
		return 'aliexpress.image.redefining.uploadtempimageforsdk'

	def getMultipartParas(self):
		return ['file_data']
