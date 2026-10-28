"""Public identity shared by validation and publishing."""
from urllib.parse import urlencode
NAME = 'ToolIndex'
SITE = 'https://toolindex.org/'
BASE = '/'
# Repository identity is independent of the public product name.
REPOSITORY = 'https://github.com/OpenRootdev/toolindex'
FORM = REPOSITORY + '/issues/new?' + urlencode({
    'title': '[Tool] ',
    'labels': 'submission',
    'body': '## Tool name and type\n\n## Source repository or official documentation\n\n'
            '## Purpose and category\n\n## Installation or connection steps\n\n'
            '## Package or service URL, version, license or terms\n\n'
            '## Manual setup, authentication and costs\nDo not include secrets.\n\n'
            '## Logo or custom image (optional)\nImage URL, source and alt text, or leave blank.\n\n'
            '## Optional composition and test evidence\n',
})
TOOL_TYPES = ['Skill', 'MCP server', 'CLI', 'API', 'Library', 'Plugin', 'Workflow', 'Harness', 'Other']
LEGACY_SITES = [
    'https://openrootdev.github.io/harness-library/',
    'https://kaelux-labs.github.io/harness-library/',
    'https://ker102.github.io/harness-library/',
]
