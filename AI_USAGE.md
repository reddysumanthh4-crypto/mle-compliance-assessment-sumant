Models and tools used
Model / tool	Purpose (e.g. code gen, prompts, analysis)
ChatGPT (GPT-5 / GPT-4 style assistant)	Guidance on system design, code structuring, and documentation for the compliance checker and situation classifier
VS Code + Git	Code development, refactoring, and running the assessment scripts
Workflows / skills

Used ChatGPT to brainstorm the architecture for the compliance checking pipeline and situation classification.

Used AI assistance to refactor the provided run_assessment.py into modular components (compliance_checker.py and situation_classifier.py).

Reviewed and adjusted the generated suggestions manually to ensure the implementation works with the provided dataset and repository structure.

All final code and testing were performed locally using Python and VS Code.

Token usage and cost (approximate)
Model	Input tokens (approx)	Output tokens (approx)	Est. cost ($)
ChatGPT	~2000	~1200	~$0.01
Total			~$0.01

(Estimates are approximate and based on interactive usage during development.)

Scaling to production — commentary

For production deployment handling thousands of conversations per day, I would design a hybrid system that combines rule-based checks with ML/LLM components.

First, a lightweight rule-based engine (like the one implemented in this assessment) would perform fast keyword or regex checks to detect obvious compliance violations. This ensures low latency and minimal cost for the majority of conversations.

For more ambiguous cases, an LLM-based classifier or embedding similarity search could be used as a second layer. This allows semantic understanding beyond simple keyword matching.

To control cost and improve performance:

Implement caching for repeated or similar conversations.

Use smaller models for simple classification tasks, reserving larger models only for complex cases.

Process conversations in batches asynchronously to improve throughput.

Add guardrails and fallbacks, where rule-based detection runs first and LLM calls are triggered only when needed.

This hybrid approach balances accuracy, cost efficiency, and scalability for large-scale customer communication compliance systems.