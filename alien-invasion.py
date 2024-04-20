import sys 
import pygame 
from settings import Settings
from ship import Ship

class AlienInvasion: 
    """Overall class to manage game assets and behavior."""

    def __init__(self): 
        """Initialize the game, and create game resources."""
        # initialize the game
        pygame.init()

        # define the clock 
        self.clock = pygame.time.Clock()

        # create the settings instance
        self.settings = Settings()

        # take the parameters and display on the screen
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

    
        # display the caption of the game 
        pygame.display.set_caption("Alien Invasion")

        # create a new ship 
        self.ship = Ship(self)

        # Set the background color. 
        self.bg_color = (230, 230, 230)
    
    def run_game(self): 
        """Start the main loop for the game."""
        while True: 
            # Watch for keyboard and mouse events. 
            for event in pygame.event.get():
                # quit the game if clicking the X button on the window.
                if event.type == pygame.QUIT: 
                    sys.exit() 
            
            # Redraw the screen during each pass through the loop. 
            self.screen.fill(self.settings.bg_color)

            # draw the ship
            self.ship.blitme()

            # create the screen frame of 60 -> game run consistently on every system. 
            self.clock.tick(60)

            # Make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == "__main__": 
    # Make a game instance, and run the game. 
    ai = AlienInvasion()
    ai.run_game()
