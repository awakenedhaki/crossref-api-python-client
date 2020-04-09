from pathlib import Path

import crossrefapiclient
from poetry_publish.publish import poetry_publish


def publish():
    poetry_publish(
        package_root=Path(crossrefapiclient.__file__).parent.parent,
        version=crossrefapiclient.__version__,
    )