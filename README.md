# Dify Plugins Repository

This repository is storing **Plugins** for the **[Dify](https://github.com/langgenius/dify)** application.

## Requirements

- **Dify Version**: `1.0.0` or later
- **Environment Variable Setting**:You need to set the `FORCE_VERIFYING_SIGNATURE=false` in environment variables

## Usage

[Official Documentation](https://docs.dify.ai/plugins/quick-start/install-and-use-plugins#install-plugins)

## List of Plugins

- **Cerebras**
  - Models provided by [Cerebras](https://cloud.cerebras.ai/)
- **Gemini-oai-compatible**
  - [Gemini OpenAI compatibility Endpoint](https://ai.google.dev/gemini-api/docs/openai) (for [llm-proxy-on-cloudflare-workers](https://github.com/blue-pen5805/llm-proxy-on-cloudflare-workers))

## Development

### Packaging

[Official Documentation](https://docs.dify.ai/plugins/publish-plugins/package-plugin-file-and-publish)

```bash
dify plugin package ./your_plugin_project
```
