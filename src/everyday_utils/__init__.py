
#### src/everyday_utils/__init__.py
```python
from .datetime_utils import *
from .file_utils import *
from .hash_utils import *
from .password_utils import *
from .random_utils import *
from .string_utils import *
from .validation_utils import *

__version__ = "0.1.0"
__all__ = [
    "current_datetime",
    "get_file_size",
    "human_readable_size",
    "load_json_file",
    "save_json_file",
    "hash_string",
    "generate_password",
    "random_choice_from_list",
    "flatten_list",
    "unique_list",
    "deep_merge_dicts",
    "mean",
    "median",
    "is_palindrome",
    "is_valid_email",
    "truncate_string",
    "remove_punctuation",
    "slugify",
]