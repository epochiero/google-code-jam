package codejam2011;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;

public class CandySplitting {
	public static void main(String[] args) {
		try {
			FileIOManager manager = new FileIOManager("C-small-attempt0");

			int T = manager.getLineAsInteger();

			for (int t = 0; t < T; t++) {
				int N = manager.getLineAsInteger();
				String[] linea = manager.getLine().split(" ");
				int result = Integer.parseInt(linea[0]);
				String salida = null;
				ArrayList<Integer> orderedList = new ArrayList<Integer>();
				orderedList.add(result);

				for (int n = 1; n < N; n++) {
					result ^= Integer.parseInt(linea[n]);
					orderedList.add(Integer.parseInt(linea[n]));
				}
				Collections.sort(orderedList, Collections.reverseOrder());

				if (result != 0) {
					salida = "NO";
				} else {
					do {
						int sum = orderedList.get(0);
						int sumaFinal = sum;
						for (int i = 1; i < orderedList.size() - 1; i++) {
							sum ^= orderedList.get(i);
							sumaFinal += orderedList.get(i);
						}
						if (sum == orderedList.get(orderedList.size() - 1)) {
							salida = String.valueOf(sumaFinal);
						} else {
							orderedList.remove(orderedList.size() - 1);
						}

					} while (salida == null);
				}

				manager.writeLine("Case #" + (t + 1) + ": " + salida);
			}
			manager.closeWriter();

		} catch (IOException e) {
			e.printStackTrace();
		}

	}

}
