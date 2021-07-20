import json
import uuid
import requests
import typing


def uuid_to_current_name(uuid_: uuid.UUID) -> str:
    history = uuid_to_name_history(uuid_)
    return history[-1] if history else None


def uuid_to_name_history(uuid_: uuid.UUID) -> typing.List[str]:
    if uuid_:
        res = requests.get(f"https://api.mojang.com/user/profiles/{str(uuid_)}/names")
        if res.status_code != 200:
            return None

        names = []
        res_j = json.loads(res.text)
        for name_history in res_j:
            name = name_history.get("name")
            if name:
                names.append(name)
        return names
    else:
        return None
