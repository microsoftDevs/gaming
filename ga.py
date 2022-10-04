import pygame
from pygame import *
import random
jump_sound = pygame.mixer.Sound('resources/jump.wav')
die_sound = pygame.mixer.Sound('resources/die.wav')
checkPoint_sound = pygame.mixer.Sound('resources/checkPoint.wav')
def load_image(
name,
sx=-1,
sy=-1,
colorkey=None,
):

fullname = os.path.join('resources', name)
img = pygame.image.load(fullname)
img = img.convert()
if colorkey is not None:
if colorkey == -1:
colorkey = img.get_at((0, 0))
img.set_colorkey(colorkey, RLEACCEL)

if sx != -1 or sy != -1:
img = pygame.transform.scale(img, (sx, sy))

return (img, img.get_rect())

def gameover_display_message(rbtn_image, gmo_image):
rbtn_rect = rbtn_image.get_rect()
rbtn_rect.centerx = width_screen / 2
rbtn_rect.top = height_screen * 0.52

gmo_rect = gmo_image.get_rect()
gmo_rect.centerx = width_screen / 2
gmo_rect.centery = height_screen * 0.35

screen_layout_display.blit(rbtn_image, rbtn_rect)
screen_layout_display.blit(gmo_image, gmo_rect)

class Cactus(pygame.sprite.Sprite):
def __init__(self, speed=5, sx=-1, sy=-1):
pygame.sprite.Sprite.__init__(self,self.containers)
self.imgs, self.rect = load_sprite_sheet('cactus-small.png', 3, 1, sx, sy, -1)
self.rect.bottom = int(0.98 * height_screen)
self.rect.left = width_screen + self.rect.width
self.image = self.imgs[random.randrange(0, 3)]
self.movement = [-1*speed,0]

def draw(self):
screen_layout_display.blit(self.image, self.rect)

def update(self):
self.rect = self.rect.move(self.movement)

if self.rect.right < 0:
self.kill()
