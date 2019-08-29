#coding=utf-8
#author：zhujingyuan
import unittest
# 加载测试用例
import testDaping
import testROM
import HTMLTestRunner

#将测试用例添加到测试集合

test_dir="./"
discover=unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")


#定义个报告存放路径，支持相对路径
filename='E:\\python\\report\\result.html'
fp=file(filename,'wb')

if __name__=="__main__":
    #定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description=u'用例执行情况')
    runner.run(discover)
