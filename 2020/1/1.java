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
		List<Integer> values = new LinkedList<Integer>();
		Integer year = Integer.valueOf(2020);
		Integer answer1= null, answer2 = null;
		try{
				lines = Files.readAllLines(Paths.get("1_input.txt"), Charset.defaultCharset());
		}catch(IOException e){
				System.out.println(e.toString());
				System.exit(3);
		}
		
		Iterator convertor = lines.iterator();
		while (convertor.hasNext()) {
			values.add(Integer.parseInt(convertor.next().toString()));
		}
		convertor = null;
		lines = null;
		Iterator<Integer> outer = values.iterator();
		while (outer.hasNext()) {
			Integer x = outer.next();
			Iterator<Integer> inner = values.iterator();
			while (inner.hasNext()) {
				Integer y = inner.next();
				Integer value = x.intValue() + y.intValue();
				if (value.compareTo(year) == 0) {
					answer1 = x.intValue() * y.intValue();
					break;
				}
			}
			if (answer1 != null) {
				break;
			}
		}
		Iterator<Integer> iter1 = values.iterator();
		while (iter1.hasNext()){
			if (answer2 != null) {
				break;
			}
			Integer x = iter1.next();
			Iterator<Integer> iter2 = values.iterator();
			while (iter2.hasNext()){
				if (answer2  != null){
					break;
				}
				Integer y = iter2.next();
				Iterator<Integer> iter3 = values.iterator();
				while(iter3.hasNext()){
					Integer z = iter3.next();
					Integer value = x.intValue() + y.intValue() + z.intValue();
					if (value.compareTo(year) == 0){
						answer2 = x.intValue() * y.intValue() * z.intValue();
						break;
					}
					
				}
			}
		}
	
		System.out.println(answer1.toString());
		System.out.println(answer2.toString());
	}	
}
