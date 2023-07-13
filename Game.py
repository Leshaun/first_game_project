from Templates import CreatureTemplate
from random import randint

character = CreatureTemplate("", "", 2, 2, 2)
character.name = input("Please enter your characters name: ")

creatures = [
    CreatureTemplate("a", "mad rat", 1, 1, 1),
    CreatureTemplate("a", "venomous spider", 2, 2, 3),
    CreatureTemplate("a", "hungry wolf", 3, 1, 2),
    CreatureTemplate("an", "evil goblin", 2, 3, 2),
    CreatureTemplate("a", "vicious dragon", 3, 3, 3)
]

print("You are " + character.name + " and you are about to embark on an adventure.\n"
                                    "First though, what about your background?\n"
                                    "(a) You are the strongest in the village.\n"
                                    "(b) You are the toughest in the village.\n"
                                    "(c) You are the fastest in the village.")

while True:
    character_background = input()
    if character_background == "a":
        character.strength += 1
        print("You are the strongest in the village!\nYour starting strength has been improved.")
        break
    elif character_background == "b":
        character.defense += 1
        print("You are the toughest in the village!\nYour starting defense has been improved.")
        break
    elif character_background == "c":
        character.speed += 1
        print("You are the fastest in the village!\nYour starting speed has been improved.")
        break
    else:
        print("Please enter your background:\n(a) The strongest\n(b) The toughest\n(c) The fastest")

print("\nHaving remembered all relevant details about yourself, "
      "such as your name and background, "
      "you are now ready to begin your adventure.\n"
      "Heading out of your village, you see two paths:\n"
      "(a) The left path leads into the gloomy forest.\n"
      "(b) The right path leads into the ominous mountain.")

while True:
    first_path_taken = input()
    if first_path_taken == "a":
        print("You enter the gloomy forest.")
        encounter_gf = randint(0, 2)
        if encounter_gf == 0:
            print("You encounter " + creatures[0].article + " " + creatures[0].name + ".")
            if character.speed >= creatures[0].speed:
                if character.strength > creatures[0].defense:
                    print("You easily dispatch the " + creatures[0].name + ".")
                    break
                elif creatures[0].strength > character.defense:
                    print("You are defeated by the " + creatures[0].name + ".")
                    exit()
                else:
                    print("Neither of you perceiving any weakness in the other, "
                          "you shake hands and go your separate ways.")
                    break
            else:
                if creatures[0].strength > character.defense:
                    print("You are defeated by the " + creatures[0].name + ".")
                    exit()
                elif character.strength > creatures[0].defense:
                    print("You easily dispatch the " + creatures[0].name + ".")
                    break
                else:
                    print("Neither of you perceiving any weakness in the other, "
                          "you shake hands and go your separate ways.")
                    break
        elif encounter_gf == 1:
            print("You encounter " + creatures[1].article + " " + creatures[1].name + ".")
            if character.speed >= creatures[1].speed:
                if character.strength > creatures[1].defense:
                    print("You easily dispatch the " + creatures[1].name + ".")
                    print("The deadly ordeal has made you faster.")
                    character.speed += 1
                    break
                elif creatures[1].strength > character.defense:
                    print("You are defeated by the " + creatures[1].name + ".")
                    exit()
                else:
                    print("Neither of you perceiving any weakness in the other, "
                          "you shake hands and go your separate ways.")
                    break
            else:
                if creatures[1].strength > character.defense:
                    print("You are defeated by the " + creatures[1].name + ".")
                    exit()
                elif character.strength > creatures[1].defense:
                    print("You easily dispatch the " + creatures[1].name + ".")
                    print("The deadly ordeal has made you faster.")
                    character.speed += 1
                    break
                else:
                    print("Neither of you perceiving any weakness in the other, "
                          "you shake hands and go your separate ways.")
                    break
        else:
            print("You encounter " + creatures[2].article + " " + creatures[2].name + ".")
            if character.speed >= creatures[2].speed:
                if character.strength > creatures[2].defense:
                    print("You easily dispatch the " + creatures[2].name + ".")
                    print("The deadly ordeal has made you stronger.")
                    character.strength += 1
                    break
                elif creatures[2].strength > character.defense:
                    print("You are defeated by the " + creatures[2].name + ".")
                    exit()
                else:
                    print("Neither of you perceiving any weakness in the other, "
                          "you shake hands and go your separate ways.")
                    break
            else:
                if creatures[2].strength > character.defense:
                    print("You are defeated by the " + creatures[2].name + ".")
                    exit()
                elif character.strength > creatures[2].defense:
                    print("You easily dispatch the " + creatures[2].name + ".")
                    print("The deadly ordeal has made you stronger.")
                    character.strength += 1
                    break
                else:
                    print("Neither of you perceiving any weakness in the other, "
                          "you shake hands and go your separate ways.")
                    break
    elif first_path_taken == "b":
        print("You enter the ominous mountain.")
        encounter_om = randint(1, 3)
        if encounter_om == 1:
            print("You encounter " + creatures[1].article + " " + creatures[1].name + ".")
            if character.speed >= creatures[1].speed:
                if character.strength > creatures[1].defense:
                    print("You easily dispatch the " + creatures[1].name + ".")
                    print("The deadly ordeal has made you faster.")
                    character.speed += 1
                    break
                elif creatures[1].strength > character.defense:
                    print("You are defeated by the " + creatures[1].name + ".")
                    exit()
                else:
                    print("Neither of you perceiving any weakness in the other, "
                          "you shake hands and go your separate ways.")
                    break
            else:
                if creatures[1].strength > character.defense:
                    print("You are defeated by the " + creatures[1].name + ".")
                    exit()
                elif character.strength > creatures[1].defense:
                    print("You easily dispatch the " + creatures[1].name + ".")
                    print("The deadly ordeal has made you faster.")
                    character.speed += 1
                    break
                else:
                    print("Neither of you perceiving any weakness in the other, "
                          "you shake hands and go your separate ways.")
                    break
        elif encounter_om == 2:
            print("You encounter " + creatures[2].article + " " + creatures[2].name + ".")
            if character.speed >= creatures[2].speed:
                if character.strength > creatures[2].defense:
                    print("You easily dispatch the " + creatures[2].name + ".")
                    print("The deadly ordeal has made you stronger.")
                    character.strength += 1
                    break
                elif creatures[2].strength > character.defense:
                    print("You are defeated by the " + creatures[2].name + ".")
                    exit()
                else:
                    print("Neither of you perceiving any weakness in the other, "
                          "you shake hands and go your separate ways.")
                    break
            else:
                if creatures[2].strength > character.defense:
                    print("You are defeated by the " + creatures[2].name + ".")
                    exit()
                elif character.strength > creatures[2].defense:
                    print("You easily dispatch the " + creatures[2].name + ".")
                    print("The deadly ordeal has made you stronger.")
                    character.strength += 1
                    break
                else:
                    print("Neither of you perceiving any weakness in the other, "
                          "you shake hands and go your separate ways.")
                    break
        else:
            print("You encounter " + creatures[3].article + " " + creatures[3].name + ".")
            if character.speed >= creatures[3].speed:
                if character.strength > creatures[3].defense:
                    print("You easily dispatch the " + creatures[3].name + ".")
                    print("The deadly ordeal has made you tougher.")
                    character.defense += 1
                    break
                elif creatures[3].strength > character.defense:
                    print("You are defeated by the " + creatures[3].name + ".")
                    exit()
                else:
                    print("Neither of you perceiving any weakness in the other, "
                          "you shake hands and go your separate ways.")
                    break
            else:
                if creatures[3].strength > character.defense:
                    print("You are defeated by the " + creatures[3].name + ".")
                    exit()
                elif character.strength > creatures[3].defense:
                    print("You easily dispatch the " + creatures[3].name + ".")
                    print("The deadly ordeal has made you tougher.")
                    character.defense += 1
                    break
                else:
                    print("Neither of you perceiving any weakness in the other, "
                          "you shake hands and go your separate ways.")
                    break
    else:
        print("Please choose a path:\n(a) The gloomy forest\n(b) The ominous mountain")

print("\nThe next leg of your journey takes you to a fork in the path:\n"
      "(a) The left path leads into the funky swamp.\n"
      "(b) The right path leads into the hostile glacier.")

while True:
    second_path_taken = input()
    if second_path_taken == "a":
        print("You enter the funky swamp.")
        encounter_fs = randint(1, 3)
        if encounter_fs == 1:
            print("You encounter " + creatures[1].article + " " + creatures[1].name + ".")
            if character.speed >= creatures[1].speed:
                if character.strength > creatures[1].defense:
                    print("You easily dispatch the " + creatures[1].name + ".")
                    print("The deadly ordeal has made you faster.")
                    character.speed += 1
                    break
                elif creatures[1].strength > character.defense:
                    print("You are defeated by the " + creatures[1].name + ".")
                    exit()
                else:
                    print("Neither of you perceiving any weakness in the other, "
                          "you shake hands and go your separate ways.")
                    break
            else:
                if creatures[1].strength > character.defense:
                    print("You are defeated by the " + creatures[1].name + ".")
                    exit()
                elif character.strength > creatures[1].defense:
                    print("You easily dispatch the " + creatures[1].name + ".")
                    print("The deadly ordeal has made you faster.")
                    character.speed += 1
                    break
                else:
                    print("Neither of you perceiving any weakness in the other, "
                          "you shake hands and go your separate ways.")
                    break
        elif encounter_fs == 2:
            print("You encounter " + creatures[2].article + " " + creatures[2].name + ".")
            if character.speed >= creatures[2].speed:
                if character.strength > creatures[2].defense:
                    print("You easily dispatch the " + creatures[2].name + ".")
                    print("The deadly ordeal has made you stronger.")
                    character.strength += 1
                    break
                elif creatures[2].strength > character.defense:
                    print("You are defeated by the " + creatures[2].name + ".")
                    exit()
                else:
                    print("Neither of you perceiving any weakness in the other, "
                          "you shake hands and go your separate ways.")
                    break
            else:
                if creatures[2].strength > character.defense:
                    print("You are defeated by the " + creatures[2].name + ".")
                    exit()
                elif character.strength > creatures[2].defense:
                    print("You easily dispatch the " + creatures[2].name + ".")
                    print("The deadly ordeal has made you stronger.")
                    character.strength += 1
                    break
                else:
                    print("Neither of you perceiving any weakness in the other, "
                          "you shake hands and go your separate ways.")
                    break
        else:
            print("You encounter " + creatures[3].article + " " + creatures[3].name + ".")
            if character.speed >= creatures[3].speed:
                if character.strength > creatures[3].defense:
                    print("You easily dispatch the " + creatures[3].name + ".")
                    print("The deadly ordeal has made you tougher.")
                    character.defense += 1
                    break
                elif creatures[3].strength > character.defense:
                    print("You are defeated by the " + creatures[3].name + ".")
                    exit()
                else:
                    print("Neither of you perceiving any weakness in the other, "
                          "you shake hands and go your separate ways.")
                    break
            else:
                if creatures[3].strength > character.defense:
                    print("You are defeated by the " + creatures[3].name + ".")
                    exit()
                elif character.strength > creatures[3].defense:
                    print("You easily dispatch the " + creatures[3].name + ".")
                    print("The deadly ordeal has made you tougher.")
                    character.defense += 1
                    break
                else:
                    print("Neither of you perceiving any weakness in the other, "
                          "you shake hands and go your separate ways.")
                    break
    elif second_path_taken == "b":
        print("You enter the hostile glacier.")
        encounter_hg = randint(2, 4)
        if encounter_hg == 2:
            print("You encounter " + creatures[2].article + " " + creatures[2].name + ".")
            if character.speed >= creatures[2].speed:
                if character.strength > creatures[2].defense:
                    print("You easily dispatch the " + creatures[2].name + ".")
                    print("The deadly ordeal has made you stronger.")
                    character.strength += 1
                    break
                elif creatures[2].strength > character.defense:
                    print("You are defeated by the " + creatures[2].name + ".")
                    exit()
                else:
                    print("Neither of you perceiving any weakness in the other, "
                          "you shake hands and go your separate ways.")
                    break
            else:
                if creatures[2].strength > character.defense:
                    print("You are defeated by the " + creatures[2].name + ".")
                    exit()
                elif character.strength > creatures[2].defense:
                    print("You easily dispatch the " + creatures[2].name + ".")
                    print("The deadly ordeal has made you stronger.")
                    character.strength += 1
                    break
                else:
                    print("Neither of you perceiving any weakness in the other, "
                          "you shake hands and go your separate ways.")
                    break
        elif encounter_hg == 3:
            print("You encounter " + creatures[3].article + " " + creatures[3].name + ".")
            if character.speed >= creatures[3].speed:
                if character.strength > creatures[3].defense:
                    print("You easily dispatch the " + creatures[3].name + ".")
                    print("The deadly ordeal has made you tougher.")
                    character.defense += 1
                    break
                elif creatures[3].strength > character.defense:
                    print("You are defeated by the " + creatures[3].name + ".")
                    exit()
                else:
                    print("Neither of you perceiving any weakness in the other, "
                          "you shake hands and go your separate ways.")
                    break
            else:
                if creatures[3].strength > character.defense:
                    print("You are defeated by the " + creatures[3].name + ".")
                    exit()
                elif character.strength > creatures[3].defense:
                    print("You easily dispatch the " + creatures[3].name + ".")
                    print("The deadly ordeal has made you tougher.")
                    character.defense += 1
                    break
                else:
                    print("Neither of you perceiving any weakness in the other, "
                          "you shake hands and go your separate ways.")
                    break
        else:
            print("You encounter " + creatures[4].article + " " + creatures[4].name + ".")
            if character.speed >= creatures[4].speed:
                if character.strength > creatures[4].defense:
                    print("You easily dispatch the " + creatures[4].name + ".")
                    print("Realizing any future accomplishments will forever be overshadowed by you slaying "
                          + creatures[4].article + " " + creatures[4].name +
                          ", you decide to hang up your adventuring mantle.")
                    exit()
                elif creatures[4].strength > character.defense:
                    print("You are defeated by the " + creatures[4].name + ".")
                    exit()
                else:
                    print("Neither of you perceiving any weakness in the other, "
                          "you shake hands and go your separate ways.")
                    break
            else:
                if creatures[4].strength > character.defense:
                    print("You are defeated by the " + creatures[4].name + ".")
                    exit()
                elif character.strength > creatures[4].defense:
                    print("You easily dispatch the " + creatures[4].name + ".")
                    print("Realizing any future accomplishments will forever be overshadowed by you slaying "
                          + creatures[4].article + " " + creatures[4].name +
                          ", you decide to hang up your adventuring mantle.")
                    break
                else:
                    print("Neither of you perceiving any weakness in the other, "
                          "you shake hands and go your separate ways.")
                    break
    else:
        print("Please choose a path:\n(a) The funky swamp\n(b) The hostile glacier")

print("\nFilled with determination, you continue your adventure to the perilous volcano.")
print("You encounter " + creatures[4].article + " " + creatures[4].name + ".")
if character.speed >= creatures[4].speed:
    if character.strength > creatures[4].defense:
        print("You easily dispatch the " + creatures[4].name + ".")
        print("Realizing any future accomplishments will forever be overshadowed by you slaying "
              + creatures[4].article + " " + creatures[4].name +
              ", you decide to hang up your adventuring mantle.")
        exit()
    elif creatures[4].strength > character.defense:
        print("You are defeated by the " + creatures[4].name + ".")
        exit()
    else:
        print("Neither of you perceiving any weakness in the other, "
              "you shake hands and go your separate ways.\n"
              "Feeling done with adventuring, you decide to head home to your village.\n"
              "Upon arrival you find it burnt to a crisp by the "
              + creatures[4].name +
              ".\nThere are no survivors.")
        exit()
else:
    if creatures[4].strength > character.defense:
        print("You are defeated by the " + creatures[4].name + ".")
        exit()
    elif character.strength > creatures[4].defense:
        print("You easily dispatch the " + creatures[4].name + ".")
        print("Realizing any future accomplishments will forever be overshadowed by you slaying "
              + creatures[4].article + " " + creatures[4].name +
              ", you decide to hang up your adventuring mantle.")
        exit()
    else:
        print("Neither of you perceiving any weakness in the other, "
              "you shake hands and go your separate ways.\n"
              "Feeling done with adventuring, you decide to head home to your village.\n"
              "Upon arrival you find it burnt to a crisp by the "
              + creatures[4].name +
              ".\nThere are no survivors.")
        exit()
