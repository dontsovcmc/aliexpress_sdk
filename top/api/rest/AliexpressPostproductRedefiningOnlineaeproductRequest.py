'''
Created by auto_sdk on 2020.06.01
'''
from top.api.base import RestApi
class AliexpressPostproductRedefiningOnlineaeproductRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.product_ids = None

	def getapiname(self):
		return 'aliexpress.postproduct.redefining.onlineaeproduct'
