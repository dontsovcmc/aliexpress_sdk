'''
Created by auto_sdk on 2019.06.20
'''
from top.api.base import RestApi
class AliexpressPostproductRedefiningEditsimpleproductfiledRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.fied_name = None
		self.fiedvalue = None
		self.product_id = None

	def getapiname(self):
		return 'aliexpress.postproduct.redefining.editsimpleproductfiled'