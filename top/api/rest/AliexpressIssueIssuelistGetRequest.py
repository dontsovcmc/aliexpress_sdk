'''
Created by auto_sdk on 2019.10.30
'''
from top.api.base import RestApi
class AliexpressIssueIssuelistGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.query_dto = None

	def getapiname(self):
		return 'aliexpress.issue.issuelist.get'
