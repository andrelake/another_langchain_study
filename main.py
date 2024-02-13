import os
from dotenv import load_dotenv

from llm_interaction import build_llm

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


def main() -> None:
    build_llm(OPENAI_API_KEY)


if __name__ == "__main__":
    main()
