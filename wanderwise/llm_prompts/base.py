"""Defines Prompts and System Instructions for AI to use."""


class Prompt:
    def __init__(self, template):
        """Initializes a Prompt instance.
        Args:
            template: The template string.
        """
        self.template = template

    def format(self, **kwargs):
        """
        Formats the template string dynamically.
        Args:
            **kwargs:

        Returns:
            The formatted string (variables attached).
        """
        return self.template.format(**kwargs)
