from dotenv import load_dotenv
load_dotenv()


# from langchain_openai import OpenAI
# #1.모델 객체 생성
# llm = OpenAI()
# #2. LLM 호출 ( 구버전의 llm.predict("안녕!") )
# llm_response = llm.invoke("내가 좋아하는 색상은?")
# #3. 결과 출력
# print(llm_response)


from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI()
response = chat_model.invoke("나는 초록색을 좋아해 너는?")
# ChatModel의 invoke() 결과는 객체(AIMessage)로 반환되므로, 텍스트만 보려면 .content를 사용합니다.
# print(response)
print(response.content)
# print(response.additional_kwargs)