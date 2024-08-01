import java.util.Scanner;
import java.util.Random;

public class DiceGame {

    private static final int MAX_SCORE = 21;
    private static final Scanner SCANNER = new Scanner(System.in);
    private static final Random RANDOM = new Random();

    public static void main(String[] args) {
        game();
    }

    private static void game() {
        int playerScore = playerTurn();
        int dealerScore = dealerTurn();

        System.out.println("Player Score: " + playerScore);
        System.out.println("Dealer Score: " + dealerScore);

        if (playerScore > dealerScore && playerScore <= MAX_SCORE) {
            System.out.println("You Win!");
        } else if (dealerScore > playerScore && dealerScore <= MAX_SCORE) {
            System.out.println("You Lose!");
        } else if (playerScore == dealerScore) {
            System.out.println("Draw!");
        } else {
            if (playerScore > MAX_SCORE) {
                System.out.println("You Lose! (Bust)");
            } else {
                System.out.println("You Lose! (Bust)");
            }
        }

        if (askToContinue()) {
            game();
        }
    }

    private static int playerTurn() {
        int score = 0;
        printDash();
        while (true) {
            System.out.println("Your Score: " + score);
            printDash();
            System.out.println("continue | enter");
            System.out.println("stop     | hold");
            printDash();
            System.out.print("Your action | ");
            String action = SCANNER.nextLine().trim();
            printDash();

            if (action.equals("hold")) {
                break;
            }

            score += rollDice();
            if (score == MAX_SCORE) {
                System.out.println("Your Score: " + score);
                System.out.println("You Win!");
                printDash();
                return score;
            } else if (score > MAX_SCORE) {
                System.out.println("Your Score: " + score);
                System.out.println("You Lose! (Bust)");
                printDash();
                return score;
            }
        }
        System.out.println("Your score: " + score);
        printDash();
        return score;
    }

    private static int dealerTurn() {
        int score = 0;
        while (score < 17) {
            System.out.println("Dealer score: " + score);
            score += rollDice();
        }
        System.out.println("Dealer score: " + score);
        printDash();
        if (score > MAX_SCORE) {
            System.out.println("You Win! (Dealer Bust)");
            printDash();
        }
        return score;
    }

    private static int rollDice() {
        return RANDOM.nextInt(11) + 1; // Random number between 1 and 11
    }

    private static void printDash() {
        System.out.println(String.valueOf('-').repeat(16));
    }

    private static boolean askToContinue() {
        System.out.print("If you want to continue press EnternInput | ");
        String input = SCANNER.nextLine();
        return input.isEmpty();
    }
}
