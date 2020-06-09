public class BMICalculatorFX {

    //private final JTextField txtMass = makePrettyTextField();
    //private final JTextField txtHeight = makePrettyTextField();
    //private final JButton btnCalc = makePrettyButton("Calculate BMI");
    
    public BMICalculatorFX() {
        /*
        btnCalc.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent arg0) {
                double mass;
                double height;
                try {
                    mass = Double.parseDouble(txtMass.getText());
                    height = Double.parseDouble(txtHeight.getText());
                } catch (NumberFormatException e) {
                    JOptionPane.showMessageDialog(self,
                            "Please enter a valid number for mass and height.",
                            "Input error",
                            JOptionPane.ERROR_MESSAGE);
                    return;
                }
                double result = calculateBMI(mass, height);
                JOptionPane.showMessageDialog(self,
                        "Your BMI is: " + (Math.round(result*100.0)/100.0),
                        "Your BMI result",
                        JOptionPane.PLAIN_MESSAGE);
            }           
        });
        */
    }
    
    protected double calculateBMI(double mass, double height) {
        return mass / Math.pow(height/100.0, 2.0);
    }

    
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() { new BMICalculatorFX(); }
        });
	}
}