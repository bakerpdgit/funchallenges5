# Battle game by Nachiketh Prabhu

attacks = ["punch"]  # Add more attacks here
monster_health = 5
print("A monster appears!")

# Add a while loop here for task 1

print("Choose your attack:")
print(attacks)
choice = input("> ").lower()

if choice in attacks:
    damage = 1
    monster_health -= damage
    print("You used", choice)
    print("You dealt", damage, "damage!")
    print("Monster health:", monster_health)
else:
    print("That's not a valid attack.")
