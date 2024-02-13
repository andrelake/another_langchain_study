from langchain_openai.chat_models import ChatOpenAI


def build_llm(key: str) -> None:
    llm = ChatOpenAI(openai_api_key=key)
    resp = llm.invoke('Give me five benefits of Pilates practice')
    print(resp.content)
