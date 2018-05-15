# coding=utf-8
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

# driver.get("http://nebula-ai.com")
# time.sleep(1)
# if "https://nebula-ai.com/" == driver.current_url:
#     print ('The web site: http://nebula-ai.com Assertion test pass.')
# else:
#     print ('The web site: http://nebula-ai.com Assertion test fail.')
# # driver.close()
# # driver.quit()
#
# driver.get("http://www.nebula-ai.com")
# time.sleep(1)
# if "https://www.nebula-ai.com/" == driver.current_url:
#     print ('For the web site: http://www.nebula-ai.com Assertion test pass.')
# else:
#     print ('For the web site: http://www.nebula-ai.com Assertion test fail.')
# # driver.close()
# # driver.quit()
#
# driver.get("https://nebula-ai.com")
# time.sleep(1)
# if "https://nebula-ai.com" == driver.current_url:
#     print ('For the web site: https://nebula-ai.com Assertion test pass.')
# else:
#     print ('For the web site: https://nebula-ai.com Assertion test fail.')
# # driver.close()
# # driver.quit()

driver.get("https://www.nebula-ai.com")
time.sleep(1)
print(driver.current_url)
if "https://www.nebula-ai.com" == driver.current_url:
    print('For the web site: https://www.nebula-ai.com Assertion test pass.')
else:
    print('For the web site: https://www.nebula-ai.com Assertion test fail.')
driver.close()
driver.quit()



