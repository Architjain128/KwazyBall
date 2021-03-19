from playsound import playsound
brick = 'sounds/brick.wav'
blast = 'sounds/blast.wav'
gameover = 'sounds/gameover.wav'
winner = 'sounds/winner.mp3'
other = 'sounds/other.wav'
loss = 'sounds/loss.wav'

def play_blast():
    playsound(blast)
def play_brick():
    playsound(brick)
def play_gameover():
    playsound(gameover)
def play_winner():
    playsound(winner)
def play_other():
    playsound(other)
def play_loss():
    playsound(loss)