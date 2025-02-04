# langchain

## 1. Llama 3.2 Korean 모델 사용

```shell
# Ollama 설치
$ brew install ollama

# Ollama 실행
$ ollama serve

# Llama Korean 모델 다운로드
$ task pull-llama-korean

# Open WebUI 서버 실행 후 localhost:3000 접속
$ task open-webui

# venv 를 사용해 애플리케이션 실행 
$ task venv
$ source venv/bin/activate
$ task install
$ task run
```
