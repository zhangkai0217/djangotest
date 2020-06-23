# -*- coding: utf-8 -*-
import time
import uuid
import hashlib
import base64
import requests  # 需要先使用pip install requests命令安装依赖

# 必填,请参考"开发准备"获取如下数据,替换为实际值
url = 'https://rtcsms.cn-north-1.myhuaweicloud.com:10743/sms/batchSendSms/v1'  # APP接入地址+接口访问URI
APP_KEY = "n3U88tOXqhNe75P3SFs483vT57dP"  # APP_Key
APP_SECRET = "Tf2ocI9G3GH604fJddPK7Dtfx07C"  # APP_Secret
sender = "8820061907140"  # Chanel
TEMPLATE_ID = "fd170b26757b475baedefcec7c334ff1"  # mold ID

signature = ""  #

receiver = "+8615951917300,+8619946826669"  # Receive number

statusCallBack = ""

'''
Optional, please use an empty variable template TEMPLATE_PARAM = '';
Single variable template example: When the content of the template is "Your verification code is $ {1}", TEMPLATE_PARAM can be filled in as "[" 369751 "] '
Example of a dual variable template: When the content of the template is "You have $ {1} express delivery, please go to $ {2} to receive", TEMPLATE_PARAM can be filled in as "[" 3 "," People's Park Main Gate "] '
Each variable in the template must be assigned a value, and the value cannot be empty
See more template and variable specifications: Product Introduction> Template and Variable Specifications
'''
TEMPLATE_PARAM = '["888888"]'  # For template variables, take the single-variable verification code SMS as an example. Please generate a 6-digit verification code and define it as a string type to eliminate the problem of the first 0 being lost (for example: 002569 becomes 2569)

'''
构造X-WSSE参数值
@param appKey: string
@param appSecret: string
@return: string
'''


def buildWSSEHeader(appKey, appSecret):
    now = time.strftime('%Y-%m-%dT%H:%M:%SZ')  # Created
    nonce = str(uuid.uuid4()).replace('-', '')  # Nonce
    digest = hashlib.sha256((nonce + now + appSecret).encode()).hexdigest()

    digestBase64 = base64.b64encode(digest.encode()).decode()  # PasswordDigest
    return 'UsernameToken Username="{}",PasswordDigest="{}",Nonce="{}",Created="{}"'.format(appKey, digestBase64, nonce,
                                                                                            now);


def main():
    # 请求Headers
    header = {'Authorization': 'WSSE realm="SDP",profile="UsernameToken",type="Appkey"',
              'X-WSSE': buildWSSEHeader(APP_KEY, APP_SECRET)}
    # 请求Body
    formData = {'from': sender,
                'to': receiver,
                'templateId': TEMPLATE_ID,
                'templateParas': TEMPLATE_PARAM,
                'statusCallback': statusCallBack,
                #                'signature': signature #使用国内短信通用模板时,必须填写签名名称
                }
    print(header)

    # 为防止因HTTPS证书认证失败造成API调用失败,需要先忽略证书信任问题
    r = requests.post(url, data=formData, headers=header, verify=False)
    print(r.text)  # 打印响应信息


if __name__ == '__main__':
    main()
