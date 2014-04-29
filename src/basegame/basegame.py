#!/usr/bin/python3

# Client running code, isolated and keep process available for stdin and stdout
#  maybe make this a class

from queue import Queue
from subprocess import Popen,PIPE

class BaseGame:
    def __init__(self, players):
        self.players = players
        # Use list of workers
        self.player_handles = []
        self.initialize_game()

    # Depends on the game, but all will call launch on subprocesses
    def initialize_game():
        for player in self.players:
            self.player_handles.append(launch(player))
        
    # Launch the client (AI) code and keep a process handle to send IO
    def launch(self, player):
        pass
        # will return process handle

    # Send output from game to stdin client
    def send_to_player(self, player):
        pass

    # make synchronous or asynchronous
    # Send output from client to game
    def receive_from_player(self, player):
        pass

    # End processes if they haven't ended already and output results given from game
    def complete(self):
        pass

# this will read all IO and add to queues
def monitor(worker):
    pass
        
class Worker:
    pass

if __name__ == '__main__':
    pass