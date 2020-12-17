import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.charset.Charset;
import java.io.IOException;
import java.util.*;

public class four {
    public static final String[] fields = { "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" };
    public static final String[] ecls = { "amb", "blu", "brn", "gry", "grn", "hzl", "oth" };

    public static void main(String[] args) {

        int answer1 = 0, answer2 = 0;
        List<String> lines = getInput("/home/khorne/git/advent_of_code/2020/4/4_input.txt");
        Map<String, String> fieldsToValues = new HashMap<String, String>();

        Iterator<String> it = lines.iterator();
        while (it.hasNext()) {
            String current = it.next();
            if (current.equals("")) {
                System.out.println(fieldsToValues.toString());
                if (testPartOne(fieldsToValues)) {
                    answer1++;
                    if (testPartTwo(fieldsToValues)) {
                        answer2++;
                    }
                }
                fieldsToValues.clear();
            } else {
                String[] splat = current.split(" |:");

                for (int i = 0; i < splat.length; i = i + 2) {
                    fieldsToValues.put(splat[i], splat[i + 1]);
                }

            }

        }
        System.out.println("Part 1: " + answer1);
        System.out.println("Part 2: " + answer2);
    }

    public static List<String> getInput(String filename) {
        List<String> lines = new LinkedList<String>();
        try {
            lines = Files.readAllLines(Paths.get(filename), Charset.defaultCharset());
        } catch (IOException e) {
            System.out.println(e.toString());
            System.exit(3);
        }
        lines.add("");

        return lines;
    }

    public static boolean testPartOne(Map<String, String> fieldsToValues) {
        for (String field : fields) {
            if (!fieldsToValues.containsKey(field)) {
                return false;
            }
        }
        return true;
    }

    public static boolean testPartTwo(Map<String, String> fieldsToValues) {

        int byr = Integer.parseInt(fieldsToValues.get("byr"));
        if (byr < 1920 || byr > 2002) {
            return false;
        }

        int iyr = Integer.parseInt(fieldsToValues.get("iyr"));
        if (iyr < 2010 || iyr > 2020) {
            return false;
        }

        int eyr = Integer.parseInt(fieldsToValues.get("eyr"));
        if (eyr < 2020 || eyr > 2030) {
            return false;
        }

        String hgt = fieldsToValues.get("hgt");
        if (hgt.contains("in") && hgt.contains("cm")) {
            return false;
        } else if (hgt.contains("in")) {
            int value = Integer.parseInt(hgt.substring(0, hgt.length() - 2));
            if (value < 59 || value > 76) {
                return false;
            }
        } else if (hgt.contains("cm")) {
            int value = Integer.parseInt(hgt.substring(0, hgt.length() - 2));
            if (value < 150 || value > 193) {
                return false;
            }
        } else {
            return false;
        }

        String hcl = fieldsToValues.get("hcl");
        if (!hcl.startsWith("#")) {
            return false;
        }
        if (hcl.length() != 7) {
            return false;
        }
        hcl = hcl.substring(1);
        for (int i = 1; i < hcl.length(); i++) {
            try {
                int t = Integer.parseInt(hcl, 16);
            } catch (NumberFormatException e) {
                return false;
            }
        }

        String ecl = fieldsToValues.get("ecl");
        boolean found = false;
        for (String eyes : ecls) {
            if (ecl.equals(eyes)) {
                found = true;
            }
        }
        if (!found) {
            return false;
        }

        String pid = fieldsToValues.get("pid");
        if (pid.length() != 9) {
            return false;
        }
        try {
            int t = Integer.parseInt(pid,10);
        } catch (NumberFormatException e) {
            return false;
        }

        return true;
    }
}