// Calculator App

// Function to subtract numbers
function subtract(a, b) {
  return a - b;
}

// Function to add numbers
function add(a, b) {
  return a + b;
}

// Function to multiply numbers
function multiply(a, b) {
  return a * b;
}

// Function to divide numbers
function divide(a, b) {
  return a / b;
}

alert(
  "Welcome to the calculator app!\n\nThis app will help you calculate the result of your math problem."
);

alert(
  "Which operation would you like to perform?\n\n1. Add\n2. Subtract\n3. Multiply\n4. Divide"
);

while (true) {
  // Get user input
  let choice = prompt("\nEnter your choice : ");
  let choices = ["1", "2", "3", "4"];

  // Check if user input is valid
  if (choices.includes(choice)) {
    let a = parseInt(prompt("Enter first number: "));
    let b = parseInt(prompt("Enter second number: "));

    // Perform operation
    switch (choice) {
      case "1":
        alert(`${a} + ${b} = ${add(a, b)}`);
        break;
      case "2":
        alert(`${a} - ${b} = ${subtract(a, b)}`);
        break;
      case "3":
        alert(`${a} x ${b} = ${multiply(a, b)}`);
        break;
      case "4":
        alert(`${a} / ${b} = ${divide(a, b)}`);
        break;
    }
  } else {
    alert("Invalid choice. Please try again.");
  }
  break;
}
