import requests
import requests_mock

BASE_URL = "http://127.0.0.1:8000/chatbot/"


def test_mock_chatbot_response():
    """使用 requests-mock 模拟 Chatbot API 响应"""
    with requests_mock.Mocker() as mock:
        mock.get(BASE_URL, json={"response": "This is a mocked chatbot reply!"})

        response = requests.get(BASE_URL, params={"query": "Mock test"})
        assert response.status_code == 200
        json_data = response.json()
        assert json_data["response"] == "This is a mocked chatbot reply!"


def test_chatbot_api():
    """测试 Chatbot API 是否可以正确响应"""
    response = requests.get(BASE_URL, params={"query": "What is the schedule for orientation day?"})
    assert response.status_code == 200
    json_data = response.json()
    assert "response" in json_data
    assert "The orientation schedule is available" in json_data["response"]


def test_faq_match():
    """测试 FAQ 查询是否可以正确匹配"""
    response = requests.get(BASE_URL, params={"query": "Where can I collect my student ID?"})
    assert response.status_code == 200
    json_data = response.json()
    assert "response" in json_data
    assert "Student ID can be collected" in json_data["response"]


def test_fuzzy_matching():
    """测试模糊查询"""
    response = requests.get(BASE_URL, params={"query": "student identity card pickup"})
    assert response.status_code == 200
    json_data = response.json()
    assert "response" in json_data
    response_text = json_data["response"].lower()
    assert any(keyword in response_text for keyword in ["student id", "identity card", "collect"])


def test_empty_input():
    """测试空白输入"""
    response = requests.get(BASE_URL, params={"query": ""})
    assert response.status_code == 200
    json_data = response.json()
    assert "response" in json_data
    response_text = json_data["response"].lower()

    # 调整关键词判断，确保涵盖 fallback 响应内容
    expected_keywords = ["hello", "assist", "sorry", "not sure", "cannot", "help"]
    assert any(keyword in response_text for keyword in expected_keywords)


def test_invalid_query():
    """测试无关查询"""
    response = requests.get(BASE_URL, params={"query": "Who is the president of the USA?"})
    assert response.status_code == 200
    json_data = response.json()
    assert "response" in json_data
    assert "i can only answer questions related to jcu sg" in json_data["response"].lower()



