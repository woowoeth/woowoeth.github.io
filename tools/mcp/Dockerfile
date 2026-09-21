# Glama 的收录检查要一个能启动并响应 introspection 的镜像。
# 这里刻意不装任何东西 —— 这个 server 只用 Python 标准库。
FROM python:3.12-slim
WORKDIR /app
COPY ourword_mcp.py /app/
# 数据从线上取（jsDelivr，失败回落 ourword.ai），镜像里不带索引：
# 带了就会过期，而过期的索引比没有索引更坏。
ENTRYPOINT ["python", "/app/ourword_mcp.py"]
