# Dify Plugins Repository

This repository stores **Plugins** for the **[Dify](https://github.com/langgenius/dify)** application.

## Requirements

- **Dify Version**: `1.0.0` or later
- **Environment Variable Setting (Self-Host)**: You need to set `FORCE_VERIFYING_SIGNATURE=false` in environment variables

## Usage / Installation

[Official Documentation](https://docs.dify.ai/plugins/quick-start/install-plugins#github)

1. Install from GitHub in Dify plugins page.
2. Enter GitHub repo URL `https://github.com/blue-pen5805/dify-plugins`
3. Select the plugin you want to install.

## List of Plugins

- **Cerebras**
  - Models provided by [Cerebras](https://cloud.cerebras.ai/)
- **Gemini-oai-compatible**
  - [Gemini OpenAI compatibility Endpoint](https://ai.google.dev/gemini-api/docs/openai) (for [llm-proxy-on-cloudflare-workers](https://github.com/blue-pen5805/llm-proxy-on-cloudflare-workers))
- **groq**
  - Models provided by [Groq](https://console.groq.com/)
  - forked from [Official Plugin](https://github.com/langgenius/dify-official-plugins/tree/main/models/groq)
    - Add `base_url` parameter.
- **moderation-chakoshi**
  - Unofficial [chakoshi](https://chakoshi.ntt.com) plugin.

## Development

### Installation

To install and get started with the plugin development, run the following command:

```bash
./dify-plugin
```

### Packaging

To package the plugin, run the following command:

```bash
./package plugin-dir-name
```
