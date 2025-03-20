from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


def test_chatbot_ui():
    """测试 Chatbot UI 是否可以正常显示"""
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8501")  # Streamlit 运行地址
    time.sleep(3)  # 等待页面加载
    page_text = driver.page_source.lower()
    assert "jcu orientation chatbot" in page_text
    driver.quit()

def test_input_box():
    """测试输入框是否可用"""
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8501")

    wait = WebDriverWait(driver, 10)

    # 先尝试查找 `textarea`
    try:
        input_box = wait.until(EC.presence_of_element_located((By.TAG_NAME, "textarea")))
    except:
        # 如果 `textarea` 没找到，尝试 `input`
        input_box = wait.until(EC.presence_of_element_located((By.TAG_NAME, "input")))

    assert input_box is not None
    driver.quit()

def test_user_query():
    """测试用户输入和 Chatbot 响应"""
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8501")

    # 找到输入框并输入查询内容
    input_box = driver.find_element(By.TAG_NAME, "textarea")
    input_box.send_keys("What is the schedule for orientation day?")
    input_box.send_keys(Keys.RETURN)

    # 等待响应
    time.sleep(3)

    # 检查响应文本是否正确
    response_text = driver.find_element(By.ID, "chat-response").text
    assert "The orientation schedule is available" in response_text
    driver.quit()
