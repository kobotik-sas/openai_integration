# openai_integration/models/openai_integration.py

import requests
from odoo import models, api

class OpenAIIntegration(models.Model):
    _name = 'openai.integration'
    _description = 'OpenAI Integration'

    @api.model
    def get_openai_response(self, text):
        config = self.env['openai.config'].search([], limit=1)
        if not config:
            raise ValueError("OpenAI API Key not configured")

        headers = {'Authorization': f'Bearer {config.api_key}'}
        data = {
            'prompt': text,
            'max_tokens': 100,
        }

        response = requests.post(
            'https://api.openai.com/v1/engines/davinci-codex/completions',
            headers=headers,
            json=data
        )

        if response.status_code == 200:
            result = response.json()
            return result
        else:
            raise ValueError(f"Error: {response.status_code}: {response.text}")


