# Dify Plugins Repository

This repository is storing **Plugins** for the **[Dify](https://github.com/langgenius/dify)** application.

## Requirements

- **Dify Version**: `1.0.0-beta.1` or later

  - To use the plugins in this repository, you need to have Dify version `1.0.0-beta.1` or newer.

- **Environment Variable Setting**

  - You need to set the `FORCE_VERIFYING_SIGNATURE=false` in environment variables of `plugin_daemon`:

    ```yaml
    ...
    services:
      plugin_daemon:
        ...
        environment:
          ...: ...
          FORCE_VERIFYING_SIGNATURE: false
    ...
    ```

## Usage

[Official Documentation](https://docs.dify.ai/plugins/quick-start/install-and-use-plugins#install-plugins)
