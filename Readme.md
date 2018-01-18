### 1、Python 版本为2.7
### 2、本文主要提供qcloud apigateway加密方法，调用示例参考 Demo.py 文件
### 3、其他使用注意事项：
- 含有中文和空格的query, body在请求时需要对值进行urlencode处理，编码为utf-8.
- 参数计算签名时，必须使用编码前的值进行签名，不能用urlencode后字符串的进行签名.所以请在签名之后再对query、body的值做urlencode。