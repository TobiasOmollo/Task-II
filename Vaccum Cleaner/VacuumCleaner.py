import random

class VacuumEnvironment:
    def __init__(self):
        # Locations: 0 for Clean, 1 for Dirty
        self.locations = {
            "A": random.choice([0, 1]),
            "B": random.choice([0, 1])
        }
        self.agent_pos = random.choice(["A", "B"])

    def get_status(self, location):
        return self.locations[location]

    def set_status(self, location, status):
        self.locations[location] = status

class ReflexVacuumAgent:
    def __init__(self):
        self.score = 0

    def act(self, environment):
        location = environment.agent_pos
        status = environment.get_status(location)

        print(f"Agent is at Location {location}. Status: {'Dirty' if status == 1 else 'Clean'}")

        # Rule 1: If location is dirty, Suck dirt
        if status == 1:
            print(f"Action: Sucking dirt at {location}...")
            environment.set_status(location, 0)
            self.score += 10
            print(f"Location {location} is now Clean.")
        
        # Rule 2: If at A and clean, move to B
        elif location == "A":
            print("Action: Moving to Location B...")
            environment.agent_pos = "B"
            self.score -= 1 # Moving costs a bit of energy
            
        # Rule 3: If at B and clean, move to A
        elif location == "B":
            print("Action: Moving to Location A...")
            environment.agent_pos = "A"
            self.score -= 1

# --- Execution ---
# Initialize environment and agent
env = VacuumEnvironment()
agent = ReflexVacuumAgent()

print("--- Initial State ---")
print(f"Room A: {'Dirty' if env.locations['A'] == 1 else 'Clean'}")
print(f"Room B: {'Dirty' if env.locations['B'] == 1 else 'Clean'}")
print("-" * 20)

# Agent  check to all rooms
for step in range(1, 5):
    print(f"\nStep {step}:")
    agent.act(env)
    
    # Exit if all rooms are clean
    if env.locations["A"] == 0 and env.locations["B"] == 0:
        print("\nAll locations are clean! Task complete.")
        break

print(f"\nFinal Agent Score: {agent.score}")
