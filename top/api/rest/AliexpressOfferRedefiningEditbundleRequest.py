'''
Created by auto_sdk on 2018.07.25
'''
from top.api.base import RestApi
class AliexpressOfferRedefiningEditbundleRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.aeop_offer_bundle = None

	def getapiname(self):
		return 'aliexpress.offer.redefining.editbundle'
