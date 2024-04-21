import sys 
import pygame 
from settings import Settings
from ship import Ship
from bullet import Bullet

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

        # full screen mode
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        self.settings.screen_width = self.screen.get_rect().width

        self.settings.screen_height = self.screen.get_rect().height

    
        # display the caption of the game 
        pygame.display.set_caption("Alien Invasion")

        # create a new ship 
        self.ship = Ship(self)

        # Set the background color. 
        self.bg_color = (230, 230, 230)

        # create the group of the bullets 
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
    
    def _check_events(self): 
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            # quit the game if clicking the X button on the window.
            if event.type == pygame.QUIT: 
                sys.exit() 
            # change the status of the ship
            elif event.type == pygame.KEYDOWN: 
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event): 
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT: 
            self.ship.moving_right = True 
        elif event.key == pygame.K_LEFT: 
            self.ship.moving_left = True
        # Pressing Q to QUit
        elif event.key == pygame.K_q: 
            sys.exit()
        elif event.key == pygame.K_SPACE: 
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False  
        elif event.key == pygame.K_LEFT: 
            self.ship.moving_left = False
    
    def _fire_bullet(self): 
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed: 
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self): 
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop. 
        self.screen.fill(self.settings.bg_color)

        for bullet in self.bullets.sprites(): 
            bullet.draw_bullet()

        # draw the ship
        self.ship.blitme()

        # Make the most recently drawn screen visible
        pygame.display.flip()

    def _update_bullets(self): 
        """Update position of bullets and get rid of old bullets."""
        # Update the bullets
        self.bullets.update()

        # Get rid of bullets that have disappeared. 
        for bullet in self.bullets.copy(): 
            if bullet.rect.bottom <= 0: 
                self.bullets.remove(bullet)
            




    def run_game(self): 
        """Start the main loop for the game."""
        while True: 

            # call the check events
            self._check_events()
            
            # call the update function
            self.ship.update()

            # call the update function 
            self._update_bullets()
            
            # call the update screen function
            self._update_screen()

            # create the screen frame of 60 -> game run consistently on every system. 
            self.clock.tick(60)

            




if __name__ == "__main__": 
    # Make a game instance, and run the game. 
    ai = AlienInvasion()
    ai.run_game()
