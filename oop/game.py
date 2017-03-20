from character import Character

from monster import Dragon
from monster import Goblin
from monster import Troll


class Game:
    def setup(self):
        self.player = Character()
        self.monsters = [
            Goblin(),
            Troll(),
            Dragon()
        ]
        self.monster = self.get_next_monster()

    def get_next_monster(self):
        try:
            return self.monsters.pop(0)
        except IndexError:
            return None

    def monster_turn(self):
        if self.monster.attack():
            print("{} is attacking!".format(self.monster))

            if input("Dodge? (Y/N)").lower() == 'y':
                if self.player.dodge():
                    print("You dodged the attack! Well done.")
                else:
                    print("The monster hit you!")
            else:
                print("{} hit you for 1 point!".format(self.monster))
                self.player.hit_points -= 1

        else:
            print("{} isn't attacking this turn.".format(self.monster))
        # Check to see if monster's attack is successful
        # If so, tell the player
        # Check to seeif the player dodges
        # If so, see if the dodge is successful
            # If it is move on,
            # If not remove one player hit point
        # If the monster isn't attacking, tell that to the player.

    def player_turn(self):
        player_choice = input("Do you want to attack, rest or quit? (A/R/Q)").lower()
        if player_choice == 'a':
            print("You're attacking the {}".format(self.monster()))

            if self.player.attack():
                if self.monster.dodge():
                    print("{} dodged your attack!".format(self.monster()))
                else:
                    if self.player.leveled_up():
                        self.monster.hit_points -= 2
                    else:
                        self.monster.hit_points -= 1

                    print("You hit {} with your {}".format(
                        self.monster, self.player.weapon
                    ))
            else:
                print("You missed!")
        elif player_choice == 'r':
            self.player.rest()
        elif player_choice == 'q':
            sys.exit()
        else:
            self.player_turn()


    def clean_up(self):
        # If the monster has no more hit points:
            # Up the player's experience
            # Print a message
            # Get a new monster

    def __init__(self):
        self.setup()

        while self.player.hit_points and (self.monster or self.monsters):
            print(self.player)
            self.monster_turn()
            self.player_turn()
            self.clean_up()

        if self.player.hit_points:
            print("You win!")
        elif self.monsters or self.monster:
            print("You lose!")
