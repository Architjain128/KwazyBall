# Kwazzy Ball
## Overview
A terminal based implementation that tries to simulate the classic DX-Ball game (brick and ball) written in python3 without using any GUI library and using colorama only for addition of colours.

## How to run
+ Install the required packages
   ```
   $ pip3 install -r requirements.txt
   ```

+ Good Luck for the game
   ```
   $ python3 game.py
   ```

## Controls
- <kbd>A</kbd> or <kbd>a</kbd>: move left
- <kbd>D</kbd> or <kbd>d</kbd>: move right
- <kbd>SPACE</kbd> : launch ball
- <kbd>P</kbd> or <kbd>p</kbd>: pause
- <kbd>R</kbd> or <kbd>r</kbd>: resume
- <kbd>Q</kbd> or <kbd>q</kbd>: quit
- <kbd>z</kbd> : Level Up

## Assumptions
+ bullet cannot explode yellow bricks
+ powerup over in 10 seconds

## Featurs
+ Show play time 
+ Multiple Lives
+ Show score 
+ Multiple Levels are created
+ Powerup galls in parabolic path on dependent of ball hiting and can be collected by paddle 
+ Ball speed changes in x according to point of contaact on paddle
+ `Yellow` brick explodes in chain and also expoldes all surrounded bricks
+ `White` brick is unbreakable 
+ Level 1
    + have powerup
    + no falling sky
    + Rainbow bricks
+ Level 2
    + No powerups
    + Bullets with interval of 1 sec
    + Falling sky after 60 seconds in interval of 5 hits on paddle
    + No rainbow bricks
+ Level 3
    + No powerups
    + Ufo with health
    + Fallig Boom on paddle
    + No rainbow bricks
+ Sound
+ Fireball

### Bricks Strength
+ <kbd>CYAN</kbd> : 1 strength
+ <kbd>Blue</kbd> : 2 strength
+ <kbd>Red</kbd> : 3 strength
+ <kbd>Green</kbd> : 4 strength
+ <kbd>Yellow</kbd> : Expolding Brick
+ <kbd>Gray</kbd> : Unbreakable
+ <kbd>Multi color</kbd> : Rainbow Brick

## Powerups
Each disables after for  10 seconds
1. Large Paddle
2. Small Paddle
3. Sticky Paddle
4. Thru Ball
5. Fast Ball
6. Multi Ball
7. Fireball

## Classes
+ Scene
+ Ball
+ Paddle
+ Scoreboard
    + Time
    + Lives
    + Level
    + Level_change_flag
    + Score
    + Pause
+ Bullet
+ Bullets
+ Ufo
+ Boom

## OOPS Concepts
### Inheritace
`Time`, `Lives`, `Level`
    , `Level_change_flag`
    , `Score`
    and `Pause` are inherited classes of `Scoreboard`
### Polymorphism
Some function are added and some are changed in inherited class `Scoreboard`
+ Added
    + `sub_life()`, `add_life()` and `add_in_scene()` function in `Lives`
    + `update_val(...)`and `return_value()` function in `Time`
    + `update_val(...)` and `add_in_scene(...)` function in `Score`
    + `toggle_pause()` in `Pause`
    + `update_val()` and `add_in_scene(...)` function  in `Level`
    + `set_val(...)`  function in `Level_change_flag`
+ Changed
    + `return_val()`  function in `Time`

### Encapsulation
The entire game is modelled using classes and objects which encapsulate logically different entities.
### Abstraction
Things like `scene.generate(...)`, `ball.collison_check(...)`, `ball.move()`, `paddle.move_left()`, `paddle.move_right()` and many more function are used in abstracted way 

## Extra
+ Initial value can be changed in `config.py`
+ Didn't apply brick generation by ufo

