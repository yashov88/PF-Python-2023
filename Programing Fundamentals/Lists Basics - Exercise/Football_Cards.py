cards = input().split(" ")

should_terminate = False

team_a_off_players = []
team_b_off_players = []

for card in cards:
    if card in team_a_off_players or card in team_b_off_players:
        continue
    card_args = card.split("-")
    team_name = card_args[0]
    player_number = card_args[1]

    is_first_team = team_name == "A"
    if is_first_team:
        team_a_off_players.append(card)
    else:
        team_b_off_players.append(card)

    if len(team_a_off_players) > 4 or len(team_b_off_players) > 4:
        should_terminate = True
        break

initial_players = 11
team_a_players = initial_players - len(team_a_off_players)
team_b_players = initial_players - len(team_b_off_players)

print(f"Team A - {team_a_players}; Team B - {team_b_players}")

if should_terminate:
    print("Game was terminated")