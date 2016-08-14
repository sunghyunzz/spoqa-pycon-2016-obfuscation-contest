import sys
import os

os.write(
    1,
    (
        lambda x: bytes(str(x), 'utf-8')
    )(
        eval(sys.argv[1])
    )
)
