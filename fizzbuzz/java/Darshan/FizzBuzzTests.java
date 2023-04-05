import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import org.junit.Test;
import static org.junit.Assert.assertEquals;


public class FizzBuzzTests {
    @Test
    public void testFizz() {
        String[] args = {"3", "5"};
        String expected = "1\r\n2\r\nFizz\r\n4\r\n5\r\n";
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outContent));
        fizbuz.main(args);
        String received = outContent.toString();
        assertEquals(expected, received);
    }

    //pushing for now, more tests to come...
    
}
