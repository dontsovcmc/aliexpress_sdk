'''
Created by auto_sdk on 2018.12.14
'''
from top.api.base import RestApi
class AliexpressPostproductRedefiningRenewexpireRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.product_id = None

	def getapiname(self):
		return 'aliexpress.postproduct.redefining.renewexpire'
