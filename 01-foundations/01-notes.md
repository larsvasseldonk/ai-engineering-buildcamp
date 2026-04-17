# Week 1 - Foundations - LLMs, RAG and Search

Apr 13 - Apr 19

## Course Overview & Logistics

In general:
- 9-week program designed to take us from LLM basics to production-ready AI applications.
- Course structure:
  - Week 1: Foundation - LLMs, RAG and Search
  - Week 2: Advanced RAG and Buffer Week
  - Week 3: AI Agents
  - Week 4: Testing and Multi-Agent Systems
  - Week 5: Monitoring and Observability
  - Week 6: Evaluation and Improvement
  - Week 7: Project Work and Bonus
  - Week 8: Project Work and Cases
  - Week 9: Demo
- Technologies used throughout the course:
  - LLM APIs: OpenAI, Anthropic, Groq, Gemini, Z.ai, Amazon Bedrock
  - Vector databases: Qdrant, Elasticsearch
  - Agent frameworks: PydanticAI, OpenAI Agents SDK, ToyAIKit, Langchain
  - Evaluation tools: synthetic data, LLM judges
  - Monitoring: Logfire, OpenTelemetry, Jaeger, Grafana
  - Deployment: Streamlit, Render, AWS

Usefull links:
- [Course Management Platform: AI Buildcamp Cohort 3](https://courses.datatalks.club/ai-buildcamp-3/)
- [Office Hour Summaries](https://docs.google.com/document/d/1wriy0wg8S0DcWbJBs_c2Wm8_uFNnc_P4aWFiD5k95ck/edit?pli=1&tab=t.0#heading=h.yldzkaqakq8u)

Learning goals week 1:
- Course introduction and learning in public
- Environment setup (Codespaces or local)
- OpenAI Responses API basics
- Structured output with Pydantic
- RAG pattern: retrieval, augmentation, generation
- Getting documentation data from GitHub
- Indexing with minsearch
- Document chunking strategies
- Complete documentation assistant
- Streaming structured output

## Foundation: LLMs, RAG and Search

RAG lets people ask LLMs questions about their own information, information the LLM doesn't otherwise have access to. This was a breakthrough, and many companies started implementing it.

RAG consists of three steps:
- Search - We need to get the data, index the data, and prepare the data
- Build the prompt - Construct the prompt we'll send to the LLM
- Generate - Send the request to the LLM and get the answer

### Documentation Agent

A documentation agent is an AI system that can answer questions about a specific knowledge base. 

Reasons for a documentation agent:
- Knowledge cutoff - LLMs typically know things up to a certain point (like the end of 2024).
- Less popular libraries - Even for well-known libraries like Evidently, the LLM might not have seen enough examples in the training data. For libraries you or I develop, there's even less chance the LLM knows them well.
- Internal knowledge - Sometimes you have internal knowledge databases at your company like Jira, Confluence, or other tools where you've accumulated knowledge about your internals. The LLM had no way of accessing this data during training.

### RAG

RAG consists of three steps:
1. RETRIEVAL - Find relevant documents using search
2. AUGMENTATION - Include the documents in the prompt
3. GENERATION - LLM generates an answer using the retrieved context

Simple example:
```python
def rag(query):
    search_results = search(query)
    prompt = build_prompt(query, search_results)
    answer = llm(prompt)
    return answer

```

Benefits of RAG
- Accurate answers - based on our actual documentation
- Reduced hallucinations - LLM uses provided context
- Source attribution - we can cite where information came from
- Updatable - update our docs, update the answers
- Private data - use internal knowledge the LLM hasn't seen