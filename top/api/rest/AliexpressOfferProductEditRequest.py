'''
Created by auto_sdk on 2020.01.20
'''
from top.api.base import RestApi
class AliexpressOfferProductEditRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.aeop_a_e_product = None

	def getapiname(self):
		return 'aliexpress.offer.product.edit'
