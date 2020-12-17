import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.charset.Charset;
import java.io.IOException;
import java.util.LinkedList;
import java.util.List;
import java.util.Iterator;
import java.math.BigInteger;
public class three {
	public static void main(String[] args) {
		List<String> lines = new LinkedList<String>();
		int answer1 = 0, column = 0;
        long answer2 = 1;
        String tree = "#";

		try{
				lines = Files.readAllLines(Paths.get("3_input.txt"), Charset.defaultCharset());
		}catch(IOException e){
				System.out.println(e.toString());
				System.exit(3);
		}
        int vertical = lines.size();
        int horizontal = lines.get(0).length();
        Object[] holder = lines.toArray();
        for (int i = 0; i < vertical; i++){
            if (holder[i].toString().substring(column,column+1).equals(tree)) {
                answer1++;
            }
            column = (column + 3) % horizontal;
        }
        int[][] steps = {{1,1},{3,1},{5,1},{7,1},{1,2}};
        
        for (int j = 0; j < steps.length; j++){
            long partTwoTemp = 0;
            column = 0;
            int stepVertical = steps[j][0], stepHorizontal = steps[j][1];
            for (int i = 0; i < vertical; i = i + stepHorizontal){
                if (holder[i].toString().substring(column,column+1).equals(tree)) {
                    partTwoTemp++;
                }
                column = (column + stepVertical) % horizontal;
            }
            answer2 = answer2 * partTwoTemp;
        }
        System.out.println("Part 1: "+answer1);
        System.out.println("Part 2: "+answer2);
    }
}