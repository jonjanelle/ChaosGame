import java.awt.Dimension;

import javax.swing.*;
public class ChaosRunner {

	public static void main(String[] args) {
		JFrame gw = new JFrame();
		Dimension d = java.awt.Toolkit.getDefaultToolkit().getScreenSize();
		gw.setSize(d.width, d.height);
		gw.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		gw.setVisible(true);
		
		ChaosGame gamePanel = new ChaosGame();
		gw.add(gamePanel);
		

	}

}
