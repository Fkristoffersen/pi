from typing import Any, Optional, Sequence, Union

from django.apps.config import AppConfig
from django.core.checks.messages import CheckMessage, Error, Warning
from django.urls.resolvers import URLPattern, URLResolver

def check_url_config(app_configs: Optional[Sequence[AppConfig]], **kwargs: Any) -> Sequence[CheckMessage]: ...
def check_resolver(resolver: Union[URLPattern, URLResolver]) -> Sequence[CheckMessage]: ...
def check_url_namespaces_unique(app_configs: Optional[Sequence[AppConfig]], **kwargs: Any) -> Sequence[Warning]: ...
def get_warning_for_invalid_pattern(pattern: Any) -> Sequence[Error]: ...
def check_url_settings(app_configs: Optional[Sequence[AppConfig]], **kwargs: Any) -> Sequence[Error]: ...
def E006(name: str) -> Error: ...
