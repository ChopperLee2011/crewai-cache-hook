import pytest
import logging

def pytest_configure(config):
    """配置全局测试日志"""
    logging.basicConfig(
        level=logging.INFO, 
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

@pytest.fixture(scope='session')
def redis_config():
    """提供测试用的 Redis 配置"""
    return {
        'host': 'localhost',
        'port': 6379,
        'db': 0
    }
