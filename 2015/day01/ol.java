import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.concurrent.atomic.AtomicInteger;

public class ol {
    public static void main(String[] args) throws IOException {
            // Part 1
//            int floor = ;
            System.out.println(
                    Files.readString(Paths.get("input.txt"))
                .chars()
                .map(c -> c == '(' ? 1 : c == ')' ? -1 : 0)
                .sum()
            );

            // Part 2
            String inp = Files.readString(Paths.get("input.txt"));
            AtomicInteger floorCounter = new AtomicInteger(0);
            int position = inp.chars()
                .map(c -> c == '(' ? 1 : c == ')' ? -1 : 0)
                .takeWhile(n -> floorCounter.addAndGet(n) >= 0)
                .toArray().length + 1;
            System.out.println(position);
    }
}
