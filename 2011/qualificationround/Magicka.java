package codejam2011;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;

public class Magicka {

	public static void main(String[] args) {
		try {
			FileIOManager manager = new FileIOManager("B-small-attempt0");

			int T = manager.getLineAsInteger();

			for (int t = 0; t < T; t++) {
				String[] linea = manager.getLine().split(" ");
				HashMap<HashSet<String>, String> baseElements = new HashMap<HashSet<String>, String>();
				ArrayList<HashSet<String>> opposedElements = new ArrayList<HashSet<String>>();

				int index = 0;
				int C = Integer.parseInt(linea[index]);
				index++;
				if (C != 0) {
					for (int c = 0; c < C; c++) {
						HashSet<String> set = new HashSet<String>();
						set.add(linea[index].split("")[1]);
						set.add(linea[index].split("")[2]);
						baseElements.put(set, linea[index].split("")[3]);
						index++;
					}
				}

				int D = Integer.parseInt(linea[index]);
				index++;
				if (D != 0) {
					for (int d = 0; d < D; d++) {
						HashSet<String> set = new HashSet<String>();
						set.add(linea[index].split("")[1]);
						set.add(linea[index].split("")[2]);
						opposedElements.add(set);
						index++;
					}
				}

				int N = Integer.parseInt(linea[index++]);
				ArrayList<String> recorridos = new ArrayList<String>();
				String[] caracteres = linea[index].split("");
				recorridos.add(caracteres[1]);
				String actual;
				for (int i = 2; i <= N; i++) {
					HashSet<String> set = new HashSet<String>();
					actual = caracteres[i];
					if (recorridos.size() != 0) {
						set.add(recorridos.get(recorridos.size() - 1));
					} else {
						recorridos.add(actual);
						continue;
					}
					set.add(actual);
					recorridos.add(actual);
					if (baseElements.get(set) != null) {
						recorridos.remove(recorridos.size() - 1);
						recorridos.remove(recorridos.size() - 1);
						recorridos.add(baseElements.get(set));
					}
					for (HashSet<String> opposed : opposedElements) {
						if (recorridos.containsAll(opposed)) {
							recorridos.clear();
						}
					}

				}

				manager.writeLine("Case #" + (t + 1) + ": " + recorridos);
			}
			manager.closeWriter();

		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
