# Dify Plugins Repository

This repository stores **Plugins** for the **[Dify](https://github.com/langgenius/dify)** application.

## Requirements

- **Dify Version**: `1.0.0` or later
- **Environment Variable Setting (Self-Host)**: You need to set `FORCE_VERIFYING_SIGNATURE=false` in environment variables

## Usage / Installation

[Official Documentation](https://docs.dify.ai/plugins/quick-start/install-plugins#github)

1. Install from GitHub in Dify plugins page.
2. Enter GitHub repo URL `https://github.com/blue-pen5805/{PLUGIN_REPOSITORY_NAME}`
3. Select the plugin you want to install.

## List of Plugins

### Model Providers

- **[Cerebras](https://github.com/blue-pen5805/dify-plugin-cerebras)**
  - `https://github.com/blue-pen5805/dify-plugin-cerebras`
  - Models provided by [Cerebras](https://cloud.cerebras.ai/)

#### Forked from Official Plugin

- **[Gemini](https://github.com/blue-pen5805/dify-plugin-gemini)**
  - `https://github.com/blue-pen5805/dify-plugin-gemini`
  - Models provided by [Google](https://aistudio.google.com/)
  - Add `base_url` parameter.
  - Add `Enable file upload` options. (Disable to use `Files API`)
  - Modify model parameters.
    - Temperature range: `0.0` - `2.0`
    - Add `response_format` parameter.
    - Add `safety_settings` parameter.
    - Add `thinking_budget` parameter.
  - Remove deprecated models.
- **[Groq](https://github.com/blue-pen5805/dify-plugin-groq)**
  - `https://github.com/blue-pen5805/dify-plugin-groq`
  - Models provided by [Groq](https://console.groq.com/)
  - Add `base_url` parameter.
- **[Mistral AI](https://github.com/blue-pen5805/dify-plugin-mistralai)**
  - `https://github.com/blue-pen5805/dify-plugin-mistralai`
  - Models provided by [MistralAI](https://mistral.ai)
  - Add `base_url` parameter.
- **[xAI](https://github.com/blue-pen5805/dify-plugin-xai)**
  - `https://github.com/blue-pen5805/dify-plugin-xai`
  - Models provided by [xAI](https://console.x.ai/)
  - Modify model parameters.
    - Change value ranges. (`temperature`, `presence_penalty`, `frequency_penalty`).
    - Add `response_format` parameter.
    - Add `reasoning_effort` parameter.

### Tools

- **[vertex-ai-image-generation](https://github.com/blue-pen5805/dify-plugin-vertex-ai-image-generation)**
  - `https://github.com/blue-pen5805/dify-plugin-vertex-ai-image-generation`
  - [Vertex AI](https://cloud.google.com/vertex-ai/docs/generative-ai) image generation node plugin.
- **[json-tools](https://github.com/blue-pen5805/dify-plugin-json-tools)**
  - `https://github.com/blue-pen5805/dify-plugin-json-tools`
  - JSON tools plugin. (e.g. JSON string to Object, JSON string to Yaml, etc.)
- **[image-shrink](https://github.com/blue-pen5805/dify-plugin-image-shrink)**
  - `https://github.com/blue-pen5805/dify-plugin-image-shrink`
  - Image file shrink automatically.
- **[moderation-chakoshi](https://github.com/blue-pen5805/dify-plugin-moderation-chakoshi)**
  - `https://github.com/blue-pen5805/dify-plugin-moderation-chakoshi`
  - Unofficial [chakoshi](https://chakoshi.ntt.com) plugin.
- **[moderation-openai](https://github.com/blue-pen5805/dify-plugin-moderation-openai)**
  - `https://github.com/blue-pen5805/dify-plugin-moderation-openai`
  - [OpenAI](https://platform.openai.com/) moderation node plugin.
- **[moderation-mistralai](https://github.com/blue-pen5805/dify-plugin-moderation-mistralai)**
  - `https://github.com/blue-pen5805/dify-plugin-moderation-mistralai`
  - [MistralAI](https://mistral.ai) moderation node plugin.
- **[moderation-perspective-api](https://github.com/blue-pen5805/dify-plugin-moderation-perspective-api)**
  - `https://github.com/blue-pen5805/dify-plugin-moderation-perspective-api`
  - [Perspective API](https://platform.openai.com/) analyze node plugin.

## Upcoming / Planned Plugins

...

## Other Resources

- Plugin template repository
  - https://github.com/blue-pen5805/dify-plugin-template
