# Automatic QA Testing

Automatic QA UI testing with LLM and E2B sandboxing.

# Design Note

- Navigate to a page
- Get the content of a page
- Enter the test case
- Generate test code with LLM
- Execute the code inside the E2B Code Interpreter
- Use Playwright as a service browser
- Run the test
- Extract the screenshots

# Tools

- E2B
- Fireworks.ai
- Playwright



# Setup

install e2b CLI
```bash

npm install -g @e2b/cli@latest

e2b template build -c "/root/.jupyter/start-up.sh" --name='e2b-hack'

```
