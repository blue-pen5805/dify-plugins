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

- **[Gemini / with Google Gen AI SDK](https://github.com/blue-pen5805/dify-plugin-gemini-genai-sdk)**
  - `https://github.com/blue-pen5805/dify-plugin-gemini-genai-sdk`
  - forked from [Official Plugin](https://github.com/langgenius/dify-official-plugins/tree/main/models/gemini)
    - Modified to use the [Google Gen AI SDK](https://github.com/googleapis/python-genai) instead of the [Google AI Python SDK for the Gemini API](https://github.com/google-gemini/generative-ai-python).
  - Add `base_url` provider parameter.
  - Support `Safety Settings` parameter.
  - Support `Grounding`.
  - Support `presence_penalty` and `frequency_penalty` parameters.
- **[Gemini / OpenAI Compatible Endpoint](https://github.com/blue-pen5805/dify-plugin-gemini-oai-compatible)**
  - `https://github.com/blue-pen5805/dify-plugin-gemini-oai-compatible`
  - [Gemini OpenAI compatibility Endpoint](https://ai.google.dev/gemini-api/docs/openai) (for [llm-proxy-on-cloudflare-workers](https://github.com/blue-pen5805/llm-proxy-on-cloudflare-workers))
- **[Cerebras](https://github.com/blue-pen5805/dify-plugin-cerebras)**
  - `https://github.com/blue-pen5805/dify-plugin-cerebras`
  - Models provided by [Cerebras](https://cloud.cerebras.ai/)
- **[Groq](https://github.com/blue-pen5805/dify-plugin-groq)**
  - `https://github.com/blue-pen5805/dify-plugin-groq`
  - Models provided by [Groq](https://console.groq.com/)
  - forked from [Official Plugin](https://github.com/langgenius/dify-official-plugins/tree/main/models/groq)
    - Add `base_url` parameter.
- **[Mistral AI](https://github.com/blue-pen5805/dify-plugin-mistralai)**
  - `https://github.com/blue-pen5805/dify-plugin-mistralai`
  - Models provided by [MistralAI](https://mistral.ai)
  - forked from [Official Plugin](https://github.com/langgenius/dify-official-plugins/tree/main/models/mistralai)
    - Add `base_url` parameter.
- **[xAI](https://github.com/blue-pen5805/dify-plugin-xai)**
  - `https://github.com/blue-pen5805/dify-plugin-xai`
  - Models provided by [xAI](https://console.x.ai/)
  - forked from [Official Plugin](https://github.com/langgenius/dify-official-plugins/tree/main/models/mistralai)
    - modify parameters.

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
