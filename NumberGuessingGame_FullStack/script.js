document.getElementById("runBtn").addEventListener("click", async () => {
  const inputNumber = document.getElementById("numField").value;
  const outputDiv = document.getElementById("output");

  if (!inputNumber) {
    outputDiv.textContent = "Please enter a number first!";
    return;
  }

  try {
    const response = await fetch("http://127.0.0", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ num_input: inputNumber }),
    });

    const data = await response.json();

    outputDiv.textContent = `Restlt: ${data.answer}`;
  } catch (error) {
    console.error("Connection Failed: ", error);
    outputDiv.textContent = "Error: Cannot connect to Python backend.";
  }
});
