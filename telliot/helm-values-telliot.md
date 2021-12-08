# telliot

![Version: 1.0.0](https://img.shields.io/badge/Version-1.0.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 5.9.0](https://img.shields.io/badge/AppVersion-5.9.0-informational?style=flat-square)

A Helm chart for Kubernetes

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| container.image | string | `"tellor/telliot:master"` | Docker image for telliot |
| container.port | int | `9090` |  |
| modes | list | `["mine"]` | Array of commands to spawn separate instances of telliot instances with |
| service.port | int | `9090` |  |
| storage | string | `"2Gi"` | telliot persistent storage size |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.5.0](https://github.com/norwoodj/helm-docs/releases/v1.5.0)