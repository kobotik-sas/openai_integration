# openai_integration/models/openai_config.py

from odoo import models, fields

class OpenAIConfig(models.Model):
    _name = 'openai.config'
    _description = 'OpenAI Configuration'

    api_key = fields.Char(string='API Key', required=True)
