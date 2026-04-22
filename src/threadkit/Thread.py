# imports
from concurrent.futures import ThreadPoolExecutor
from typing import Callable, Any

# user imports
from src.threadkit.utils import Retry, HandleException

# functions
def Thread(
    func : Callable[..., Any] | None = None,
    items : list[dict] | None = None,
    workers : int = 8,
    attempts : int = 1,
    results : bool = False,
    timeout : int | None = None,
    ordered : bool = False,
    callback : Callable[..., Any] | None = None,
    exception : Callable[..., Any] | None = None,
    progress : bool = False,
) -> None:

    return