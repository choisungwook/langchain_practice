# 개요
langchain 학습

# AI모델 다운로드
* https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF

# 실행 방법
```bash
# 파이썬 가상환경 설치
pip install -r requirements.txt

# llama cpp 설치
# CMAKE_ARGS="-DLLAMA_METAL=on" FORCE_CMAKE=1 pip install llama-cpp-python

cd examples/
python {예제파일}.py
```

# 예제 목록
* [쿠버네티스 yaml generator](./examples/example-2-kubernetes.py)

# 참고자료
* https://python.langchain.com/docs/get_started/quickstart#composing-with-lcel
* https://python.langchain.com/docs/modules/model_io/prompts/prompt_templates/msg_prompt_templates
* https://python.langchain.com/docs/modules/model_io/prompts/prompt_templates/
* https://breezymind.com/llamacpp-embedding-news/
* https://breezymind.com/llamacpp-embedding/
