# Solution Overview

This system performs two main tasks:

1. Compliance rule checking
2. Customer situation classification

## Compliance Checker

Agent messages are scanned against predefined compliance rules using
keyword and regex matching.

Each violation returns:
- rule_id
- category
- severity
- matched keyword

## Situation Classification

Customer conversations are classified into:

- product_loss
- substandard_service
- other

A heuristic keyword-based classifier is used for this task.

## Architecture

Conversation Data
        ↓
Compliance Checker
        ↓
Situation Classifier
        ↓
Results Output

## Future Improvements

In production this system could be improved by:

- semantic rule detection using embeddings
- few-shot LLM classification
- fine-tuning a domain-specific model using LoRA