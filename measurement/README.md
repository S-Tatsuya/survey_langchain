# LangChainを使った計測方法の検討

## やること

- [x] [LLMs](https://python.langchain.com/docs/modules/model_io/models/llms/)を使ったコードの実装
    - 未指定の場合は `text-davinci-003` が使われる
- [x] [ChatModels](https://python.langchain.com/docs/modules/model_io/models/chat/)を使ったコードの実装
    - 未指定の場合は `gpt-3.5-turbo` が使用される
- [x] [Note: ChatGPTの応答時間測定](https://note.com/bbz662bbz/n/n9dfc87691818) 応答時間の計測方法
- [ ] [get_openai_callback](https://python.langchain.com/docs/modules/callbacks/token_counting) トークン数の測定
- [ ] [Sequential Chain](https://python.langchain.com/docs/modules/chains/foundational/sequential_chains) の使い方を調べる
- [x] `GPT3.5` でも `llms` が使えるのかを調査する
    - `model_name="gpt-3.5-turbo"` の指定では以下の警告が出力される

        ```bash
        ❯ poetry run python src/main.py
        /home/tsakurai/work/survey/survey_langchain/measurement/.venv/lib/python3.10/site-packages/langchain/llms/openai.py:216: UserWarning: You are trying to use a chat model. This way of initializing it is no longer supported. Instead, please use: `from langchain.chat_models import ChatOpenAI`
        warnings.warn(
        /home/tsakurai/work/survey/survey_langchain/measurement/.venv/lib/python3.10/site-packages/langchain/llms/openai.py:811: UserWarning: You are trying to use a chat model. This way of initializing it is no longer supported. Instead, please use: `from langchain.chat_models import ChatOpenAI`
        warnings.warn(
        Sure, here's a joke for you:

        Why don't scientists trust atoms? 

        Because they make up everything! 
        ```

- [ ] ModelをAzureに切り替える

## 内田さんの要求

- Slackから引用

    >簡単にいうとこんなことがやりたいです。
    >SystemPrompt（初回のみ）：あなたは要求仕様を添削する人です。ユーザーが入力する文章の文法誤りや誤字を指摘し、修正案を提示してください。応答のフォーマットは〇〇で。
    >HumanMessage：要求１を入力
    >AIMessage：LLMが要求１の指摘および修正案を応答
    >HumanMessage：要求２を入力
    >AIMessage：LLMが要求２の指摘および修正案を応答
    >　　　:
    >で、最後にAIMessageが応答したすべての文章を拾い上げて、REST APIの応答フォーマットに沿って返すみたいなことがしたいです。
