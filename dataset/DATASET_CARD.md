# Indian Government Legal Simplification Dataset

## Overview
This dataset contains parallel segments of Indian government and legal text paired with plain-language simplifications. It focuses primarily on the income-tax domain, making it suitable for evaluating reading comprehension, semantic preservation, and simplification models.

## Schema
| Field | Description |
|---|---|
| `id` | Unique row identifier |
| `document_id` | Identifier of the source document this segment came from |
| `original_text` | Raw legal/bureaucratic source text |
| `simplified_text` | Plain-language rewrite |
| `source_language` | Language code of `original_text` (e.g., `en`) |
| `target_language` | Language code of `simplified_text` (e.g., `en`, `hi`) |
| `document_type` | Type of document (e.g., circular, FAQ, form instruction, notice) |
| `domain` | The domain of the legal text (e.g., income-tax) |
| `complexity` | Rough difficulty tier (1–3) |
| `source_url` | Provenance / URL of the original text |

## Construction Methodology
- **Collection**: Raw texts are sourced from official government portals (e.g., incometaxindia.gov.in).
- **Simplification**: Initial drafts can be generated via LLMs, intended to be manually reviewed and corrected by human annotators.
- **Current Status**: The current implementation contains a small placeholder dataset to validate the machine learning pipeline and evaluation metrics. A full data collection and human review process is required before a production release.

## Split Methodology
- The dataset is split into Train, Validation, and Test subsets based on `document_id` rather than segment-level splitting. 
- **Integrity**: This document-level splitting ensures that all segments from a single document appear in only one split. This prevents data leakage where a model might see a document's style or specific terminology during training and be incorrectly evaluated on segments from the same document in the test set.
- **Stratification**: Where possible, splits are stratified by `document_type` and `complexity` to ensure balanced distributions across all sets.

## Limitations
- **Current Data**: The current repository contains a few mock samples to establish the training pipeline. It does NOT currently contain fully human-reviewed and verified data at scale.
- **Scope**: The dataset is limited initially to income-tax procedures in English. Future expansions are planned for Hindi and other regional languages.
