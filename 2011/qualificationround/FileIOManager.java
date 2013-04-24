package codejam2011;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class FileIOManager {

	public static String FILE_INPUT_PATH = "C:\\Users\\pochiero\\Downloads\\";
	public static String FILE_OUTPUT_PATH = "C:\\Users\\pochiero\\Desktop\\";

	private String inputFile;
	private String outputFile;
	private BufferedReader reader;
	private BufferedWriter writer;

	public FileIOManager(String filename) throws IOException {
		this.inputFile = FILE_INPUT_PATH + filename + ".in";
		this.outputFile = FILE_OUTPUT_PATH + filename + ".out";
		this.reader = new BufferedReader(new FileReader(inputFile));
		this.writer = new BufferedWriter(new FileWriter(outputFile, false));
	}

	public String getLine() throws IOException {
		return reader.readLine();
	}

	public int getLineAsInteger() throws IOException {
		return Integer.parseInt(reader.readLine());
	}

	public void writeLine(String line) throws IOException {
		writer.write(line + "\n");
	}

	public void closeWriter() throws IOException {
		writer.close();
	}

}
