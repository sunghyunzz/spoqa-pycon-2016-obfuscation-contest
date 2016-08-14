getattr(__import__("os"), "write")(
    1,
    (
        lambda x: bytes(str(x), 'utf-8')
    )(
        eval(
            getattr(
                __import__("sys"),
                "argv"
            )[1]
        )
    )
)
