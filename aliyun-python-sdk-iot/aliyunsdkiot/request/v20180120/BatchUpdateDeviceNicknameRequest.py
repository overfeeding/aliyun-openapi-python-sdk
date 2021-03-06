# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class BatchUpdateDeviceNicknameRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2018-01-20', 'BatchUpdateDeviceNickname','iot')

	def get_DeviceNicknameInfos(self):
		return self.get_query_params().get('DeviceNicknameInfos')

	def set_DeviceNicknameInfos(self,DeviceNicknameInfos):
		for i in range(len(DeviceNicknameInfos)):	
			if DeviceNicknameInfos[i].get('IotId') is not None:
				self.add_query_param('DeviceNicknameInfo.' + str(i + 1) + '.IotId' , DeviceNicknameInfos[i].get('IotId'))
			if DeviceNicknameInfos[i].get('Nickname') is not None:
				self.add_query_param('DeviceNicknameInfo.' + str(i + 1) + '.Nickname' , DeviceNicknameInfos[i].get('Nickname'))
			if DeviceNicknameInfos[i].get('DeviceName') is not None:
				self.add_query_param('DeviceNicknameInfo.' + str(i + 1) + '.DeviceName' , DeviceNicknameInfos[i].get('DeviceName'))
			if DeviceNicknameInfos[i].get('ProductKey') is not None:
				self.add_query_param('DeviceNicknameInfo.' + str(i + 1) + '.ProductKey' , DeviceNicknameInfos[i].get('ProductKey'))


	def get_IotInstanceId(self):
		return self.get_query_params().get('IotInstanceId')

	def set_IotInstanceId(self,IotInstanceId):
		self.add_query_param('IotInstanceId',IotInstanceId)