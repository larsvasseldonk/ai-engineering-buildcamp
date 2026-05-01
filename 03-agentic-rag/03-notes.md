# Agentic RAG

The traditional RAG flow is fixed. With Agents, we add flexibility. We let the LLM be in control of the search process and give it tools to execute.

## Agent Architecture

4 key components of AI agent architecture in its simplest form:
- Brain - The LLM. It reasons, plans, and decides what to do next.
- Instructions - The system prompt. It defines the agent's role, boundaries, and behavior.
- Tools - Functions the agent can call to interact with the world: reading files, writing code, running commands, searching data.
- Memory - The conversation history and tool results that provide context across steps.

## Agentic loop

Has the following steps:
- The user gives a task
- The agent reasons based on instructions and memory
- It decides to respond or call a tool
- Tool results are added to memory
- The loop continues until the task is complete

## Tool-call loop

LLM in control of the search process:
- Sends the entire message history to the LLM
- Checks each response message
- If it's a function call, executes it and appends the result
- If it's a message (final answer), prints it
- Breaks when no more function calls are made

## Structured output for agents

There are three approaches to tackle this:
1. Using `output_type` in the Loop: Simple, but structures every iteration and can interfere with tool calling
  - The idea: modify the loop to use responses.parse when an output_type is provided.
2. Two-Step Pattern with Wrapper: Flexible, shows reasoning, but requires two API calls with duplication
  - Instead of structuring every iteration, let the agent reason normally, then parse the final result.
3. Fake Tool Call: Single call, maintains reasoning ability, but more complex
  - Instead of parsing after the loop, create a fake "tool" that the LLM calls when ready to provide structured output.

## How Agentic Loop works

The tool call loop (inner loop) works like this:
- LLM receives current message history
- LLM decides what to do:
  - Call a tool → execute tool, add result to history, repeat
  - Provide final answer → exit loop

The key insight is that the LLM chooses its own actions. If it needs more information, it calls a search tool. If it finds what it needs, it synthesizes an answer. If it's unsure, it might search again.

## RAG vs. Agentic RAG

Traditional RAG:
- User query → embed → search → LLM generates answer
- One search, one answer
- LLM has no control over the search process

Agentic RAG:
- User query → LLM decides what to search
- LLM analyzes results and decides whether to search again
- LLM continues until satisfied, then generates answer
- Multiple iterations with the LLM in control

The agentic approach gives the LLM autonomy. It can refine searches, explore different angles, and decide when it has enough information.