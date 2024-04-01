from game import Agent
from game import Directions
import random

class DumbAgent(Agent):
    def getAction(self, state):
        print("Location: ", state.getPacmanPosition())
        print("Actions available: ", state.getLegalPacmanActions())
        if Directions.WEST in state.getLegalPacmanActions():
            print("Going East.")
            return Directions.WEST
        else:
            print("Stopping.")
            return Directions.STOP
class RandomAgent(Agent):
    def getAction(self, state):
        legal_actions = state.getLegalPacmanActions()
        return random.choice(legal_actions)

class BetterRandomAgent(Agent):
    def getAction(self, state):
        legal_actions = state.getLegalPacmanActions()
        if Directions.STOP in legal_actions:
            legal_actions.remove(Directions.STOP)
        return random.choice(legal_actions)

class ReflexAgent(Agent):
    def getAction(self, state):
        legal_actions = state.getLegalPacmanActions()

        # Check if any immediate action leads to eating a food pellet
        for action in legal_actions:
            successor = state.generatePacmanSuccessor(action)
            next_pos = successor.getPacmanPosition()
            if next_pos in state.getCapsules() or next_pos in state.getFood().asList():
                return action
        # If no immediate action leads to food, choose randomly (excluding 'Stop')
        legal_actions.remove(Directions.STOP)
        return random.choice(legal_actions)