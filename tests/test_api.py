import requests
import json

BASE_URL = "http://127.0.0.1:8000/chatbot/"

def test_chatbot_api():
    """测试 Chatbot API 是否可以正确响应"""
    response = requests.get(BASE_URL, params={"query": "What is the schedule for orientation day?"})
    assert response.status_code == 200
    assert "The orientation schedule is available" in response.json()["response"]

def test_faq_match():
    """测试 FAQ 查询是否可以正确匹配"""
    response = requests.get(BASE_URL, params={"query": "Where can I collect my student ID?"})
    assert response.status_code == 200
    assert "Student ID can be collected" in response.json()["response"]

def test_fuzzy_matching():
    """测试模糊查询"""
    response = requests.get(BASE_URL, params={"query": "student identity card pickup"})
    assert response.status_code == 200
    response_text = response.json()["response"].lower()
    assert "student id" in response_text and "collected" in response_text


def test_empty_input():
    """测试空白输入"""
    response = requests.get(BASE_URL, params={"query": ""})
    assert response.status_code == 200
    response_text = response.json()["response"]
    assert "Hello!" in response_text or "How can I assist you" in response_text


def test_invalid_query():
    """测试无关查询"""
    response = requests.get(BASE_URL, params={"query": "Who is the president of the USA?"})
    assert response.status_code == 200
    assert "I can only answer questions related to JCU SG" in response.json()["response"]
