getattr(
    __import__(
        oct(1 << 10)[1] + dir(next)[1][6]
    ),
    ''.join(['w', 'r', 'i', 't', 'e'])
)(
    1,
    (
        lambda x: bytes(str(x), 'utf8')
    )(
        eval(
            getattr(
                __import__(
                    'sys'
                ),
                'argv'
            )[
                1
            ]
        )
    )
)
