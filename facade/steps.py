def step(action, error_message='Something went wrong...'):
    try:
        action()
    except Exception:
        print(error_message)
        raise  # <-- re-raise to fail the test immediately