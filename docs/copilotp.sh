#!/bin/bash

# Setting the base URL turns on BYOK mode (no GitHub auth needed for models)
export COPILOT_PROVIDER_BASE_URL=https://rgvaiclass.com/v1
export COPILOT_PROVIDER_TYPE=openai

# Sent as "Authorization: Bearer <key>"
export COPILOT_PROVIDER_API_KEY=YOUR_KEY_HERE

# Must match a model the proxy serves
export COPILOT_MODEL='gpt-6-luna'

# Copilot recommends "responses"
export COPILOT_PROVIDER_WIRE_API=responses

copilot "$@"
