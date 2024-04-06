#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # Set the DJANGO_SETTINGS_MODULE environment variable to 'my_project.settings'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')
    try:
        # Try importing the execute_from_command_line function from django.core.management module
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # If Django is not installed or not available, raise ImportError with a helpful message
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Execute Django management commands from the command line with sys.argv    
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # Call the main function if this script is executed directly
    main()
