'''
Created by auto_sdk on 2019.07.01
'''
from top.api.base import RestApi
class AliexpressTradeSellerOrderAcceptcancelRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.param_order_cancel_request = None

	def getapiname(self):
		return 'aliexpress.trade.seller.order.acceptcancel'
