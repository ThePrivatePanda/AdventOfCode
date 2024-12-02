import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Main {
    public static void main(String[] args) {
        try {
            // Read the input from "input.txt"
            String inp = new String(Files.readAllBytes(Paths.get("input.txt")));

            // Part 1
            int currFloor = 0;
            for (char c : inp.toCharArray()) {
                if (c == '(') {
                    currFloor += 1;
                } else if (c == ')') {
                    currFloor -= 1;
                }
            }
            System.out.println(currFloor);

            // Part 2
            currFloor = 0;
            int position = -1;
            for (int i = 0; i < inp.length(); i++) {
                char c = inp.charAt(i);
                if (c == '(') {
                    currFloor += 1;
                } else if (c == ')') {
                    currFloor -= 1;
                }
                if (currFloor < 0) {
                    position = i + 1; // 1-based index
                    break;
                }
            }
            System.out.println(position);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
