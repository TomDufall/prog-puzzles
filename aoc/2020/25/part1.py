from itertools import count

MODULUS = 20201227


def transform(subject_number: int, loop_size: int, value: int = 1) -> int:
    for _ in range(loop_size):
        value = (value * subject_number) % MODULUS
    return value


def handshake(card_secret_loop_size: int, door_secret_loop_size: int):
    CARD_SUBJECT_NUMBER = 7
    card_public_key = transform(CARD_SUBJECT_NUMBER, card_secret_loop_size)
    DOOR_SUBJECT_NUMBER = 7
    door_public_key = transform(DOOR_SUBJECT_NUMBER, door_secret_loop_size)
    door_encryption_key = transform(card_public_key, door_secret_loop_size)
    card_encryption_key = transform(door_public_key, card_secret_loop_size)
    if door_encryption_key != card_encryption_key:
        raise ValueError("Keys don't match!")
    return door_encryption_key


def dumb_crack_public_key(key: int) -> int:
    # Calling transform means repeating a lot of work - iterate instead
    subject_number = 7
    value = 1
    for i in count():
        if value == key:
            return i
        value = (value * subject_number) % MODULUS


def break_handshake(card_public_key: int, door_public_key: int) -> int:
    card_loop_size = dumb_crack_public_key(card_public_key)
    return transform(door_public_key, card_loop_size)


if __name__ == "__main__":
    from datetime import datetime
    start = datetime.now()
    CARD_PUBLIC_KEY = 14082811
    DOOR_PUBLIC_KEY = 5249543
    answer = break_handshake(CARD_PUBLIC_KEY, DOOR_PUBLIC_KEY)
    end = datetime.now()
    time = (end - start).total_seconds()
    print(time)
    print(answer)
