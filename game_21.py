from random import randint


def game():
    def reload():
        if not input('If you want to continue press Enter\nInput | '):
            game()

    def dash():
        return '-' * 16 + '\n'

    def print_dash():
        print(dash(), end='')

    def roll_dice():
        return randint(1, 11)

    def player():
        score = 0
        print_dash()
        while input(
                f'Your score: {score}\n{dash()}continue | enter\nstop     | hold\n{dash()}Your action | ') != 'hold':
            print_dash()
            score += roll_dice()
            if score == 21:
                print(f'Your Score: {score}\nYou Win')
                print_dash()
                reload()
            elif score > 21:
                print(f'Your Score: {score}\nYou Lose')
                print_dash()
                reload()
        print_dash()
        print(f'Your score: {score}')
        print_dash()
        return score

    def dealer():
        score = 0
        while score < 17:
            print(f'Dealer score: {score}')
            score += roll_dice()
        print(f'Dealer score: {score}')
        print_dash()
        if score > 21:
            print('You Win')
            print_dash()
            reload()
        return score

    player_score = player()
    dealer_score = dealer()

    if player_score > dealer_score:
        print('You Win')
    elif player_score < dealer_score:
        print('You Lose')
    else:
        print('Draw')
    print_dash()
    reload()


if __name__ == '__main__':
    game()
