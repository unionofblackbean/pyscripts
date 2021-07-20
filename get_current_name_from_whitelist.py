from uuid_to_name import *
import json


def main():
    with open("./whitelist.json", "r", encoding="utf8") as whitelist_file:
        whitelist_json = json.load(whitelist_file)

    player_names = []
    for player in whitelist_json:
        player_uuid = player.get("uuid")
        if player_uuid:
            player_name = uuid_to_current_name(uuid.UUID(player_uuid))
            print(player_name)
            if player_name:
                player_names.append(player_name)

    with open("./whitelist_names.txt", "w+", encoding="utf8") as whitelist_names_file:
        for player_name in player_names:
            whitelist_names_file.write(f"{player_name}\n")


if __name__ == "__main__":
    main()
