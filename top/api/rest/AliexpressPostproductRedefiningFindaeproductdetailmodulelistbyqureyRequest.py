'''
Created by auto_sdk on 2018.07.25
'''
from top.api.base import RestApi
class AliexpressPostproductRedefiningFindaeproductdetailmodulelistbyqureyRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.module_status = None
		self.page_index = None
		self.type = None

	def getapiname(self):
		return 'aliexpress.postproduct.redefining.findaeproductdetailmodulelistbyqurey'
