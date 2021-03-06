#app控件交互

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestTouchAction:
    # 初始化用例，设置capbility参数，设置隐式等待时间
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        #desired_caps['platformVersion'] = '10'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.view.WelcomeActivityAlias'
        desired_caps["noReset"] = 'true'
        desired_caps["dontStopAppOnReset"] = 'true'
        desired_caps["skipDeviceInitialization"] = 'true'
        # desired_caps["unicodeKeyBoard"] = 'true'
        # desired_caps["resetKeyBoard"] = 'true'
        desired_caps["unicodeKeyboard"] = True
        desired_caps["resetKeyboard"] = True

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.back()
        self.driver.back()

    #     self.driver.quit()

    def test_elements(self):
        '''
        打开雪球应用首页
        定位首页的搜索框
        判断搜索框是否可见，并查看搜索框的name属性
        打印搜索框这个元素的左上角坐标喝它的宽高
        向搜索框输入：alibaba
        判断阿里巴巴是否可见
        如果可见则打印搜索成功点击，如果不可见，打印搜索失败
        :return:
        '''
        elements = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        elements_enable = elements.is_enabled()
        print(elements.text)
        print(elements.location)
        print(elements.size)
        if elements_enable == True:
            elements.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
            element_isable = self.driver.find_element_by_xpath(
                "//*[@resource-id = 'com.xueqiu.android:id/name' and @text = '阿里巴巴']")
            element_display = element_isable.get_attribute('displayed')
            print(element_display)
            if element_display == 'true':
                print("搜索成功")
            else:
                print("搜索失败")

##高级定位技巧
    def test_get_current(self):
        '''
        打开雪球APP
        搜索alibaba
        从搜素结果查找、阿里巴巴的价格
        :return:
        '''
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
        self.driver.find_element_by_xpath(
            "//*[@resource-id = 'com.xueqiu.android:id/name' and @text = '阿里巴巴']")
        get_current = self.driver.find_element_by_xpath(
            '//*[@text="BABA"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]').text
        assert float(get_current) > 200

        # 使用uiautomator定位

    def test_uiautomator(self):
        '''
        点击我的，进入到个人信息页面
        点击登录，进入到登录页面
        输入用户名密码
        点击登录
        :return:
        '''
        self.driver.find_element_by_android_uiautomator('new UiSelector().')
