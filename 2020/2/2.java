import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.charset.Charset;
import java.io.IOException;
import java.util.LinkedList;
import java.util.List;
import java.util.Iterator;
public class one {
	public static void main(String[] args) {
		List<String> lines = new LinkedList<String>();
		int answer1 = 0, answer2 = 0;

		try{
				lines = Files.readAllLines(Paths.get("2_input.txt"), Charset.defaultCharset());
		}catch(IOException e){
				System.out.println(e.toString());
				System.exit(3);
		}

        Iterator<String> it = lines.iterator();
		while (it.hasNext()) {
			String line = it.next();

			String[] splat = line.split("-| |:");
			int occurences = 0;
			int lower = Integer.parseInt(splat[0]);
			int upper = Integer.parseInt(splat[1]);
			char letter = splat[2].charAt(0);
			String value = splat[4];
			boolean position_one = false, position_two = false;

			for(int i = 0; i < value.length();i++){
				char character = value.charAt(i);
				if (character == letter){
					occurences++;
					if (i+1 == lower){
						position_one = true;
					}
					if (i+1 == upper){
						position_two = true;
					}
				}
			}

			if(lower <= occurences && occurences <= upper){
				answer1++;
			}
			if (position_one^position_two){
				answer2++;
			}
		}

		System.out.println("Part 1: "+answer1);
		System.out.println("Part 2: "+answer2);
	}	
}
