import requests
import threading

BASE_URL = "http://127.0.0.1:8000/chatbot/"


def send_request():
    response = requests.get(BASE_URL, params={"query": "What is the schedule for orientation day?"})
    assert response.status_code == 200


def test_high_concurrency():
    """测试高并发请求是否可以正常处理"""
    threads = [threading.Thread(target=send_request) for _ in range(50)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
