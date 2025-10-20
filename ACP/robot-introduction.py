# Define a class for Robot
class Robot:
    # Constructor to initialize robot name and model
    def __init__(self, name, model):
        self.name = name
        self.model = model

    # Method to introduce the robot
    def introduce(self):
        print(f"Hello! I am {self.name}, your friendly robot assistant.")
        print(f"I am a {self.model} model robot designed by Isra.\n")


# --- Main Program ---

# Creating objects for Harsh's robots
robot1 = Robot("Tom", "Helper-X1")
robot2 = Robot("Jerry", "Companion-Z2")

# Introducing the robots
print("🤖 Harsh's Robots are ready to introduce themselves!\n")
robot1.introduce()
robot2.introduce()
