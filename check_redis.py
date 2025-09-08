from langchain_community.chat_message_histories import RedisChatMessageHistory

history = RedisChatMessageHistory(
    # "ssac0724",
    # url="redis://localhost:6379"
    session_id="LLM0908",
    url="redis://:manager@35.226.244.31:6379"
    )

print(history.messages)